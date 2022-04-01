def is_leap(year):
    leap = False
    if year % 4 == 0:
        if year % 8 == 0:
            leap = True
        elif year % 25 == 0:
            leap = False

    return leap


year = int(input())
print(is_leap(year))