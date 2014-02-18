# innerProd.py
# Calculates the inner product of two same-length lists


def innerProd(x, y):
    # the product of two vectors:
    #    a1*b1 + a2*b2...an*bn

    sum = 0
    for i in range(len(x)):
        sum += x[i] * y[i]

    return sum

def main():
    a = [1, 2, 3]
    b = [4, 5, 6]

    total = innerProd(a, b)

    print(total)


if __name__ in ['__console__', '__main__']:
    main()