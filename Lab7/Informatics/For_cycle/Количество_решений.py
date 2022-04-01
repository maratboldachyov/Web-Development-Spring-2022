a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
cnt = 0

for i in range(0, 1001):
    if i == e:
        continue
    elif (a * pow(i, 3) + b * pow(i, 2) + c * i + d) / (i - e) == 0:
        cnt += 1
print(cnt)
