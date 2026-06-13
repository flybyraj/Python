# Grade students based on marks

marks = int(input("Enter Marks : "))

if marks >= 90:
    grade = "A"
elif marks < 90 and marks >= 80:
    grade = "B"
elif marks < 80 and marks >=70:
    grade = "C"
elif marks < 70:
    grade = "D"

print("Grade obtained at" , marks , "marks is" , grade)