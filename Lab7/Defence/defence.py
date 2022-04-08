# s = str(input())
# # max = 0
# # for i in s:
# #     if i > str(max):
# #         max = i
# # print(max)

def check(s, max, i):
    if i == len(s):
        return max
    if s[i] > str(max):
        max = s[i]
        i += 1
        return check(s, max, i)
    else:
        i += 1
        return check(s, max, i)


s = str(input())
print(check(s, -100, 0))


