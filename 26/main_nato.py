import pprint

import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}
data = pandas.read_csv('nato_alphabet.csv')

new_dict = { row.letter:row.code for (index,row) in data.iterrows()}
palabra = input('Por favor introduzca una palabra\n').upper()


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
for letra in palabra:
    print(f'{letra} de {new_dict[letra]}')
