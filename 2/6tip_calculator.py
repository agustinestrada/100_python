print('Welcome to the tip calculator!')
bill = int(input('What was the total bill? '))
tip = int(input('How much tip would you like to give 10, 12, 15? '))
number_of_people = int(input('How many people to split the bill? '))

multiplicador = (tip/100)+1

print(f'Each person should pay {round((bill*multiplicador)/number_of_people,2)}')