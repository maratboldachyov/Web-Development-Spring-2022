n = int(input())
fib0 = 0
fib1 = 1
fib2 = 0
cnt = 1

while fib2 < n:
    fib2 = fib0 + fib1
    fib0 = fib1
    fib1 = fib2
    cnt += 1

    if fib2 == n:
        print(cnt)
        break
    elif fib2 > n:
        print(-1)
        break
