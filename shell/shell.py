#! /usr/bin/env python3

import os, sys, re
from prompt import Prompt
from change_dir import ChangeDir
from redirect import Redirect

prompt = Prompt()

while 1:

    pid = os.getpid()
    rc = os.fork()

    if rc < 0:
        os.write(2, ("fork failed, returning %d\n" % rc).encode())
        sys.exit(1)

    elif rc == 0:
        args = prompt.talk()

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

        Redirect.checkRedirect(args)

        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir, args[0])
            try:
                os.execve(program, args, os.environ)
            except FileNotFoundError:
                pass

        os.write(2, (("Child: Could not exec %s\n" % args[0]).encode()))

        sys.exit(1)

    else:
        childPidCode = os.wait()
