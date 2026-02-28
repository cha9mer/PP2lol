import re

s=input()
p=input()

match = re.findall(re.escape(p), s)
print(len(match))

