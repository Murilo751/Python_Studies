def is_leap(year):
    leap = False
    if year % 400 == 0:
        return not (leap)
    if year % 4 == 0:

        if year % 100 == 0:
            return leap
        else:
            return not (leap)
    return leap


year = int(input())
print(is_leap(year))