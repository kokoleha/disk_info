import sys
import time
import threading
import psutil
from http.server import HTTPServer, CGIHTTPRequestHandler

def create_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()
threading.Thread(target=create_server).start()

def get_disk_info():
    disk_info = []
    for part in psutil.disk_partitions(all=False):
        usage = psutil.disk_usage(part.mountpoint)
        print('size_disk_info{device_name="'+part.device+'",mount_point="'+part.mountpoint+'"} '+ str(usage.total))
        print('used_disk_info{device_name="'+part.device+'",mount_point="'+part.mountpoint+'"} '+ str(usage.used))
    return 0

while True:
    sys.stdout=open("metrics","w")
    get_disk_info()    
    sys.stdout.close()
    time.sleep(1)
