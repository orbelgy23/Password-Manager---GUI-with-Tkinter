from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '*', '(', ')', '+']

    password_random_list1 = [random.choice(letters) for _ in range(random.randint(8, 10))]
    password_random_list2 = [random.choice(numbers) for _ in range(random.randint(2, 4))]
    password_random_list3 = [random.choice(symbols) for _ in range(random.randint(1, 2))]
    password_list = password_random_list1 + password_random_list2 + password_random_list3
    random.shuffle(password_list)

    password_random = "".join(password_list)  # join method

    entry_password.delete(0, END)
    entry_password.insert(0, password_random)
    pyperclip.copy(password_random)  # copy the password to clipboard


# ---------------------------- SAVE PASSWORD ------------------------------- #


def SaveData():  # we use Standard Dialog here
    website = entry_website.get()
    username = entry_username.get()
    password = entry_password.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0:  # input validation
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
        return

    is_ok = messagebox.askokcancel(title=website,
                           message=f"There are the details entered:\nEmail: {username}\n"
                           f"Password: {password}\nIs it ok to save?")

    if is_ok == 1:
        file = open("data.txt", "a")
        file.write(f"{website} | {username} | {password}\n")
        file.close()

    entry_website.delete(0, END)
    entry_username.delete(0, END)
    entry_password.delete(0, END)
    entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=60, pady=60)

img = PhotoImage(file="logo.png")

canvas = Canvas(height=200, width=190)
canvas.create_image(100, 95, image=img)
canvas.grid(row=0, column=1)

label_website = Label(text="Website")
label_website.grid(row=1, column=0)
label_username = Label(text="Email/Username", width=20)
label_username.grid(row=2, column=0)
label_password = Label(text="Password")
label_password.grid(row=3, column=0)

entry_website = Entry(width=50)
entry_website.grid(row=1, column=1, columnspan=3)
entry_website.focus()
entry_username = Entry(width=50)
entry_username.grid(row=2, column=1, columnspan=3)
entry_password = Entry(width=31)
entry_password.grid(row=3, column=1)

button_generate = Button(text="Generate Password", command=generate)
button_generate.grid(row=3, column=2)
button_add = Button(text="Add", width=42, command=SaveData)
button_add.grid(row=4, column=1, columnspan=3)


window.mainloop()

