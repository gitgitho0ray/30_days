# binary converter, find longest sequence of 1's

def numero_uno(n):
    basetwo = []
    # counter = 0
    while n > 0:
        remainder = str(n % 2)
        basetwo.append(remainder)
        n = n // 2

    print(len(max(''.join(basetwo[::-1]).split('0'))))

numero_uno(6)
