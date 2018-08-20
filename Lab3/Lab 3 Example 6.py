def letter_grade(mark):
    if mark <0 or mark >100:
        return None
    if mark>=90:
        return "A"
    elif mark>=80:
        return "B"
    elif mark>=70:
        return "C"
    elif mark>=60:
        return "D"
    else:
        return "E"

a=letter_grade(72)
print(a)

