"""
Урок: https://www.youtube.com/watch?v=h-EFkclgCc8
"""

def gen():
    for x in range(1,3):
        print(x)
        yield x


a = gen()
print(next(a))