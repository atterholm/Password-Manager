from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    #generate random password
    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    #convert list to string
    password = "".join(password_list)

    #clear password field
    password_field.delete(0,END)
    password_field.insert(0, password)

    #save password to clipboard to easily copy password into website field
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():

    website = website_field.get()
    email = email_field.get()
    password = password_field.get()

    #checks that no fields are empty
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title="Woops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"Are these inputs correct? "
                                                      f"\nEmail: {email} \nPassword: {password}")

        #checks with user whether input is correct, saves if ok, otherwise does nothing
        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_field.delete(0, END)
                password_field.delete(0, END)




# ---------------------------- UI SETUP ------------------------------- #


# Window creation and configs
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50) #Adding padding

#Adding logo
canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image) #First two arguments are x and y positions
canvas.grid(row=1, column=2)


#Labels
website_label = Label(text="Website:")
website_label.grid(row=2, column=1)
email_label = Label(text="Email/Username:")
email_label.grid(row=3, column=1)
password_label = Label(text="Password:")
password_label.grid(row=4, column=1)

#Input fields
website_field = Entry(width=36)
website_field.grid(row=2, column=2, columnspan=2)
website_field.focus()
email_field = Entry(width=36)
email_field.grid(row=3, column=2, columnspan=2)
email_field.insert(END, "test@abc.com")
password_field = Entry(width=21)
password_field.grid(row=4, column=2)

#Buttons
password_button = Button(text="Generate Password", width=11, command=generate_password)
password_button.grid(row=4, column=3)
add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=5, column=2, columnspan=2)





#Open window
window.mainloop()