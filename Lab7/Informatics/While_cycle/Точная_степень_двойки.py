n = int(input())
two = 1

while n >= 1:
    if n == 1:
        print("YES")
        break
    elif n % 2 == 0:
        n /= 2
    else:
        print("NO")
        break
