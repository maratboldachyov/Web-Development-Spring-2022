def fix(numObj, digits = 0):
    return f"{numObj:.{digits}f}"


n = int(input())
student_marks = {}
avg = 0.00
for _ in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()

for key, value in student_marks.items():
    if key == query_name:
        avg = sum(value)
print(fix((avg/3), 2))

