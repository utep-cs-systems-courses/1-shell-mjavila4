import os, sys, re, fileinput


class Pipe:

    @staticmethod
    def checkOp(args):
        hasOperator = False
        for word in args:
            if word == "|":
                hasOperator = True
                break
        return hasOperator

    @staticmethod
    def checkIndex(args):
        index = -1
        counter = 0
        for word in args:
            if word == "|":
                index = counter + 1
                break
            counter += 1
        return index

    @staticmethod
    def checkPipe(args, pr, pw):
        index = Pipe.checkIndex(args)
        if Pipe.checkOp(args) and len(args) > index:

            os.close(1)
            os.dup(pw)

            for fd in (pr, pw):
                os.close(fd)

            firstArgs = args[:index-1]
            remArgs = args[index-1:]



        return firstArgs