a = int(input())
b = int(input())
c = int(input())
d = int(input())

for i in range(1000, -1, -1):
    if a * pow(i, 3) + b * pow(i, 2) + c * i + d == 0:
        print(i, end=' ')

