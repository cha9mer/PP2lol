a=int(input())
num=list(map(int, input().split()))
maxi = num[0]
mini = num[0]
for i in num:
    if i > maxi:
        maxi=i
    if i < mini:
        mini = i
for i in num: 
    if i == maxi:
        print(mini, end=" ")
    else:
        print(i, end=" ")