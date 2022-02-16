import re

testString = "hello my abc name is mark abc marabc is coolABC!"

# 'r' is raw string
print(r"Hello World\n")

# Pattern to search in other calls
pattern = re.compile(r'abc')

matches = pattern.finditer(testString)
for match in matches:
    print(match)

print(testString[26:29])