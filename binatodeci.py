def binary_to_decimal(x):
    p2 = 1
    num = 0

    for i in range(len(x) - 1, -1, -1):
        if x[i] == '1':
            num = num + p2
        p2 = p2 * 2

    return num
print(binary_to_decimal("1011"))
