n = int(input())
cnt = 1
fib0 = 0
fib1 = 1
fib3 = 0
if n == 0:
    print(fib0)
elif n == 1 or n == 2:
    print(fib1)
while cnt < n and n >= 3:
    fib3 = fib1 + fib0
    fib0 = fib1
    fib1 = fib3
    cnt += 1
    if cnt == n:
        print(fib3)
        break

