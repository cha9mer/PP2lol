n = int(input())
lst = list(map(str, input().split()))

for i in range(n):
    print(f"{i}:{lst[i]}", end=" ")