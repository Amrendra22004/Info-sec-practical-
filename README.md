# Cybersecurity Practicals 1–4

A combined guide covering Network Tools, Password Cracking Tools, Nmap/Zenmap, and Burp Proxy.

---

## Practical 1 — Network Tools

### Overview
Network diagnostic tools help administrators monitor, troubleshoot, and analyze network activity.

### Tools & Usage

#### `ping`
Tests connectivity between two hosts.
```bash
ping google.com
ping -c 4 192.168.1.1       # Linux: send 4 packets
ping -n 4 192.168.1.1       # Windows
```

#### `ipconfig` / `ifconfig`
Displays IP configuration of network interfaces.
```bash
ipconfig              # Windows
ipconfig /all         # Windows – detailed info
ifconfig              # Linux/macOS
ifconfig eth0         # Specific interface
```

#### `tracert` / `traceroute`
Traces the route packets take to reach a destination.
```bash
tracert google.com         # Windows
traceroute google.com      # Linux
```

#### `arp`
Displays and modifies the ARP (Address Resolution Protocol) cache.
```bash
arp -a                # View ARP table
arp -d 192.168.1.1   # Delete an entry
```

#### `netstat`
Displays active connections, ports, and routing tables.
```bash
netstat -an           # All connections with port numbers
netstat -r            # Routing table
netstat -tulnp        # Listening ports (Linux)
```

#### `whois`
Retrieves domain registration information.
```bash
whois google.com
whois 8.8.8.8
```

---

## Practical 2 — Password Cracking Tools

### Overview
Password cracking tools test password strength 

### John the Ripper

**Installation:**
```bash
sudo apt install john          # Debian/Ubuntu
```

**Basic Usage:**
```bash
# Create a shadow-format file
john --wordlist=/usr/share/wordlists/rockyou.txt hashes.txt

# Show cracked passwords
john --show hashes.txt

# Single crack mode
john --single hashes.txt
```

**Generate a test hash:**
```bash
echo -n "password123" | md5sum > hash.txt
john --format=raw-md5 hash.txt
```

### Ophcrack

**Installation:**
```bash
sudo apt install ophcrack
```

**Usage:**
- GUI-based tool for Windows NTLM hash cracking using rainbow tables.
- Load SAM hashes → Load rainbow tables → Click **Crack**.
- Tables available at: https://ophcrack.sourceforge.io/tables.php

### Verifying Password Strength
| Criteria            | Weak       | Strong              |
|---------------------|------------|---------------------|
| Length              | < 8 chars  | ≥ 12 chars          |
| Character mix       | Only lower | Upper+lower+num+sym |
| Dictionary word     | Yes        | No                  |
| Time to crack (JtR) | Seconds    | Years               |

---

## Practical 3 — Nmap / Zenmap

### Overview
Nmap is a powerful network scanner used to discover hosts and services on a network.

**Installation:**
```bash
sudo apt install nmap       # Linux
# Zenmap (GUI) – download from https://nmap.org/zenmap/
```

### Common Nmap Commands

```bash
# Basic host scan
nmap 192.168.1.1

# Scan a range of IPs
nmap 192.168.1.1-254

# OS detection + version detection + script scan + traceroute
nmap -A 192.168.1.1

# Scan specific ports
nmap -p 22,80,443 192.168.1.1

# UDP scan
nmap -sU 192.168.1.1

# Stealth SYN scan
nmap -sS 192.168.1.1

# Save output to file
nmap -oN scan_result.txt 192.168.1.1
```

### Zenmap (GUI)
1. Open Zenmap.
2. Enter target IP in **Target** field.
3. Choose a profile (e.g., *Intense Scan*).
4. Click **Scan** and view results in the Output / Topology tabs.

---

## Practical 4 — Burp Suite Proxy

### Overview
Burp Suite is a web security testing tool. Its **Proxy** module intercepts HTTP/HTTPS traffic between a browser and a web server, allowing inspection and modification of requests/responses.

### Setup Steps

#### 1. Configure Burp Proxy
1. Open Burp Suite → **Proxy** tab → **Options**.
2. Ensure the proxy listener is set to `127.0.0.1:8080`.

#### 2. Configure Browser
- **Firefox:** Settings → Network Settings → Manual Proxy → `127.0.0.1`, Port `8080`.
- Or use the **FoxyProxy** extension for quick toggling.

#### 3. Install Burp CA Certificate (for HTTPS)
1. With proxy active, visit `http://burpsuite` in the browser.
2. Download and install the CA certificate into your browser's trusted store.

#### 4. Intercept & Modify a Request
1. Enable **Intercept is ON** in Proxy tab.
2. Browse to a target website (e.g., a login page on a test lab like DVWA).
3. Burp captures the request — modify parameters as needed.
4. Click **Forward** to send the modified request.

#### 5. Useful Burp Modules
| Module      | Purpose                                      |
|-------------|----------------------------------------------|
| Proxy       | Intercept & modify HTTP/S traffic            |
| Repeater    | Manually replay and tweak requests           |
| Intruder    | Automated fuzzing / brute force              |
| Decoder     | Encode/decode Base64, URL, HTML, etc.        |
| Scanner     | Automated vulnerability scanning (Pro only) |



---
