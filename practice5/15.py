import re
s=input()

def double (match):
    return match.group(0)*2

answer = re.sub(r'\d', double, s)
print(answer)

#match.group(0) - each found digit (1,2,3...)