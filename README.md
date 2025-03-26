# 🎵 MSHTA MP3 Polyglot Creator 🎭

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.x-blue.svg)](https://www.python.org/)

## 🔍 Overview

This tool creates dual-purpose MP3 files that:
- ▶️ Play normally in any media player
- 🌐 Execute an HTA payload when opened with `mshta.exe`

Perfect for red team exercises, penetration testing, and security research.

## ⚙️ How It Works

**The Magic Behind the Scenes:**
1. 🎵 MP3 players read from the beginning and stop at the end of valid MP3 data
2. 🔄 `mshta.exe` scans for HTA content anywhere in the file
3. 🥷 The payload remains invisible to basic file analysis

## 🚀 Features

- 💯 Preserves original MP3 playability
- 🔗 Configurable target URL
- 🛡️ Zero detection rate in basic antivirus scans
- 🧩 Clean separation between MP3 and HTA content

# Current Configuration
- Currently it's simply configured to open https://hacknexus.io upon executing the mp3 file. 

## 📋 Usage

```bash
# Clone the repository
git clone https://github.com/pentestfunctions/mshta_mp3_polyglot.git
cd mshta_mp3_polyglot

# Configure your MP3 and target URL in the script
# Then run
python3 mp3_hta_polyglot.py
```

### ⚠️ Configuration Variables

```python
# Modify these as needed
INPUT_MP3 = "backup.mp3"      # Your source MP3 file
OUTPUT_MP3 = "modified.mp3"   # The generated polyglot file
TARGET_URL = "https://example.com"  # URL to open on execution
```

## 🔮 Example Output

```
Simple MP3 Comment Polyglot Generator
[*] Input: backup.mp3
[*] Output: modified.mp3
[*] Target URL: https://hacknexus.io

[+] Successfully created modified.mp3
[+] The file can be played as a normal MP3
[+] When executed with mshta.exe, it will open https://hacknexus.io in the default browser

[+] Done! The file is ready.
[+] Current directory: /path/to/directory
[+] Full path to output file: /path/to/directory/modified.mp3
[+] Run the file with: mshta.exe "/path/to/directory/modified.mp3"
[+] When executed, it will open https://hacknexus.io in the default browser
```

## 💡 Advanced Tip

For even better stealth, create a small C program that:
- 🔍 Finds the MP3 in the current folder
- 🚀 Executes it using `mshta.exe`
- 🛡️ Contains no malicious code itself

## 🔒 Disclaimer

This tool is intended for **authorized security testing and educational purposes only**. Always obtain proper permissions before testing on any system or network you don't own.

## 🔗 Links

- [Personal Website](https://hacknexus.io)
- [GitHub](https://github.com/pentestfunctions)
