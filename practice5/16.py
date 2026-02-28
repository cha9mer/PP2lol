import re
s=input()
match=re.search(r'Name:\s*(.+),\s*Age:\s*(.+)', s)
print(match.group(1), match.group(2))

#\s* = spaces
#(.+) = first/second capturing group (name and age)
