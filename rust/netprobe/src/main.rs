// EwnaTool - Network Prober (Ping Sweep + Banner Grab)
// Created By 'Ewnaskia
// Kullanım: netprobe sweep <prefix>  |  netprobe banner <ip> <port>

use std::env;
use std::io::{Read, Write};
use std::net::{IpAddr, SocketAddr, TcpStream};
use std::str::FromStr;
use std::sync::{Arc, Mutex};
use std::thread;
use std::time::Duration;

fn sweep(prefix: &str) {
    let prefix = prefix.to_string();
    let alive = Arc::new(Mutex::new(Vec::new()));
    let mut handles = vec![];
    
    println!("[i] Tarama: {}.0/24", prefix);
    
    // 254 IP'yi 50 thread'e böl
    for chunk_start in (1..255).step_by(50) {
        let chunk_end = (chunk_start + 50).min(255);
        let p = prefix.clone();
        let alive = alive.clone();
        
        let handle = thread::spawn(move || {
            for i in chunk_start..chunk_end {
                let ip_str = format!("{}.{}", p, i);
                let ip = match IpAddr::from_str(&ip_str) {
                    Ok(i) => i,
                    Err(_) => continue,
                };
                // Port 80 veya 443 açıksa canlı say
                let addr80 = SocketAddr::new(ip, 80);
                let addr443 = SocketAddr::new(ip, 443);
                
                if TcpStream::connect_timeout(&addr80, Duration::from_millis(300)).is_ok()
                    || TcpStream::connect_timeout(&addr443, Duration::from_millis(300)).is_ok()
                {
                    println!("[+] {} AKTİF", ip_str);
                    alive.lock().unwrap().push(ip_str);
                }
            }
        });
        handles.push(handle);
    }
    
    for h in handles { let _ = h.join(); }
    println!("\n[✓] Toplam {} aktif host", alive.lock().unwrap().len());
}

fn banner(ip: &str, port: u16) {
    let addr = format!("{}:{}", ip, port);
    let socket = match addr.to_socket_addrs().map(|mut i| i.next()) {
        Ok(Some(a)) => a,
        _ => {
            println!("[-] Geçersiz adres");
            return;
        }
    };
    
    match TcpStream::connect_timeout(&socket, Duration::from_secs(3)) {
        Ok(mut stream) => {
            println!("[+] Bağlantı kuruldu: {}", addr);
            let _ = stream.set_read_timeout(Some(Duration::from_secs(3)));
            
            // HTTP isteği gönder
            let req = format!("HEAD / HTTP/1.0\r\nHost: {}\r\n\r\n", ip);
            let _ = stream.write_all(req.as_bytes());
            
            let mut buf = [0u8; 4096];
            match stream.read(&mut buf) {
                Ok(n) if n > 0 => {
                    println!("[i] Banner:");
                    println!("{}", String::from_utf8_lossy(&buf[..n]));
                }
                _ => println!("[-] Banner alınamadı"),
            }
        }
        Err(e) => println!("[-] Bağlantı hatası: {}", e),
    }
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        eprintln!("Kullanım:");
        eprintln!("  netprobe sweep <prefix>");
        eprintln!("  netprobe banner <ip> <port>");
        std::process::exit(1);
    }
    
    match args[1].as_str() {
        "sweep" => sweep(&args[2]),
        "banner" => {
            if args.len() < 4 {
                eprintln!("Port gerekli");
                std::process::exit(1);
            }
            let port: u16 = args[3].parse().unwrap();
            banner(&args[2], port);
        }
        _ => eprintln!("Bilinmeyen mod"),
    }
}