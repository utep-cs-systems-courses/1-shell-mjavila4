#! /usr/bin/env python3

import os, sys, re, fileinput
from prompt import Prompt
from change_dir import ChangeDir
from redirect import Redirect
from exec import Exec
from pipe import Pipe

prompt = Prompt()
pid = os.getpid()

pr, pw = os.pipe()

for f in (pr, pw):
    os.set_inheritable(f, True)

args = ''
argsList = []

while 1:

    args = prompt.talk()

    if args[0] == 'exit':
        sys.exit()
    
    rc = os.fork()
    
    if rc == 0:
        
        if not args:
            os.write(2, "Empty Command Line\n".encode())
            sys.exit()

        if args[0] == 'cd' and len(args) > 1:
            ChangeDir.change(args[1])
            sys.exit()
            
        if '|' in args:
            while '|' in args:
                nextArg = args[:args.index('|')]
                argsList.append(nextArg)
                args = args[args.index('|') + 2:]

                rc2 = os.fork()
                
                if rc2 == 0:
                    os.close(1)
                    os.dup(pw)
                    os.set_inheritable(1, True)

                    for fd in (pw, pr):
                        os.close(fd)
                    
                    Exec.execProgram(nextArg)

                else:
                    os.close(0)
                    os.dup(pr)
                    os.set_inheritable(0, True)
                    for fd in (pw, pr):
                        os.close(fd)
                    os.wait()

            argsList.append(args)





















