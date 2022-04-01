n = int(input())

k = 0
log = 1
if n == 1:
    print(0)
while log < n:
    log *= 2
    k += 1
    if log >= n:
        print(k)
        break
