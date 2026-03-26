import psutil
import time
import os


def scan_processes():
    #Scans running processes and returns a list of suspicious ones.
    suspicious = []
    for process in psutil.process_iter(['pid', 'name', 'username']):
        try:
            # Check for python scripts
            if 'python' in process.info['name'].lower() and process.info['pid'] != os.getpid(): # Get the current process ID to avoid scanning itself.
                suspicious.append(process.info)
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass
    return suspicious

while True:
   found = scan_processes()
   if found:
    for p in found:
        print(f"[ALERT] Suspicious process detected: {p['name']} (PID: {p['pid']}, User: {p['username']})")
    time.sleep(5)  # Scan every 5 seconds  