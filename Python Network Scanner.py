import os
import re
import subprocess
def get_gateway():
    data = os.popen("ipconfig").read()
    gateway = re.search(r"Default Gateway . . . . . . . . . : (\d+\.\d+\.\d+\.\d+)", data)
    if gateway:
        return gateway.group(1)
    return None
def get_network_base(gateway_ip):
    return ".".join(gateway_ip.split(".")[:3]) + "."
def ping(ip):
    return os.system(f"ping -n 1 -w 100 {ip} > nul") == 0
def get_arp_table():
    output = os.popen("arp -a").read()
    return output
def get_mac(ip, arp_data):
    pattern = rf"{ip}\s+([-\w]+)"
    match = re.search(pattern, arp_data)
    if match:
        return match.group(1)
    return "Unknown"
def get_hostname(ip):
    try:
        return subprocess.check_output(f"nslookup {ip}", shell=True).decode().split("Name:")[-1].strip().split("\n")[0]
    except:
        return "Unknown"
gateway_ip = get_gateway()
if not gateway_ip:
    print("❌ Could not detect network.")
    exit()
network_base = get_network_base(gateway_ip)
print(f"\n🌐 Scanning Network: {network_base}0/24")
print(f"📡 Gateway: {gateway_ip}\n")
active_devices = []
for i in range(1, 255):
    ip = network_base + str(i)
    if ping(ip):
        print(f"✅ Active: {ip}")
        active_devices.append(ip)
print("\n🔍 Fetching device details...\n")
arp_data = get_arp_table()
print("{:<16} {:<20} {:<30}".format("IP ADDRESS", "MAC ADDRESS", "HOSTNAME"))
print("-" * 70)
for ip in active_devices:
    mac = get_mac(ip, arp_data)
    hostname = get_hostname(ip)
    print(f"{ip:<16} {mac:<20} {hostname:<30}")
