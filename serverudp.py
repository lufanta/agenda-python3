import socket
import pickle
import subprocess
import time
import gspread
import os
from gspread.exceptions import SpreadsheetNotFound, NoValidUrlKeyFound
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import HttpAccessTokenRefreshError
UDP_IP = str(os.system('hostname -I'))
UDP_PORT = 5005


sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # internet, UDP
sock.bind((UDP_IP, UDP_PORT))

#Credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('RPiServer-107f5dba0d1f.json', scope)
gc = gspread.authorize(credentials)
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/16md4AS1fLWV4L7-NkQhgST_O-JdCrzmFF9Oe0oGyNd0/edit#gid=0")

homework_sheet = sht.get_worksheet(0)
exams_sheet = sht.get_worksheet(1)

while True:
    try:

        print("Server iniciado ")

        print("Ip del servidor : {} \n Puerto {}".format(UDP_IP, UDP_PORT))
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        veces_loop = 0
        received = pickle.loads(data)

        homework = received[1]
        exams = received[0]
        homework_data = received[2]

        for i in homework.values():
            if veces_loop == 0:
                subject = "mate"
                cord1 = "A2"
                cord2 = "A3"
            elif veces_loop == 1:
                subject = "euskera"
                cord1 = "C2"
                cord2 = "C3"
            elif veces_loop == 2:
                subject = "gazte"
                cord1 = "B2"
                cord2 = "B3"
            print("{}. bueltan, i = {}".format(veces_loop, i))
            if i == "kendu":
                homework_sheet.update_acell(cord1, '')
                homework_sheet.update_acell(cord2, '')
            else:
                homework_sheet.update_acell(cord1, i)
                homework_sheet.update_acell(cord2, homework_data[subject])
            veces_loop += 1
        veces_loop = 0

        for i in exams.values():
            if veces_loop == 0:
                cord = "A2"
            elif veces_loop == 1:
                cord = "C2"
            elif veces_loop == 2:
                cord = "B2"
            print("{}. bueltan, i = {}".format(veces_loop, i))
            if i == "kendu":
                exams_sheet.update_acell(cord, "")
            else:
                exams_sheet.update_acell(cord, i)
            veces_loop += 1

        veces_loop = 0

    except KeyboardInterrupt:
        break
