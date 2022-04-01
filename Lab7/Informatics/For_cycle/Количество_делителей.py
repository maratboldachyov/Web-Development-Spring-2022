n = int(input())
cnt = 1

for i in range(1, n):
    if n % i == 0:
        cnt += 1
print(cnt)


