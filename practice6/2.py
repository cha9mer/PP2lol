def even(number):
    return number%2==0
n=int(input())
number=list(map(int, input().split()))
filtered=filter(even, number)
even_filtered=list(filtered)
print(len(even_filtered))