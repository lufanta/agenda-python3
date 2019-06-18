import socket
import os
import pickle
import subprocess
UDP_IP = "192.168.1.41"
UDP_PORT = 5005

def send(mensaje1, mensaje2, mensaje3):
    mensaje = [mensaje1, mensaje2, mensaje3]
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM) # internet, UDP
    sock.sendto(pickle.dumps(mensaje),(UDP_IP, UDP_PORT))


def new(changeable, decision, data):
    print("ikasgaia, 0.mate, 1.gazte, 2.euskera: ")
    subject = int(input())

    if decision == 1:
        what = str(input("Egin beharrekoa: "))
        time = int(input("Zenbat egun dituzu egiteko: "))
        if subject == 0:
            etxekolanak.update({'mate': what})
            data.update({'mate': time})
        elif subject == 1:
            etxekolanak.update({'gazte': what})
            data.update({'gazte': time})
        elif subject ==2:
            etxekolanak.update({'euskera': what})
            data.update({'euskera': time})
        return etxekolanak, data

    elif decision == 2:
        what = str(input("Azterketaren eguna: "))
        if subject == 0:
            changeable.update({'mate': what})
        elif subject == 1:
            changeable.update({'gazte': what})
        elif subject ==2:
            changeable.update({'euskera': what})
        return changeable


def delet(azterketak, etxekolanak):
    print("ikasgaia, 0.mate, 1.gazte, 2.euskera: ")
    subject = int(input())
    os.system('clear')
    print("0.etxekolanak, 1.azterketak")
    work = int(input())

    if subject == 0:
        subjectName = 'mate'
    elif subject ==1:
        subjectName = 'gazte'
    elif subject == 2:
        subjectName = 'euskera'

    if work == 0:
        etxekolanak[subjectName] = "kendu"
    elif work == 1:
        azterketak[subjectName] = "kendu"

    return etxekolanak, azterketak

def blank(etxekolanak, azterketak):
    etxekolanak = {'mate': "", "gazte": "", "euskera": ""}
    azterketak ={'mate': "", "gazte": "", "euskera": ""}
    return etxekolanak, azterketak


def start():
    print("Kaixo Lukas zer nahi duzu egin?\n 1. Etxekolan berriak jarri \n",
     "2. Azterketa berriak jarri\n 3. bidali RPI-ra datu guztiak \n 4.Lanak kendu \n 5.listak ikusi \n 6. listak berritu")
    ans = int(input(""))
    return ans


if __name__ == '__main__':
    etxekolanak = {'mate': "", "gazte": "", "euskera": ""}
    etxekolanak_data = {'mate': "", "gazte": "", "euskera": ""}
    azterketak = {'mate': "", "gazte": "", "euskera": ""}
    while True:
        decision = start()
        if decision == 1:
            etxekolanak, etxekolanak_data = new(etxekolanak, decision, etxekolanak_data)

            print(etxekolanak, etxekolanak_data)
        elif decision == 2:
            azterketak = new(azterketak, decision, etxekolanak_data)
            print(azterketak)
        elif decision == 3:
            send(azterketak, etxekolanak, etxekolanak_data)
        elif decision ==4:
            etxekolanak, azterketak = delet(azterketak, etxekolanak)
        elif decision == 5:
            print("Hauek dira etxekolanak, {} \n".format(etxekolanak))
            print("Hauek dira azterketak, {} \n".format(azterketak))
        elif decision == 6:
            etxekolanak, azterketak = blank(etxekolanak, azterketak)
