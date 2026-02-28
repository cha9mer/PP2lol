import re
s=input()
if re.match(r'^[A-Za-z].*\d$', s):
    print("Yes")
else:
    print("No")

#^ — the beginning of a line.
#[A-Za-z] — any letter (upper or lowercase).
#.* — any number of any characters (including zero).
#\d — any digit.
#$ — the end of a line.