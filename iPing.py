#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print('\033[32m'+"""
*************************************
* #iPing                            *
* @IhsanSencan                      *
* github.com/ihsansencan/iPing      *
*************************************
"""+'\x1b[0m')
import subprocess
import os

print("\033[91m\033[1mSample: 192.168.2\x1b[0m")
ipAdrs = input("Ip Adres: ")
with open(os.devnull, "wb") as ver:
        try:
                for n in range(1, 254):
                        ip=ipAdrs+".{0}".format(n)
                        result=subprocess.Popen(["ping", "-c", "1", "-n", "-W", "2", ip],
                                stdout=ver, stderr=ver).wait()
                        if result:
                                print(ip, "\033[91m\033[1mClosed.\x1b[0m")
                        else:
                                print(ip, "\033[32mOpen.\x1b[0m")
        except KeyboardInterrupt:
                pass