x = int(input())
p = int(input())
y = int(input())
i = 0

if x >= y or p == 0:
    print(i)

while y > x:
    if p != 0:
        x *= 0.01 * p + 1
        x = int(x)
        i += 1
    if x >= y:
        print(i)
        break

