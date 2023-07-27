# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_to_float = float(height)
m2_height = (height_to_float**2)
bmi = (float(weight) / float(m2_height))
bmi_two = round(bmi)
if bmi <= float(18.5):
    print(f"Your BMI is {bmi_two}, you are underweight.")
elif bmi <= int(25):
        print(f"Your BMI is {bmi_two}, you have normal weight.")
elif bmi <= int(30):
    print(f"Your BMI is {bmi_two}, your are slightly overweight.")
elif bmi <= int(35):
    print(f"Your BMI is {bmi_two}, you are obese.")
else:
    print(f"Your BMI is {bmi_two}, you are clinically obese.")



