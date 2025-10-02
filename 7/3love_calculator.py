# Love Calculator
# 💪 This is a difficult challenge! 💪 

# You are going to write a function called calculate_love_score() that tests the compatibility between two names.  To work out the love score between two people: 

# 1. Take both people's names and check for the number of times the letters in the word TRUE occurs.   
# 2. Then check for the number of times the letters in the word LOVE occurs.   
# 3. Then combine these numbers to make a 2 digit number and print it out. 

# name1 = "Angela Yu" name2 = "Jack Bauer"

# T occurs 0 times
# R occurs 1 time
# U occurs 2 times
# E occurs 2 times

# Total = 5 

# L occurs 1 time 
# O occurs 0 times 
# V occurs 0 times 
# E occurs 2 times 

# Total = 3

# Love Score = 53

n1 = input('Ingresa el primer nombre\n').lower()
n2 = input('Ingresa el segundo nombre\n').lower()
nombres = n1+n2
t = 'true'
l = 'love'

def calculate_love_score(nombre1,nombre2):
    tru = []
    lov = []
    porcentaje = ''
    
    for number in range(0,4):
        tru.append(nombres.count(t[number]))
        lov.append(nombres.count(l[number]))

    porcentaje = str(sum(tru)) + str(sum(lov))

    print(porcentaje)

calculate_love_score(n1,n2)
