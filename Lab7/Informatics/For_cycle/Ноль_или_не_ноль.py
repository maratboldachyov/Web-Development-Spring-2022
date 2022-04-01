n = int(input())
pointer = 0
for i in range(n):
    a = int(input())
    if a == 0:
        print("YES")
        pointer += 1
        break
if pointer == 0:
    print("NO")
