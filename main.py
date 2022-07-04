from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def GenPass():

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = 7
    nr_symbols = 4
    nr_numbers = 5



    res = ""
    currlett = 0
    currsym = 0
    currnum = 0

    while True:
        rand = random.randint(1, 3)
        if rand == 1 and currlett != nr_letters:
            res += random.choice(letters)
            currlett += 1
        elif rand == 2 and currsym != nr_symbols:
            res += random.choice(symbols)
            currsym += 1
        elif rand == 3 and currnum != nr_numbers:
            res += random.choice(numbers)
            currnum += 1
        elif currlett == nr_letters and currsym == nr_symbols and currnum == nr_numbers:
            break
    password_entry.delete(0, END)
    password_entry.insert(0, res)
    pyperclip.copy(res)



# ---------------------------- PASSWORD MANAGEMENT ------------------------------- #
def validation():
    if len(email_entry.get()) > 0 and len(website_entry.get()) > 0 and len(password_entry.get()) > 0:
        return True


def add():
    new_data = {
        website_entry.get():{
            "email": email_entry.get(),
            "password": password_entry.get()
        }
    }
    if validation():
        yes = messagebox.askyesno(title="I am just a pop-up", message=f"Details entered:\n"
                                                                      f"Website: {website_entry.get()}\n"
                                                                      f"Email: {email_entry.get()}\n"
                                                                      f"Password: {password_entry.get()}\n"
                                                                      f"If you wish to proceed press yes?")
        if yes:
            try:
                with open("data.json", "r") as file:
                    temdata = json.load(file)
                    temdata.update(new_data)
            except ValueError:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                with open("data.json", "w") as file:
                    json.dump(temdata, file, indent=4)
            finally:
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)

    else:
        messagebox.showerror(title="Stop right there you criminal scam, you violated the law!!", message="You did not fill up all the lines, check it once more, please.")

def Search():
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
    except ValueError:
        messagebox.showerror(title="YOU DUMBASSS!", message="YOU HAVE TO ADD SOME DATA  FIRST, BEFORE YOU TRY TO SEARCH THEM...")
    else:
        try:
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {data[website_entry.get()]['email']}\n"
                                                              f"Password: {data[website_entry.get()]['password']}")
        except KeyError:
            messagebox.showerror(title="Ow man, I can't find the website.", message="You made an typo or the website exist only in metrix, try something else.")

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200, highlightthickness=0)
png = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=png)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

website_entry = Entry()
website_entry.grid(column=1, row=1, sticky="EW")
website_entry.focus()

search_button = Button(text="Search", command=Search)
search_button.grid(column=2, row=1, sticky="EW")

email_entry = Entry()
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")


password_entry = Entry()
password_entry.grid(column=1, row=3, sticky="EW")

passgen_button = Button(text="Generate Password", command=GenPass)
passgen_button.grid(column=2, row=3, sticky="EW")

add_button = Button(text="Add", command=add)
add_button.grid(column=1, row=4, columnspan=2, sticky="EW")

window.mainloop()
