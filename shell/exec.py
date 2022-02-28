import os, sys, re
from prompt import Prompt


class Exec:

    @staticmethod
    def execProgram(args):
        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir, args[0])
            try:
                os.execve(program, args, os.environ)
            except FileNotFoundError:
                pass
        os.write(2, ("Child:    Could not exec %s\n" % args[0]).encode())
        sys.exit(1)

    @staticmethod
    def execPipe(args):

        pr, pw = os.pipe()

        for f in (pr, pw):
            os.set_inheritable(f, True)

        rc1 = os.fork()

        if rc1 == 0:
            os.close(1)
            os.dup(pw)
            os.set_inheritable(1, True)

            for fd in (pw, pr):
                os.close(fd)

            Exec.execProgram([args[0]])

        else:
            rc2 = os.fork()

            if rc2 == 0:
                os.close(0)
                os.dup(pr)
                os.set_inheritable(0, True)

                for fd in (pw, pr):
                    os.close(fd)

                Exec.execProgram([args[2]])

            else:
                os.wait()

            for fd in (pw, pr):
                os.close(fd)

            os.wait()
