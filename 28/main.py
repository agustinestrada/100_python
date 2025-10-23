from tkinter import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    web = web_entry.get()
    email = email_entry.get()
    passw = pass_entry.get()
    
    with open('pass.txt', 'a') as data_file:
        data_file.write(f'{web}, {email}, {passw}\n')

    web_entry.delete(0,END)
    email_entry.delete(0,END)
    pass_entry.delete(0,END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Password Manager')
window.config(padx=50,pady=20)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file='logo.png')

canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels
web_label = Label(text='Website')
web_label.grid(row=1, column=0)
email_label = Label(text='Email/Username')
email_label.grid(row=2, column=0)
password_label = Label(text='password')
password_label.grid(row=3, column=0)

# Entries

web_entry = Entry(width=35)
web_entry.grid(row=1,column=1, columnspan=2)
email_entry = Entry(width=35)
email_entry.grid(row=2,column=1, columnspan=2)
pass_entry = Entry(width=21)
pass_entry.grid(row=3,column=1)

# Buttons

generate_button = Button(text='Generate Password')
generate_button.grid(row=3,column=3)
add_button = Button(text='Add',width=35, command=save)
add_button.grid(row=4, column=1,columnspan=2)


window.mainloop()