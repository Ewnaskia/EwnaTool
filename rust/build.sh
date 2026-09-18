#!/bin/bash
# EwnaTool - Rust Core Builder
# Created By 'Ewnaskia

set -e

CYAN='\033[96m'
GREEN='\033[92m'
RED='\033[91m'
YELLOW='\033[93m'
RESET='\033[0m'

echo -e "${CYAN}╔════════════════════════════════════════╗${RESET}"
echo -e "${CYAN}║  EwnaTool Rust Core Builder            ║${RESET}"
echo -e "${CYAN}║  Created By 'Ewnaskia                  ║${RESET}"
echo -e "${CYAN}╚════════════════════════════════════════╝${RESET}"
echo

# Rust kontrolü
if ! command -v cargo &> /dev/null; then
    echo -e "${RED}[-] Rust/Cargo bulunamadı!${RESET}"
    echo -e "${YELLOW}[i] Kurulum:${RESET}"
    echo "    curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh"
    exit 1
fi

echo -e "${GREEN}[+] Cargo: $(cargo --version)${RESET}"
echo

# Her modülü derle
MODULES=(scanner flooder hasher dnsx netprobe)
mkdir -p bin

for mod in "${MODULES[@]}"; do
    echo -e "${CYAN}[i] Derleniyor: ${mod}${RESET}"
    cd "rust/${mod}"
    cargo build --release --quiet
    cp "target/release/${mod}" "../../bin/${mod}"
    cd ../..
    echo -e "${GREEN}[+] ${mod} hazır: bin/${mod}${RESET}"
done

echo
echo -e "${GREEN}[✓] Tüm Rust modülleri derlendi${RESET}"
ls -lh bin/