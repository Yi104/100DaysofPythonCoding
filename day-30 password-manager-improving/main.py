# day 30 improving part:
# line 43-58, use JSON, error expectation to avoid potential errors, try, except, else, finally
# Add new feature, a search button, search the website, a new window pop up, retrieve password from data.json with saved email and password


from tkinter import *
import random
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters=[random.choice(letters) for _ in range(random.randint(8,10))]
    password_numbers=[random.choice(numbers) for _ in range(random.randint(2,4))]
    password_symbols = [random.choice(symbols) for _ in range(random.randint(2, 4))]
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)
    password ="".join(password_list)
    # print(f"your password is {password}")
    password_input.insert(0,password)
    pyperclip.copy(password)  # automatically copy password
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email,
            "password":password,
        }
    }
    if len(website)== 0 or len(password)==0:
        messagebox.showinfo(title="Warning", message="Please fill all the field")

    else:
        try:
            with open("data.json", "r") as data_file:
                # Read old data from data_file
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,indent=4)
        else:
            # append new_data to data
            data.update(new_data)
            with open("data.json","w") as data_file: # save the update data to data_file
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- FIND PASSWORD  ------------------------------- #
def find_password():
    website=website_input.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)  # data is dictionary embedded dict (dict in a dict)

    except FileNotFoundError:
        messagebox.showinfo(title="Error1", message=f"no dataset not found")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title="INFO", message=f"email: {email}\n password: {password}")
        else:
            messagebox.showinfo(title="Error2", message=f"{website} data does not exist")






# ---------------------------- UI SETUP ------------------------------- #
window =Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock_img)
canvas.grid(column=1, row=0)

# Labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_label.focus()  # the cursor start at website box
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)


# Entries
website_input = Entry(width=25)
website_input.grid(column=1, row=1)
email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "yijin1380@gmail.com")  # auto input in the entry box
password_input = Entry(width=25)
password_input.grid(column=1, row=3)




# Bottons
generate_button = Button(text="Generate Password",command=generate_password,width=13)
generate_button.grid(column=2, row=3)
add_button = Button(text="Add",width=36, command=save)
add_button.grid(column=1,row=4, columnspan=2)
search_button= Button(text="Search",command=find_password,width =13)
search_button.grid(column=2,row=1)





window.mainloop()