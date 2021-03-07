import os
import sys
import time
import threading
from http.server import HTTPServer, CGIHTTPRequestHandler

def create_server():
    server_address = ("", 8000)
    httpd = HTTPServer(server_address, CGIHTTPRequestHandler)
    httpd.serve_forever()
threading.Thread(target=create_server).start() #создаю поток для веб-сервера, чтобы после запуска сервера код продолжил выполняться
starttime=time.time()

while True:
    listofdisks_temp=os.popen("ls /dev/vd*").readlines()+os.popen("ls /dev/sd*").readlines()+os.popen("ls /dev/hd*").readlines()   #получаю список устройств
    listofdisks=[]
    sys.stdout=open("metrics","w")
    for i in range(len(listofdisks_temp)):
        listofdisks.append(listofdisks_temp[i][0: -1]) #привожу список устройств к виду /dev/vda
        df_command = ("df -B1 " + listofdisks[i])
        disk_info_temp = os.popen(df_command).readlines()  #получаю инфу о размере, занятом месте и точке монтирования
        disk_info=disk_info_temp[1].split()
        print('size_disk_info{device_name="'+listofdisks[i][5:]+'",Mount_point="'+disk_info[5]+'"} '+ disk_info[1]) #записываю понятные для prometheus метрики
        print('used_disk_info{device_name="'+listofdisks[i][5:]+'",Mount_point="'+disk_info[5]+'"} '+ disk_info[2])
    sys.stdout.close()
    time.sleep(60.0 - ((time.time() - starttime) % 60.0)) #пишу метрики каждую минуту
