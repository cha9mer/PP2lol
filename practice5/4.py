import re
s=input()

digits = re.findall(r'\d', s)

print(" ".join(digits))

#\d - a number from 0 to 9
#" ".join(digits) - connects them into a string separated by a space