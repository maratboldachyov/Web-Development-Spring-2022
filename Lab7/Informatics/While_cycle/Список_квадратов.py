n = int(input())
qrt = 1

while n > 0:
    if qrt ** 2 <= n:
        print(qrt ** 2)
        qrt += 1
    elif qrt ** 2 > n:
        break
