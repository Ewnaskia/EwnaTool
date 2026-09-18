// EwnaTool - Multi-Algorithm Hasher
// Created By 'Ewnaskia
// Kullanım: hasher <dosya|metin> <değer>

use std::env;
use std::fs;
use std::io::Read;
use sha2::{Sha256, Sha512, Digest};
use md5::Md5;
use sha1::Sha1;

fn hash_all(data: &[u8]) {
    let mut md5 = Md5::new();
    md5.update(data);
    println!("MD5    : {:x}", md5.finalize());
    
    let mut sha1 = Sha1::new();
    sha1.update(data);
    println!("SHA1   : {:x}", sha1.finalize());
    
    let mut sha256 = Sha256::new();
    sha256.update(data);
    println!("SHA256 : {:x}", sha256.finalize());
    
    let mut sha512 = Sha512::new();
    sha512.update(data);
    println!("SHA512 : {:x}", sha512.finalize());
    
    println!("Boyut  : {} byte", data.len());
}

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 3 {
        eprintln!("Kullanım: hasher <file|text> <değer>");
        std::process::exit(1);
    }
    
    let mode = &args[1];
    let value = &args[2];
    
    let data: Vec<u8> = match mode.as_str() {
        "file" => {
            fs::read(value).expect("Dosya okunamadı")
        }
        "text" => value.as_bytes().to_vec(),
        _ => {
            eprintln!("Mod: file veya text");
            std::process::exit(1);
        }
    };
    
    hash_all(&data);
}