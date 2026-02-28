import re
s=input()
pattern = r'\b\d{2}/\d{2}/\d{4}\b'
match=re.findall(pattern, s)
print(len(match))

#\b = word borders
#\d{x} = exactly x digits