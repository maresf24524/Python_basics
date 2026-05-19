events = [
    {"user": "filip", "ip": "192.168.1.5", "status": "success"},
    {"user": "admin", "ip": "185.220.101.4", "status": "failed"},
    {"user": "maria", "ip": "10.0.0.8", "status": "failed"},
    {"user": "root", "ip": "185.77.22.11", "status": "failed"},
    {"user": "guest", "ip": "172.16.0.5", "status": "success"}
]

threat_count = 0

# sem napíš kód
for event in events:
    if event["status"] == "failed" and event["ip"].startswith("185."):
        print("Threat detected!")
        print("User:", event["user"])
        print("IP:", event["ip"])
        threat_count += 1
print("Total threats detected:", threat_count)