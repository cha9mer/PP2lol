n = int(input())
lst = list(map(str, input().split()))
sum = 0

for i in range(n):
    print(f"{i}:{lst[i]}", end=" ")