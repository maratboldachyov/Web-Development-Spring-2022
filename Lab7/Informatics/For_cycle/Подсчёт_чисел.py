n = int(input())
cnt0 = 0
cnt1 = 0
cnt2 = 0

for i in range(n):
    a = int(input())
    if a == 0:
        cnt0 += 1
    elif a > 0:
        cnt1 += 1
    elif a < 0:
        cnt2 += 1
print(cnt0, cnt1, cnt2)
