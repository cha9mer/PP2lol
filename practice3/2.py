#usual if the prime factor = 2, 3 , 5.
def isUsual (num):
    if num <= 0:
        return False
    for i in [2,3,5]:
        while num%i==0:
            num = num//i
    return num == 1

n = int(input())
print("Yes" if isUsual (n) else "No")