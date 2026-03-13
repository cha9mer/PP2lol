n = int(input())

a = list(map(int, input().split()))

print(sum(x != 0 for x in a))