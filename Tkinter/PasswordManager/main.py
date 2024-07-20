from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    pass_letters = [choice(letters) for _ in range(randint(8,10))]
    pass_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    pass_numbers = [choice(numbers) for _ in range(randint(2,4))]

    pass_list = pass_letters + pass_symbols + pass_numbers
    shuffle(pass_list)

    password = "".join(pass_list)
    pass_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty. ")
    
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n Email:{email}\n Password: {password}\n Is it okay to save?")

        if is_ok:
            with open("Tkinter/PasswordManager/data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}")
                web_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager}")
window.config(padx=40, pady=40)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="Tkinter/PasswordManager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

#LABELS
web_label = Label(text="Webiste:")
web_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0)

pass_label = Label(text="Password:")
pass_label.grid(row=3, column=0)

#ENTRY
web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "@email.com")

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

#BUTTONS
generate_pass = Button(text="Generate Password",command=generate_password)
generate_pass.grid(row=3, column=2)

add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)


window.mainloop()