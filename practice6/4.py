n = int(input())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

x = list(zip(a, b))

sum = 0

for i in range(n):
    sum += x[i][0] * x[i][1]

print(sum)