import re
s=input()
pattern=r'cat|dog'
match = re.findall(pattern, s)
if match:
    print("Yes")
else:
    print("No")