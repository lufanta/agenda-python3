import socket
import pickle
import subprocess
import time
import gspread
import os
from gspread.exceptions import SpreadsheetNotFound, NoValidUrlKeyFound
from oauth2client.service_account import ServiceAccountCredentials
from oauth2client.client import HttpAccessTokenRefreshError


#Credentials
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('RPiServer-107f5dba0d1f.json', scope)
gc = gspread.authorize(credentials)
sht = gc.open_by_url("https://docs.google.com/spreadsheets/d/16md4AS1fLWV4L7-NkQhgST_O-JdCrzmFF9Oe0oGyNd0/edit#gid=0")

homework_sheet = sht.get_worksheet(0)
exams_sheet = sht.get_worksheet(1)

while True:
    if time.localtime().tm_hour == 13 and  time.localtime().tm_min == 33 and time.localtime().tm_sec == 0:
        for i in range(3):
            if i == 0:
                print(1)
                cord = "A3"
            elif i ==1:
                print(2)
                cord = "B3"
            elif i == 2:
                print(3)
                cord ="C3"
            print(cord)
            days_left_before = homework_sheet.acell(cord).value
            print(days_left_before )
            if days_left_before != "":
                days_left_after = int(days_left_before) -1
            else:
                days_left_after = ""
            homework_sheet.update_acell(cord, str(days_left_after))
