n = int(input())

lst = list(map(int, input().split()))

if all(x >= 0 for x in lst):
    print("Yes")
else:
    print("No")