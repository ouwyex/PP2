def square_generator(N):
    for i in range(N + 1):
        yield i * i

def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

n = int(input())
print(",".join(map(str, even_generator(n))))

def div_by_3_and_4(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

def squares(a, b):
    for i in range(a, b + 1):
        yield i * i

for num in squares(3, 8):
    print(num)

def countdown(n):
    for i in range(n, -1, -1):
        yield i

for num in countdown(5):
    print(num)
