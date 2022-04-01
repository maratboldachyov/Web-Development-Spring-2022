n = int(input())
m = int(input())

while n != m:
    if n % 2 != 0 or n / 2 < m:
        n -= 1
        print("-1")
    elif n / 2 > m:
        n /= 2
        print(":2")
