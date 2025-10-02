height = 1.65 
weight = 84

bmi = weight/(height**2)

if bmi < 18.5:
    print('underweight')
elif bmi <= 24.9:
    print('normal weight')
else:
    print('overweight')