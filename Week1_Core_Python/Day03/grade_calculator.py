test1 = int(input("Enter your first test: "))
test2 = int(input("Enter your second test: "))
test3 = int(input("Enter your third test: "))

average = (test1 + test2 + test3)/3

grade = ""

if(average >= 90):
    grade = "A"
elif(average >= 80):
    grade = "B"
elif(average >= 70):
    grade = "C"
elif(average >= 60):
    grade = "D"
else:
    grade = "F"

print(f"Your Average is {round(average, 2)} - Grade: {grade}")