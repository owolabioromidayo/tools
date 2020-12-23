#!/usr/bin/python3

import sys

def  main():
    name = sys.argv[1]
    os.system("powershell.exe netsh wlan disconnect")
    os.system(f"powershell.exe netsh wlan connect name={sys.argv[1]}")
