
import pywhatkit
import subprocess
import time

def start_copyq_server():
    try:
        # Start CopyQ server
        subprocess.run(['copyq', 'start'])
        
        # Wait for some time to ensure the server has started
        time.sleep(2)
        
        print("CopyQ server started successfully!")

    except Exception as e:
        print(f"Error starting CopyQ server: {e}")


def send_msg():
    start_copyq_server()
    url = "/home/ow3nso/projects/python/django/excel3/receipts/1168.png"
    phonenumber  = "+254707394018"

    pywhatkit.sendwhats_image(phonenumber, url)

send_msg()