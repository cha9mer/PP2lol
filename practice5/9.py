import re
s=input()
pattern = r'\b\w{3}\b'
found = re.findall(pattern, s)
print(len(found))

#re.findall - finding all | re.search - finding only the first one
#\b - границы слова | \w{x} - exactly x characters