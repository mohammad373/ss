# ss

import os
import time
import sys
import socket
import requests
from colorama import Fore


def __target__():
    os.system("clear")
    time.sleep(1)
    print(Fore.YELLOW + "Hello , This Is My Test For dirb ;))))")
    time.sleep(1)
    target = input(Fore.RED + "\n[" + Fore.YELLOW + "!" + Fore.RED + "]" + Fore.YELLOW + " ~ " + Fore.BLUE + "Pleass Enter Domain Target" + Fore.GREEN + " ==>  " )
    if target == "" or None:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!] ~ Error : Your Domain Is None ;(")
            time.sleep(1)
            sys.exit()
        except:
            sys.exit()
    r1 = requests.get(str(target))
    if r1.status_code != 200:
        try:
            time.sleep(1)
            print(Fore.RED + "\n[!] ~ Error : Your Domain Is Not Found ;(")
            time.sleep(1)
            sys.exit()
        except:
            sys.exit()
    if r1.status_code == 200:
        print(Fore.GREEN + "[+] ~ Ok , Your Domain Is Found ;)")
    my_list = ["admin" , "ADMIN" , "admin/login" , "Admin" , "Admin/Login" , "ADMIN/LOGIN" , "admin/password" , "adminlogin" , "AdminLogin" , "ADMINLOGIN" , "ADMIN/ORG" , "PassAdmin" , "passadmin" , "admins/password"]
    for i in my_list:
        r2 = target + "/" + i
        r3 = requests.get(str(r2))
        if r3.status_code == 200:
            print(Fore.GREEN + "[+] ~ " + Fore.GREEN + str(r2))
        else:
            print(Fore.RED + "[-] ~ " + Fore.RED + str(r2))
__target__()
