n = int(input())

lst = list(map(str, input().split()))

print(max(lst, key=len))