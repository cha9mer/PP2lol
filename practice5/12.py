import re
s=input()
digits = re.findall(r'\d{2,}', s)
print(" ".join(digits))

#\d - one digit
#{2,} - at least 2 times