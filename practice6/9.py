n = int(input())

a = list(map(str, input().split()))
b = list(map(str, input().split()))

inp = input()

x = dict(zip(a, b))

if inp not in x:
    print("Not found")
else:
    print(x[inp])