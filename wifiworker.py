import os, time, sys


"""
Simple script to shutdown wifi at specified time (24h format)
example:
    python3 wifiworker.py "00:00:00"

"""

def main():
    shutdown_time = sys.argv[1] #in format "H:M:S"
    while True:
        curr_time = time.strftime("%H:%M:%S", time.localtime())
        if curr_time == shutdown_time:
            os.system('powershell.exe netsh wlan disconnect')
            break

if __name__ == "__main__":
    main()
