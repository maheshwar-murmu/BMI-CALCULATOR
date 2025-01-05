print("Welcome to BMI calculator")
weight=float(input("Enter your weight:"))
height=float(input("Enter your height[in cm]:"))
result=weight/((height/100)**2)
BMI=round(result,2)
if(BMI<18.5):
     print(f"You are underweight:{BMI}")
elif(BMI>=18.5 and BMI<25):
    print(f"You have normal weight:{BMI}")
else:
     print(f"You are overweight:{BMI}")
