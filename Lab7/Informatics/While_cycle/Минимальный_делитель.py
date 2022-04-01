n = int(input())
divisor = 2

while divisor != n + 1:
    if n % divisor == 0:
        print(divisor)
        break
    divisor += 1
