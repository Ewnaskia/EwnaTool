// EwnaTool - High-Performance Port Scanner
// Created By 'Ewnaskia
// Derleme: cargo build --release
// Kullanım: scanner <ip> <start_port> <end_port> <threads>

use std::env;
use std::net::{IpAddr, SocketAddr, TcpStream};
use std::str::FromStr;
use std::sync::atomic::{AtomicUsize, Ordering};
use std::sync::{Arc, Mutex};
use std::time::Duration;
use std::thread;
use std::io::Write;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 5 {
        eprintln!("Kullanım: scanner <ip> <start> <end> <threads>");
        std::process::exit(1);
    }
    
    let ip = IpAddr::from_str(&args[1]).expect("Geçersiz IP");
    let start: u16 = args[2].parse().expect("Geçersiz başlangıç portu");
    let end: u16 = args[3].parse().expect("Geçersiz bitiş portu");
    let threads: usize = args[4].parse().unwrap_or(100);
    
    let total = (end - start + 1) as usize;
    let current = Arc::new(AtomicUsize::new(0));
    let open_ports = Arc::new(Mutex::new(Vec::new()));
    
    println!("[i] Hedef: {}", ip);
    println!("[i] Port aralığı: {}-{}", start, end);
    println!("[i] Thread sayısı: {}", threads);
    println!("[i] Toplam port: {}", total);
    println!();
    
    let start_time = std::time::Instant::now();
    let mut handles = vec![];
    
    for _ in 0..threads {
        let ip = ip;
        let current = current.clone();
        let open_ports = open_ports.clone();
        
        let handle = thread::spawn(move || {
            loop {
                let port = current.fetch_add(1, Ordering::SeqCst);
                if port >= total {
                    break;
                }
                let p = start + port as u16;
                let addr = SocketAddr::new(ip, p);
                
                if let Ok(_) = TcpStream::connect_timeout(&addr, Duration::from_millis(500)) {
                    let mut ports = open_ports.lock().unwrap();
                    ports.push(p);
                    println!("[+] Port {} AÇIK", p);
                }
            }
        });
        handles.push(handle);
    }
    
    for h in handles {
        let _ = h.join();
    }
    
    let elapsed = start_time.elapsed();
    let mut ports = open_ports.lock().unwrap();
    ports.sort();
    
    println!();
    println!("[✓] Tarama tamamlandı: {:.2}s", elapsed.as_secs_f64());
    println!("[✓] Açık port sayısı: {}", ports.len());
    println!("[✓] Açık portlar: {:?}", *ports);
}