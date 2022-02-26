#! /usr/bin/env python3

import os, sys, time, re, fileinput

pid = os.getpid()

pr, pw = os.pipe()
for f in (pr, pw):
    os.set_inheritable(f, True)

rc = os.fork()

if rc == 0:
    args = ["ls", "|", "sort"]
    os.close(1)
    os.dup(pw)

    for fd in (pr, pw):
        os.close(fd)
        
    print("Hello from child")
    
else:
    
    os.close(0)
    os.dup(pr)
    for fd in (pw, pr):
        os.close(fd)
    line = os.read(pr, 100)
    os.write(1, line)