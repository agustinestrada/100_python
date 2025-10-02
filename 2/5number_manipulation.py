height = 1.65 
weight = 84

bmi = weight/(height**2)

print(bmi)

print(type(round(bmi))) # INTEGER
print(type(round(bmi,2))) # FLOAT

# Assignment Operators

# += Suma lo que le digas a una variable
# -= Resta lo que le digas a una variable
# *= Multiplica a una variable
# /= Divide a una variable

score = 1

score += 1 # Es igual que hacer || score = score + 1
score -= 1 # Es igual que hacer || score = score - 1
score *= 5 # Es igual que hacer || score = score * 5
score /= 2 # Es igual que hacer || score = score / 2

# F-Strings || Son para mezclar distintos tipos de datos dentro de un string

print('Your score is '+ str(score))
print(f'Your score is {score}')