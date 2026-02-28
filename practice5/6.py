import re
s=input()
pattern = r'\S+@\S+\.\S+'
match = re.search(pattern, s)
if match:
    print(match.group())
else:
    print("No email")

#\S+ — one or more characters except a space
#@ — the @ symbol
#\. — a period (otherwise, in regex, it means "any character")
#match → object with info about match
#match.group() → text we want to print