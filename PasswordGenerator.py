#Password Generator Project
import random
password_file = open("passwords.txt", "a")
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to my basic password generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Create a list. 
password = []

# Create a loop for the letters, symbols and characters.
for donkey in range(1, nr_letters + 1):
  password.append(random.choice(letters))

for donkey in range(1, nr_numbers + 1):
  password.append(random.choice(numbers))

for donkey in range(1, nr_symbols + 1):
  password.append(random.choice(symbols))

# Shuffle the order of the password list to make it harder to guess.
random.shuffle(password)

# Create a string
password_string = ""

# Create a loop which checks all items in the list and combine the previous value of the string with the new value.
for donkey in password:
  password_string += donkey

# Print the password, ask the user for the website/game name and ask the user if they would like to save the password.
print(f"Your password is:\n {password_string}")
website_or_gamename = input("For what website or game would you like to use this password for? \n")
save_password = input(f"Would you like to save {password_string} as your password? Type Y/Yes to save it. \n")

# Check user input and save the password + website/game name to a .txt file.
if save_password == "Y":
    password_file.write("\n")
    password_file.write(website_or_gamename + " password: " + password_string)
    print(f"Saved the password for {website_or_gamename}. The password is {password_string}.")
elif save_password == "Yes":
    password_file.write("\n")
    password_file.write(website_or_gamename + " password: " + password_string)
    print(f"Saved the password for {website_or_gamename}. The password is {password_string}.")
else:
    print("You did something wrong. Please try again.")


#Day 5 exercise of the Udemy 100 days of code course.
