import re
s=input()
pattern=re.compile(r'^\d+$')
if pattern.match(s):
    print("Match")
else:
    print("No match")

#^ — beginning of line
#\d+ — one or more digits
#$ — end of line