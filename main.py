from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    let_list = [choice(letters) for char in range(randint(8, 10))]

    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    sym_list = [choice(symbols) for sym in range(randint(2, 4))]
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)
    num_list = [choice(numbers) for num in range(randint(2, 4))]

    password_list = let_list + sym_list + num_list

    shuffle(password_list)

    password = "".join(password_list)

    pyperclip.copy(password)

    password_entry.delete(0, END)
    password_entry.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_data():
    return_val = website_entry.get() + " | " + email_entry.get() + " | " + password_entry.get()

    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Error",message="Please do not leave any field blank")
    else:
        msg_text = f"These are the details entered:\nEmail: {email_entry.get()}\n" \
                   f"Password: {password_entry.get()}\nIs it okay to save?"
        is_okay = messagebox.askokcancel(title=website_entry.get(), message=msg_text)

        if is_okay:
            with open("data.txt", "a") as f:
                f.write(return_val+'\n')
                website_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=190)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 95, image=logo)
canvas.grid(column=1, row=0)

website = Label()
website.grid(column=0, row=1)
website.config(text="Website:")

website_entry = Entry(width=39)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email = Label()
email.grid(column=0, row=2)
email.config(text="Email/Username:")

email_entry = Entry(width=39)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, "sample@email.com")

password = Label()
password.grid(column=0, row=3)
password.config(text="Password:")

password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_password = Button(text="Generate Password", width=14, command=generate_password)
generate_password.grid(column=2, row=3)

add = Button(text="Add", command=save_data)
add.config(width=33)
add.grid(column=1, row=4, columnspan=2)

window.mainloop()
