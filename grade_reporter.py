scores = [72, 45, 90, 61, 38]

for score in scores:
    if score >= 70:
        grade = "A"
    elif score >= 60:
        grade = "B"
    elif score >= 50:
        grade = "C"
    elif score >= 40:
        grade = "D"
    else:
        grade = "F"

    print(f"Score: {score}, Grade: {grade}")