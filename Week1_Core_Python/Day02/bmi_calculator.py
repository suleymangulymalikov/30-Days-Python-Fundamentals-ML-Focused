print("Enter you weight(kg): ")
mass = float(input())

print("Enter your height(m): ")
height = float(input())
height_square = height * height
bmi = mass/height_square

print(f"Your BMI is {bmi:.2f}%")

print("-"*40)
print("Underweight           | <5%")
print("Healthy Weight        | 5% - 85%")
print("At risk of overweight | 85% - 95%")
print("Overweight            | >95%%")
