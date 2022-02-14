#! /usr/bin/env python3
import os, sys, re

args = ["wc", "program1.py"]

for dir in re.split(":", os.environ['PATH']):
    program = "%s/%s" % (dir, args[0])
    try:
        os.execve(program, args, os.environ)
        os.write(1, "Found".encode())
    except FileNotFoundError:
        pass
