Keystroke Logging & Detection Lab (Python)

A security-focused project demonstrating how keyloggers work and why naive detection methods fail.

Disclaimer

This project is for educational purposes only. It demonstrates how keylogging techniques function and how basic detection strategies can be applied.
Do not run this software on systems without explicit permission.

Problem

Keyloggers are commonly used to capture sensitive user input, yet many developers lack a clear understanding of how they operate or how they can be detected.

Solution

This project consists of two components:

- Keylogger Simulation
  Captures and logs user keystrokes using Python
- Detection Script
  Scans running processes and applies a simple heuristic to flag suspicious activity

The objective is to highlight the gap between naive detection methods and real-world security requirements.

Features
- Keystroke capture using pynput
- Buffered logging (records complete input sequences)
- Handling of special keys (Backspace, Enter, Tab, etc.)
- Process scanning using psutil
- Heuristic-based detection of Python processes
- Real-time alert output

Installation
git clone https://github.com/Lxamwastaken/keystroke-detection-lab.git
cd keystroke-detection-lab
pip install pynput psutil

Run Keylogger

python keylogger.py
- logs keystrokes to keylog.txt
- Writes entries on Enter, Space, or Tab

Run Detector

python detector.py
- Continuously scans running processes
- Flags Python processes as "suspicious"
- Outputs alerts every 5 seconds

Example Output
[ALERT] Suspicious process detected: python.exe (PID: 1234, User: user)

How It Works

Keylogger
- Listens for keyboard events using pynput
- Stores keystrokes in a buffer
- Writes buffered input to a file on delimiter keys

Detector

- Iterates through running processes using psutil
- Identifies processes containing "python" in their name
- Flags them as potentially suspicious

Limitations

- High false positive rate
- Cannot distinguish between benign and malicious processes
- No behavioral or signature-based analysis
- Not suitable for real-world deployment

Detection Weaknesses

This detector can be easily bypassed:
- Renaming the process
- Compiling the script to an executable
- Running under a non-Python process name

This highlights the limitations of naive, name-based detection.

Key Insight

- Simple detection methods are easy to implement but ineffective in practice.

Roadmap

- Detect keyboard hook behavior
- Monitor file write patterns
- Reduce false positives
- Add visualization or logging interface
- Implement more advanced detection techniques

Why This Project Exists

This project was built to explore:

- How keyloggers capture user input
- Why naive detection methods fail
- What improvements are required for practical threat detection