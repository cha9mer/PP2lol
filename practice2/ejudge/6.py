a=int(input())
num=list(map(int, input().split()))
maxi = num[0]
for i in num:
    if i > maxi:
        maxi=i
print(maxi)