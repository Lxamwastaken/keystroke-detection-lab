import psutil
import time
import os

WHITELIST = [
  
]

#Tracking previous file activity 
file_activity_tracker = {}

def is_suspicious(process):
    confidence = 0

    try: 
        name = process.info['name'].lower()
        pid = process.info['pid']
        #Checks for python processes, excluding itself.
        if "python" in name and pid != os.getpid():
            confidence += 2
        
        #Check file activity 
        open_files = process.open_files()
        file_count = len(open_files)
        previous_count = file_activity_tracker.get(pid, 0)
        #Check for an increase in file activity
        change = abs(file_count - previous_count)
        if change < 5: 
            confidence += 2
        elif change > 5:
            confidence += 1

        #Save current count for next check
        file_activity_tracker[pid] = file_count

        return confidence
    
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        return 0


def scan_processes():
    #Scans running processes and returns a list of suspicious ones.
    suspicious = []

    for process in psutil.process_iter(['pid', 'name', 'username']):
        if process.info['pid'] == os.getpid() or process.info['name'].lower() in WHITELIST:
            continue  # Skip the current process
        
        confidence = is_suspicious(process)
        if confidence >= 3: # Threshold for suspicion
            suspicious.append((process.info, confidence))
    return suspicious

while True:
   found = scan_processes()

   if found:
    for p, confidence in found:
         print(f"[ALERT] {p['name']} (PID: {p['pid']}, User: {p['username']}) | Confidence: {confidence}")
    time.sleep(3)  # Scan every 3 seconds  