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

while 1:

    args = prompt.talk()

    rc = os.fork()

    if rc < 0:
        os.write(2, ("Fork Failed, Returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:

        if not args:
            os.write(2, "Empty Command Line\n".encode())
            sys.exit()

        if args[0] == 'exit':
            sys.exit()

        if args[0] == 'cd' and len(args) > 1:
            ChangeDir.change(args[1])
            sys.exit()

        if args[0] == 'show':
            os.write(1, (os.getcwd() + "\n").encode())
            os.write(1, (os.environ['PATH'] + "\n").encode())
            sys.exit()

        args = Redirect.checkRedirect(args)
        args = Pipe.checkPipe(args, pr, pw)
        Exec.execProgram(args)

    else:

        if '|' in args:
            pipeFork = os.fork()

            if pipeFork == 0:
                os.close(0)
                os.dup(pr)
                for fd in (pw, pr):
                    os.close(fd)
                Exec.execProgram(args[Pipe.checkIndex(args):])

            else:
                os.wait()

        childPidCode = os.wait()
