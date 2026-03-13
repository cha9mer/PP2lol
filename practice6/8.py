n = int(input())

lst = set(map(int, input().split()))

sorted_lst = sorted(list(lst))

for i in sorted_lst:
    print(i, end=" ")