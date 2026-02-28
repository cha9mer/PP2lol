import re

s=input()
p=input()

match = re.findall(re.escape(p), s)
print(len(match))

#re.escape(p) - any string is taken literally + special regex characters do not interfere