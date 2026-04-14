# 🌐 Python Network Scanner

A simple but powerful **Python-based network scanner** that discovers active devices on your local network. This tool is designed for beginners stepping into **networking, cybersecurity, and IT administration**, while still being useful for real-world diagnostics.

---

## 🚀 Features

* 🔍 Automatically detects your network range
* 📡 Scans all devices on the network (Ping Sweep)
* 🖥️ Displays:

  * IP Address
  * MAC Address
  * Hostname (if available)
* ⚡ Lightweight and fast
* 🧠 Beginner-friendly and easy to understand

---

## 📸 Example Output

```
🌐 Scanning Network: 192.168.1.0/24
📡 Gateway: 192.168.1.1

✅ Active: 192.168.1.1
✅ Active: 192.168.1.5
✅ Active: 192.168.1.10

IP ADDRESS       MAC ADDRESS         HOSTNAME
------------------------------------------------------
192.168.1.1      aa-bb-cc-dd-ee-ff   router.local
192.168.1.5      11-22-33-44-55-66   DESKTOP-ABC123
192.168.1.10     77-88-99-aa-bb-cc   Unknown
```

---

## 🛠️ How It Works

1. **Detects Default Gateway**

   * Uses `ipconfig` to identify your router (Access Point)

2. **Calculates Network Range**

   * Converts gateway into a `/24` network (e.g., `192.168.1.0/24`)

3. **Performs Ping Sweep**

   * Sends ping requests to all IPs (1–254)

4. **Retrieves MAC Addresses**

   * Uses `arp -a` to map IP → MAC

5. **Attempts Hostname Resolution**

   * Uses `nslookup` to identify device names

---

## ⚙️ Requirements

* Python 3.x
* Windows OS (uses `ipconfig`, `arp`, `netsh`)

---

## ▶️ Usage

1. Clone the repository:

```
git clone https://github.com/judeabdu/network-scanner.git
cd network-scanner
```

2. Run the script:

```
python scanner.py
```

---

## ⚠️ Limitations

* Some devices may not respond to ping (firewalls)
* Hostnames may not always be available
* Works best on **local networks (LAN/Wi-Fi)**
* Windows-only (for now)

---

## 🔥 Future Improvements

* [ ] Vendor detection (Apple, Samsung, etc.)
* [ ] Multi-threading (faster scanning)
* [ ] Export results to CSV/Excel
* [ ] GUI interface
* [ ] Cross-platform support (Linux/Mac)
* [ ] Integration with routers (e.g., MikroTik)

---

## 📚 Learning Purpose

This project is great for understanding:

* Computer Networking Basics
* IP Addressing & Subnetting
* ARP (Address Resolution Protocol)
* Network Discovery Techniques

---

## ⚖️ Disclaimer

This tool is intended for **educational purposes only**.
Do not use it on networks you do not own or have permission to scan.

---

## 🙌 Author

**SSENKINDU ABDUSHAKULUH**

Aspiring Network Engineer | Python Developer | IT Enthusiast

---

## ⭐ Support

If you like this project:

* Star ⭐ the repository
* Share with others
* Contribute improvements

---

💡 *“From learning code → to building real network tools.”*
