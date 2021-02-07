"""
Day - 3
User login application:
    -Get Username and Password values from the user.
    -Check the values in an if statement and tell the user if they were successful.
Extra:
    -Try building the same user login application but this time, use a dictionary.
"""

#  Without dictionary...

# A sample user login information
username = "Murat"
password = "12345"

# the user has 3 try rights (for password)
counter = 3
while counter > 0:  # if the user has no tries end the loop
    try_name = input("Enter username: ")  # get username
    if try_name.capitalize() != username:  # check the username (case insensitive)
        print("User not found")
        continue  # If the username not found, don't run the rest of the code for this turn and restart the loop
    try_pass = input("Enter password for " + username + ": ")
    if try_pass != password:
        counter -= 1  # if the passsword is wrong, decrease the counter
        print("Wrong password. You have", counter, "tries remaining.")
    else:
        print("Login successful.")
        break
    if counter == 0:
        print("User blocked, please contact administrator.")
