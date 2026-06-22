from collections import Counter

log_file = "logs/auth.log"

failed_ips = []

# Read the log file
with open(log_file, "r") as file:
    for line in file:
        if "Failed password" in line:
            ip = line.split()[-1]
            failed_ips.append(ip)

# Count failed attempts by IP
ip_counts = Counter(failed_ips)

print("\n=== SentinelParser Report ===\n")

# Display results on screen
for ip, count in ip_counts.items():

    if count >= 3:
        severity = "HIGH"
    elif count == 2:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    print(f"{ip}: {count} failed login attempts | Severity: {severity}")

    if count >= 5:
        print(f"ALERT: Possible Brute Force Attack Detected from {ip}")

# Create report file
report = open("reports/incident_report.txt", "w")

report.write("=== SentinelParser Incident Report ===\n\n")
report.write(f"Total Failed Attempts: {len(failed_ips)}\n")
report.write(f"Unique Attack Sources: {len(ip_counts)}\n\n")

# Write results to report
for ip, count in ip_counts.items():

    if count >= 3:
        severity = "HIGH"
    elif count == 2:
        severity = "MEDIUM"
    else:
        severity = "LOW"

    report.write(
        f"{ip}: {count} failed login attempts | Severity: {severity}\n"
    )

    if count >= 5:
        report.write(
            f"ALERT: Possible Brute Force Attack Detected from {ip}\n"
        )

report.close()

print("\nAnalysis Complete")
