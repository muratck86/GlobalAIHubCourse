"""
Day - 3
User login application:
    -Get Username and Password values from the user.
    -Check the values in an if statement and tell the user if they were successful.
Extra:
    -Try building the same user login application but this time, use a dictionary.
"""

# Using dictionary

# sample user login info, user passwords and remaining tries are stored in a list as values,
# and the usernames are the keys
user_logins = {"Murat": ["12345", 3], "ahmet": ["Ahmedo123", 3], "Rosie0": ["notRosie", 3]}

while True:
    try_name = input("Enter username: ").capitalize()  # get username
    key = user_logins.get(try_name, False)
    if key:  # check the username (case insensitive)
        if key[1] > 0:
            try_pass = input("Enter password for " + try_name + ": ")
            if key[0] != try_pass:
                key[1] -= 1
                if key[1] == 0:
                    print("Too many tries, user blocked, contact to your administrator.")
                    break
                print("Invalid password,", key[1], "tries remaining")
            else:
                print("Login successful.")
                break
    else:
        print("User not found")

