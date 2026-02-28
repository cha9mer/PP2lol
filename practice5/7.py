import re
s=input()
p=input()
r=input()

replacement = re.sub(p, r, s)
print(replacement)

#re.sub(what to replace, the replacement, where)