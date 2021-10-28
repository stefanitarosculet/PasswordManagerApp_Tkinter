from tkinter import *
from tkinter import messagebox
import random
import json

#Password Generator
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
def generate_pass():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    password_symbols = [random.choice(symbols) for _ in range(nr_numbers)]
    password_list = password_letters + password_numbers + password_symbols
    random.shuffle(password_list)
    password = "".join(password_list)
    # Inserting the password to the password entry field
    password_entry.insert(0,password)

def find_website():
# This function will be used for the search button
    try:
        with open("data.json",'r') as data_file:
            data = json.load(data_file)
            website = website_entry.get()
    except FileNotFoundError:
        messagebox.showinfo(message="Sorry, data file doesn't exist!")
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title = website,message=f"{email}\n{password}")
        else:
            messagebox.showinfo(message=f"Sorry, we connat find any records for {website}.")

# Creating the Canvas and all the entry fields, buttons and labels
window = Tk()
window.title("Password Manager")
window.config(padx = 50, pady =50)

canvas = Canvas(width = 200, height= 200)
locker_image = PhotoImage(file= "logo.png")
canvas.create_image(100, 100, image= locker_image)
canvas.grid(column= 1, row= 0)

website = Label(text = "Website:  ")
website.grid(column = 0, row = 1)
website_entry = Entry(width =35)
website_entry.focus()
website_entry.grid(column=1, row=1, rowspan=2)
website_button = Button(text = "Search",width = 10, command = find_website)
website_button.grid(column=2, row= 1)

email_user = Label(text="Email/Username:  ")
email_user.grid(column=0, row=3)
email_user_entry= Entry(width=35)
email_user_entry.insert(0,"stefanita.rosculet@gmail.com")
email_user_entry.grid(column=1, row=3, rowspan=2)

password = Label(text= "Password:")
password.grid(column=0, row = 5)

password_entry= Entry(width = 21)
password_entry.grid(column=1, row =5, columnspan=2)

generate_password = Button(text= "Generate Password", command = generate_pass)
generate_password.grid(column=2, row=5)



# This function will check for empty fields and if no empty fields are detected
# will confirm the details entered before writing to a .txt file
def save():
# Creating a new dictionary which I am gonna write to a json file
    new_dictionary = {
        website_entry.get(): {
            "email": email_user_entry.get(),
            "password": password_entry.get()
        }
    }
    if len(website_entry.get()) < 1 or len(email_user_entry.get()) < 1 or len(password_entry.get())< 1:
        messagebox.showinfo(title="Error", message="You've left some fields empty")
    else:
        # is_ok = messagebox.askokcancel(title = website_entry.get(), message= f"You have entered these details:\n{website_entry.get()}\n{email_user_entry.get()}\n{password_entry.get()}\nIs ok to Save?")
        # if is_ok:
# Catching the errors
        try:
            # Reading the json data
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            # Updating the json data with new values
            data.update(new_dictionary)
            # Writing the updated data to json
            with open("data.json", 'w') as data_file:
                json.dump(data, data_file, indent = 4)

        except FileNotFoundError:
            with open("data.json", 'w') as data_file:
                json.dump(new_dictionary, data_file, indent = 4)
        finally:
            website_entry.delete(0, END)
            # email_user_entry.delete(0, END)
            password_entry.delete(0, END)

add_button = Button(text="Add", width =36, command = save)
add_button.grid(column=1, row=7)


window.mainloop()