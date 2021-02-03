from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------------- SEARCH ------------------------------------- #
def search():
    entry = website_entry.get()
    try:
        with open("data.json") as f:
            data = json.load(f)
            email = data[entry]["email"]
            password = data[entry]["password"]
            pyperclip.copy(password)
            messagebox.showinfo(f"{entry}", f"email: {email}\nPassword: {password}\n(Password copied to clipboard)")
    except KeyError:
        messagebox.showerror("Error", "The specified website has no information saved")
    except FileNotFoundError:
        messagebox.showerror("Error", "No save data detected.  Add some websites before you can use this functionality")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
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
    new_data = {
        website_entry.get(): {
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }

    if len(website_entry.get()) == 0 or len(email_entry.get()) == 0 or len(password_entry.get()) == 0:
        messagebox.showerror(title="Error", message="Please do not leave any field blank")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open("data.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            with open("data.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
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

website_entry = Entry(width=21)
website_entry.grid(column=1, row=1)
website_entry.focus()

website = Button(text="Search", width=14, command=search)
website.grid(column=2, row=1)

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
