events = [
    {"user": "filip", "country": "Slovakia", "status": "success"},
    {"user": "admin", "country": "Russia", "status": "failed"},
    {"user": "maria", "country": "Germany", "status": "failed"},
    {"user": "root", "country": "North Korea", "status": "failed"},
    {"user": "guest", "country": "USA", "status": "success"},
    {"user": "backup_admin", "country": "China", "status": "failed"},
    {"user": "test_user", "country": "Iran", "status": "failed"},
    {"user": "peter", "country": "France", "status": "success"},
    {"user": "john", "country": "Brazil", "status": "failed"},
    {"user": "service_account", "country": "Russia", "status": "success"}
]

# CODE
threat_count = 0

for event in events:
    if event["status"] == "failed" and event["country"] in ["Russia", "North Korea", "China", "Iran"]:
        print(f"Threat detected from country: {event['country']}")
        threat_count += 1

print("Total geopolitical threats detected:", threat_count)