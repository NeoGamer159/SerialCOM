# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import serial

serialPort = serial.Serial(port="COM6", baudrate=115200, bytesize=8, timeout=2, stopbits=serial.STOPBITS_ONE)

message = "hovno"
serialString = ""
while 1:
    if serialPort.in_waiting > 0:
        serialString = serialPort.readline()
        print(serialString.decode("Ascii"))
        #tady jsem chtel porovnat prijaty data (serialString) jestli neobsahuji to co je v message
        #a kdyz jo tak neco
        if(message in serialString):
