class Reverse:
    def __init__(self, string):
        self.string = string
        self.index = len(string) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < 0:
            raise StopIteration
        char = self.string[self.index]
        self.index -= 1
        return char

s = input()

rev_iter = Reverse(s)
for c in rev_iter:
    print(c, end='')