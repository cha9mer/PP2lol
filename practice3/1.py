#Given an integer number ,n write a function for checking whether this number si valid. Avalid number si one consisting of even digits only.
n=int(input())
ok = True
while n >= 1:
    if n%2==1:
        ok = False
        break
    n=n//10
if ok:
    print("Valid")
else:
    print("Not valid")