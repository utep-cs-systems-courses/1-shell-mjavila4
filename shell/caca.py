args = "wc poo.py | cd | poo | hello"
argsList = []

'''print(args)
args = args[args.index('|')+2:]'''

while '|' in args:
    argsList.append(args[:args.index('|')])
    args = args[args.index('|') + 2:]

argsList.append(args)

for i in argsList:
    print(i)
