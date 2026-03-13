vowels = "aeiouAEIOU"
str = input()

if any(x in vowels for x in str):
    print("Yes")
else:
    print("No")