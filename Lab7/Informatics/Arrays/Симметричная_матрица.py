n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

stop = False
for i in range(len(a)):
    for j in range(len(a[i])):
        if a[i][j] != a[j][i]:
            print("no")
            stop = True
            break
    if stop:
        break

if not stop:
    print("yes")
