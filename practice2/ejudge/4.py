a=int(input())
num=list(map(int, input().split()))
count = 0
for i in num:
    if i > 0:
        count=count+1
print(count)