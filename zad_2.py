grades = [95, 82, 67, 54, 100, 73, 88, 42]

excellent = []
good = []
passed = []
failed = []

for grade in grades:
    if grade >= 90:
        excellent.append(grade)
    elif 70 <= grade <= 89:
        good.append(grade)
    elif 50 <= grade <= 69:
        passed.append(grade)
    else:
        failed.append(grade)

print("excellent:", excellent)
print("good:", good)
print("pass:", passed)
print("fail:", failed)