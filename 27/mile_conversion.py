from tkinter import *

FONT = ('Courier',14,'bold')

window = Tk()
window.title('Distance Converter')

def calcular():
    numero_a_convertir = float(miles_input.get())
    kilo_result_label.config(text=f'{numero_a_convertir*1.609}')


miles_input = Entry()
miles_input.grid(column=1,row=0)
miles_input.focus()

miles_label = Label(text='Miles')
miles_label.grid(column=2,row=0)

is_equal = Label(text='is equal to')
is_equal.grid(column=0,row=1)

kilo_result_label = Label(text='0')
kilo_result_label.grid(column=1,row=1)

kilometer_label = Label(text='Km')
kilometer_label.grid(column=2,row=1)

calculate = Button(text='Calculate',command=calcular)
calculate.grid(column=1,row=2)




window.mainloop()