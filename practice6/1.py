def square(number):
    return number**2
n=int(input())
number=list(map(int, input().split()))
squared=map(square, number)
print(sum(squared))

#map(function, iterable)