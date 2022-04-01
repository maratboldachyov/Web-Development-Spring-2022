x = int(input())
y = int(input())
i = 1
if x >= y:
    print(i)
while y > x:
    x *= 1.1
    i += 1
    if x >= y:
        print(i)
        break
