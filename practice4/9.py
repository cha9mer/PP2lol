def powers_of_two(n):
    power = 0
    while power <= n:
        yield 2 ** power
        power += 1

n = int(input())

print(*powers_of_two(n))