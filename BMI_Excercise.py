weight = input("Enter your weight(kg) - ")
height = input("Enter your height(m) - ")

bmi= float(weight)/float(height)**2
bmi = round(bmi,2)
print(bmi)

if (bmi <= 18.5 ): 
    print("Underweight")
elif(bmi>18.5 and bmi < 25 ):
    print("Normal")
elif(bmi>25 and  bmi <= 30 ):
    print("Overweight")
else: 
    print("Obese")