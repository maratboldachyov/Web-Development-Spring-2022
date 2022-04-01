n = int(input())
arr = map(int, input().split())
maxi = 0

arr = set(sorted(list(arr)))
maxi = max(arr)
arr.remove(maxi)
maxi = max(arr)

print(maxi)


