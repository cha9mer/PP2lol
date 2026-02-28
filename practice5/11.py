import re
s=input()
pattern = r'[A-Z]'
match = re.findall(pattern, s)
print(len(match))