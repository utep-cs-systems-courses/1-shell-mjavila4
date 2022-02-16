import os, re

pattern = re.compile(r'\\')
matches = pattern.finditer(os.getcwd())
print(os.getcwd())
for match in matches:
    print(match)
print(os.getcwd()[])

