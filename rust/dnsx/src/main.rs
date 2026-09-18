// EwnaTool - Fast DNS Resolver
// Created By 'Ewnaskia
// Kullanım: dnsx <domain1> [domain2] ...

use std::env;
use std::net::ToSocketAddrs;

fn main() {
    let args: Vec<String> = env::args().skip(1).collect();
    if args.is_empty() {
        eprintln!("Kullanım: dnsx <domain> [domain2] ...");
        std::process::exit(1);
    }
    
    for domain in args {
        let query = format!("{}:0", domain);
        match query.to_socket_addrs() {
            Ok(addrs) => {
                let mut ips: Vec<String> = addrs.map(|a| a.ip().to_string()).collect();
                ips.sort();
                ips.dedup();
                for ip in ips {
                    println!("[+] {} -> {}", domain, ip);
                }
            }
            Err(_) => println!("[-] {} -> ÇÖZÜMLENEMEDİ", domain),
        }
    }
}