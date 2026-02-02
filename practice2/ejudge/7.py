a=int(input())
num=list(map(int, input().split()))
maxi = num[0]
maxi_index = 0
for i in range(a):
    if num[i] > maxi:
        maxi=num[i]
        maxi_index = i

print(maxi_index+1)