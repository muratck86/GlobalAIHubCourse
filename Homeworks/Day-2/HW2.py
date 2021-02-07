"""
Day - 2
2   Ask the user to input a single digit integer to a variable 'n'.
    Then, print out all of the even numbers from 0 to n(including n)
"""


# infinite loop until it encounters break keyword
while True:
    n = input("Enter a single digit number: ") # ask for input
    if n.isdigit() and len(n) == 1:  # check if the input is a single digit
        n = int(n)  # convert to integer
        break  # end the loop
    else:  # if the input is not a digit, show the message, the loop will anyway restart again
        print("Invalid input, please enter a single numeric digit")

# print the elements of the list produced by comprehension.
print([i for i in range(n + 1) if i % 2 == 0])
