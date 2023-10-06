from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
import random
import json


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    password_list = [random.choice(letters) for number in range(nr_letters)]
    password_list += [random.choice(symbols) for number in range(nr_symbols)]
    password_list += [random.choice(numbers) for number in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #   password += char
    generated_password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(END, generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    website_name = website_entry.get().lower()
    email_username_text = email_username_entry.get()
    password_text = password_entry.get()
    new_data = {
        website_name: {
            "email": email_username_text,
            "password": password_text,
        }
    }
    is_empty = len(password_text) == 0 or len(website_name) == 0
    if is_empty:
        messagebox.showwarning("Oops", "Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askyesno(website_name, f"Your entries are as follows:\n\nEmail: {email_username_text}\n"
                                                  f"Password: {password_text}\n\nIs it correct for you to save?")
        if is_ok:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                with open("data.json", "w") as file:
                    data = {}
                    data.update(new_data)
                    json.dump(data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    data.update(new_data)
                    json.dump(data, file, indent=4)
            finally:
                website_entry.delete(0, END)
                # email_username_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- FIND PASSWORD ------------------------------- #


def find_password():
    the_website = website_entry.get().lower()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Oops!", "You don't have any saved account for this website!")
    else:
        if the_website in data:
            messagebox.showinfo("Account Details", f"Email: {data[the_website]['email']}\nPassword: {data[the_website]['password']}")
        else:
            messagebox.showerror("Oops!", "You don't have any saved account for this website!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create the canvas
canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)

# labels
website = Label(text="Website:")
website.grid(row=1, column=0)

email_username = Label(text="Email/Username:")
email_username.grid(row=2, column=0)

password = Label(text="Password:")
password.grid(row=3, column=0)

# entries
website_entry = Entry(width=26)
website_entry.grid(row=1, column=1)
website_entry.focus()

email_username_entry = Entry(width=44)
email_username_entry.grid(row=2, column=1, columnspan=2, padx=3)

password_entry = Entry(width=26)
password_entry.grid(row=3, column=1)

# buttons
generate_pwd = Button(text="Generate Password", command=generate_password)
generate_pwd.grid(row=3, column=2)

add = Button(text="Add", width=43, command=save)
add.grid(row=4, column=1, columnspan=2)

search = Button(text="Search", width=14, command=find_password)
search.grid(row=1, column=2)

window.mainloop()
