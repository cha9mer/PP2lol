import re
s=input()
pattern=re.compile(r'\b\w+\b')
matches = re.findall(pattern, s)
print(len(matches))

#re.compile = a compiled regex object that can be used multiple times