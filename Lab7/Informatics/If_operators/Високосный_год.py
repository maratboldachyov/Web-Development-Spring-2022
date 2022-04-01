year = int(input())
leap = False

if year % 4 == 0:
    if year % 16 == 0:
        leap = True
    elif year % 25 == 0:
        leap = False
    else:
        leap = True

if leap:
    print("YES")
else:
    print("NO")

# 2 2 2 2 5 5

