def to_binary_func(x):
    bi = ''
    while x >= 2:

        mod = x % 2
        bi = str(mod) + bi
        x = x // 2

    bi = str(x) + bi
    return bi

decimal = int(input())
y = to_binary_func(decimal)
print(y.zfill(10))