# This program calculates a somebody's
# body mass index (BMI).

height = float(input("Please enter your height in metres: "))
weight = float(input("Please enter your weight in kilograms: "))

bmi = weight / (height ** 2)

# I will also use the rounding function. 
# But i cannot claim credit for it as i 
# seen the idea on the discussion forum. 
bmi_round = (round(bmi,2))

print("BMI is", bmi_round)
