#! /usr/bin/env python3

import os, sys, re
from prompt import Prompt

p = Prompt()
command = p.talk()

fdOut = os.open("output.txt", os.O_CREAT | os.O_WRONLY)
fdIn = os.open(command, os.O_RDONLY)

lineNum = 1
while 1:
    input = os.read(fdIn, 10000)
    if len(input) == 0:
        break
    lines = re.split(b"\n", input)
    for line in lines:
        strToPrint = f"{lineNum:5d}: {line.decode()}\n"
        os.write(fdOut, strToPrint.encode())
        os.write(1, strToPrint.encode())
        lineNum += 1
