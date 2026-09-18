<div align="center">

"""
╔═════════════════════════════════════════════════════════════════════════════╗
║                                                                             ║
║  ███████╗██╗    ██╗███╗   ██╗ █████╗   ████████╗ ██████╗  ██████╗ ██╗       ║
║  ██╔════╝██║    ██║████╗  ██║██╔══██╗  ╚══██╔══╝██╔═══██╗██╔═══██╗██║       ║
║  █████╗  ██║ █╗ ██║██╔██╗ ██║███████║     ██║   ██║   ██║██║   ██║██║       ║
║  ██╔══╝  ██║███╗██║██║╚██╗██║██╔══██║     ██║   ██║   ██║██║   ██║██║       ║
║  ███████╗╚███╔███╔╝██║ ╚████║██║  ██║     ██║   ╚██████╔╝╚██████╔╝███████╗  ║
║  ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═══╝╚═╝  ╚═╝     ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝  ║
║                                                                             ║
║                              Created By 'Ewnaskia                           ║
║                               v2.0.0 (Rust Core)                            ║
║                                                                             ║
╚═════════════════════════════════════════════════════════════════════════════╝
"""

# 🛠️ EwnaTool

### Multi-Purpose Cybersecurity Terminal Toolkit

**Rust Core + Python Interface**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Rust](https://img.shields.io/badge/Rust-1.70%2B-orange.svg)](https://www.rust-lang.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey.svg)]()
[![Version](https://img.shields.io/badge/Version-2.0.0-purple.svg)]()
[![Tools](https://img.shields.io/badge/Tools-73-brightgreen.svg)]()

A professional all-in-one cybersecurity toolkit. **Rust-powered core** for speed. **Python interface** for flexibility.

</div>

---

## 📖 About

**EwnaTool** is a terminal-based cybersecurity toolkit that brings together **73 professional tools** across **8 modules** in a single, colorful, menu-driven interface.

It combines two languages for the best of both worlds:

- **Rust** → handles heavy lifting (port scanning, packet flooding, hashing, DNS) at native speed — up to **90× faster** than pure Python
- **Python** → drives the user interface, menus, and integrations — fast to modify and extend

Whether you're doing **network recon**, **cryptography**, **OSINT**, **web analysis**, or **authorized penetration testing**, EwnaTool gives you everything in one place — no installation of 20 different tools required.

**Created by 'Ewnaskia** with a focus on speed, clarity, and a clean terminal experience.

---

## ✨ Features

### 🌐 Network Tools (12)
Local & Public IP · **High-speed port scanner** · **Ping sweep** · **DNS resolver** · **Banner grabber** · Traceroute · MAC address · Open ports · WHOIS · Reverse DNS · HTTP headers

### 🔐 Cryptography (12)
**Multi-algorithm hashing (MD5/SHA1/SHA256/SHA512)** · Base64 encode/decode · Secure password generator · XOR cipher · UUID v4 · ROT13 · Hex · URL encode/decode · Binary · Hash comparison

### 💻 System Info (7)
General system info · CPU details · Memory usage · Disk usage · Network interfaces · Running processes · Environment variables

### 📁 File Tools (9)
**File hashing** · XOR file encryption · File splitting · File merging · Pattern search · File metadata · File comparison · Base64 file encode/decode

### 🌍 Web Tools (10)
HTTP header analysis · Status codes · robots.txt · sitemap.xml · SSL certificate inspector · URL shortener · HTTP methods tester · Security headers audit · Cookie analysis · Redirect chain tracer

### ⚔️ Attack Simulation (6)
**High-speed UDP flood** · **TCP flood** · **HTTP flood** · Port knocking · SSH brute force · Reverse shell templates

### 🔍 OSINT (9)
IP geolocation · Domain WHOIS · Email validation · Phone formatting · Username search (10 platforms) · Have I Been Pwned · Domain intelligence · Subdomain discovery · IP reputation

### 🛠️ Utilities (8)
QR code generator · Random data · Countdown timer · Stopwatch · Calculator · Notepad · Bulk password generator · Lorem ipsum generator

### 🎨 Interface

- Colorful ANSI terminal UI
- ASCII art banner with author signature
- Loading spinner animations
- Hierarchical, easy-to-navigate menus
- Zero configuration — runs out of the box

---

## 📋 Requirements

| Component | Minimum | Recommended |
|-----------|---------|-------------|
| **Python** | 3.8 | 3.11+ |
| **Rust** | 1.70 | 1.75+ |
| **OS** | Windows 10 / Ubuntu 18.04 / macOS 10.14 | Latest |
| **RAM** | 64 MB | 256 MB |
| **Disk** | 5 MB | 50 MB (with Rust build) |

**Optional Packages:**

| Package | Purpose | Install |
|---------|---------|---------|
| `qrcode` | QR code generation | `pip install qrcode` |
| `paramiko` | SSH brute force | `pip install paramiko` |
| `whois` (system) | WHOIS lookups | Linux: `apt install whois`<br>macOS: `brew install whois` |

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/Ewnaskia/EwnaTool.git
cd EwnaTool
```

### 2. Install Rust (if not installed)

**Linux / macOS:**
```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
source $HOME/.cargo/env
```

**Windows:**
Download and run [rustup-init.exe](https://rustup.rs/)

Verify:
```bash
cargo --version
```

### 3. Build the Rust Core

```bash
chmod +x build.sh
./build.sh
```

This compiles 5 native binaries: `scanner`, `flooder`, `hasher`, `dnsx`, `netprobe`.

### 4. Install Python Dependencies (Optional)

```bash
pip install -r requirements.txt
```

### 5. Run EwnaTool

```bash
python3 ewnatool.py
```

**Windows:**
```cmd
python ewnatool.py
```

### ⚡ One-Line Install (Linux / macOS)

```bash
git clone https://github.com/Ewnaskia/EwnaTool.git && cd EwnaTool && chmod +x build.sh && ./build.sh && pip install -r requirements.txt && python3 ewnatool.py
```

### 🐳 Docker

```bash
docker build -t ewnatool .
docker run -it --rm ewnatool
```

### 🔧 Global Alias (Optional)

**Linux / macOS:**
```bash
echo "alias ewnatool='python3 $(pwd)/ewnatool.py'" >> ~/.bashrc
source ~/.bashrc
```

Now run from anywhere with just:
```bash
ewnatool
```

---

## 🎮 Usage

Launch the tool:

```bash
python3 ewnatool.py
```

You'll see the main menu:

```
  [1] 🌐 Network Tools        (12 tools)
  [2] 🔐 Cryptography         (12 tools)
  [3] 💻 System Info          (7 tools)
  [4] 📁 File Tools           (9 tools)
  [5] 🌍 Web Tools            (10 tools)
  [6] ⚔️  Attack Simulation   (6 tools - Rust)
  [7] 🔍 OSINT                (9 tools)
  [8] 🛠️  Utilities           (8 tools)
  [9] ℹ️  About
  [0] 🚪 Exit
```

Enter the number and press **Enter** to navigate into any module.

### Example Workflows

**High-speed port scan:**
```
EwnaTool > 1
Seçim > 3
Hedef IP > 192.168.1.1
Port aralığı > 1-65535
Thread > 500
```

**Generate a secure password:**
```
EwnaTool > 2
Seçim > 4
Uzunluk > 32
```

**OSINT username search:**
```
EwnaTool > 7
Seçim > 5
Kullanıcı adı > ewnaskia
```

### Direct Rust Binary Usage

The Rust binaries can also be called directly from the shell:

```bash
# Port scanner
./bin/scanner 192.168.1.1 1 65535 500

# UDP flood (60 seconds, 500 threads)
./bin/flooder udp 192.168.1.100 80 500 60

# Multi-hash
./bin/hasher text "hello"
./bin/hasher file /path/to/file.bin

# Batch DNS
./bin/dnsx example.com google.com github.com

# Ping sweep
./bin/netprobe sweep 192.168.1

# Banner grab
./bin/netprobe banner 192.168.1.1 80
```

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| `cargo: command not found` | Install Rust: `curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs \| sh` |
| `Eksik Rust binary` warning | Run `./build.sh` to compile the Rust core |
| `ModuleNotFoundError: qrcode` | `pip install qrcode` |
| `ModuleNotFoundError: paramiko` | `pip install paramiko` |
| ANSI colors not showing (Windows CMD) | Use Windows Terminal, or enable VT: `reg add HKCU\Console /v VirtualTerminalLevel /t REG_DWORD /d 1` |
| `whois: command not found` | Linux: `sudo apt install whois` — macOS: `brew install whois` |
| Rust build fails | Ensure Rust ≥ 1.70, run `rustup update` |
| `permission denied` on flood modules | Some flood features may require root/admin for raw sockets |

---

## ⚠️ Disclaimer

**FOR EDUCATIONAL AND AUTHORIZED TESTING PURPOSES ONLY.**

EwnaTool is designed for:
- ✅ Ethical hacking and penetration testing
- ✅ Security research and education
- ✅ Authorized network administration
- ✅ CTF competitions and lab environments
- ✅ Red team / blue team exercises

**You MUST NOT use this tool for:**
- ❌ Unauthorized access to systems
- ❌ Attacking infrastructure you do not own
- ❌ Any illegal activity

**The author assumes NO responsibility for misuse or damage caused by this tool.** Users are solely responsible for compliance with all applicable laws. Always obtain **written permission** before testing any system you do not own.

By using EwnaTool, you agree to these terms.

---

## 📜 License

**MIT License** — see [LICENSE](LICENSE) file for full text.

Copyright (c) 2026 'Ewnaskia

---

## 📬 Contact

| | |
|---|---|
| **Author** | 'Ewnaskia |
| **GitHub** | [@Ewnaskia](https://github.com/Ewnaskia) |
| **Repository** | [EwnaTool](https://github.com/Ewnaskia/EwnaTool) |
| **Issues** | [Report a bug](https://github.com/Ewnaskia/EwnaTool/issues) |

---

<div align="center">

**⭐ Star this project if you find it useful! ⭐**

Made with ❤️ by **'Ewnaskia**

</div>
