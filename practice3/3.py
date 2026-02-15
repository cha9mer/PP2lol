n=input().strip()
to_digit = {
    "ZER": "0", "ONE": "1", "TWO": "2", "THR": "3", "FOU": "4",
    "FIV": "5", "SIX": "6", "SEV": "7", "EIG": "8", "NIN": "9"}
to_word = {}
for k,v in to_digit.items():
    to_word[v]=k #zapolnyaem toword s pomoshiu todigit (reverse mapping)

for symbol in "+-*":
    if symbol in n:
        left, right = n.split(symbol)
        operator = symbol
        break

def tudasuda(part):
    number = ""
    for i in range(0, len(part),3):
        threep = part[i:i+3]
        number += to_digit[threep]
    return int(number)

number1 = tudasuda(left)
number2 = tudasuda(right)

if operator == "+":
    res = number1 + number2
elif operator == "-":
    res = number1 - number2
else:
    res = number1 * number2

strres = str(res)
ans = ""
for digit in strres:
    ans += to_word[digit]

print(ans)