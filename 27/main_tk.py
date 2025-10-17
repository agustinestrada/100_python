import tkinter as t
FONT = ('Courier',14,'bold')

window = t.Tk()
window.title('My First GUI Program')
window.minsize(width=500, height=300)

# Label

my_label = t.Label(text='I am a Label',font=FONT)
my_label.pack()

my_label['text'] = 'New Text'
my_label.config(text='New Text')

# Button
n = {'cantidad_de_clicks':0}

def button_clicked():
    n['cantidad_de_clicks'] += 1
    my_label.config(text=f'Button got clicked {n["cantidad_de_clicks"]} times')

def button_capture():
    valor = inputt.get()
    my_label.config(text=valor, font=FONT)

button = t.Button(text='Click Me', command=button_clicked)
button.pack()

inputt = t.Entry()
inputt.pack()
inputt.focus()

label2 = t.Label()
label2.pack()


button2 = t.Button(text='Capturar Input', command=button_capture)
button2.pack()

window.mainloop()