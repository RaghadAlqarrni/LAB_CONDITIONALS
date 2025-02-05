
weight = float(input("what is your weight: "))
height = float(input("what is your height: "))


bmi = weight / (height ** 2)

print("Your BMI is: {}".format(bmi))

if bmi < 18.5:
     print("You are underweight. Watch your health.")
elif 18.5 <= bmi < 24.9:
        print("You are fit & healthy.")
else:
        print("You are overweight; you need to work out more and watch your diet.")