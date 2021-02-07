"""
Day - 2
1   Create a List and swap the second half of the list with the first half of the list and print
this list on the screen.
"""


# n : list length
n = 8

# create a list of n numbers from 1 to n
li = [x for x in range(1, n + 1)]

# print the list before swapping
print("Before:", li)

# half size of the list
half_size = len(li) // 2

# swap the first half of the list with the second half (if the list size is an odd number, the number in the
# middle will stay as it is.
if n % 2 == 1:
    li.append(li.pop(half_size))  # put the mid element to the end so it will come to its first place after swapping

# swap operation
for i in range(half_size):
    li.append(li.pop(0))  # remove the first element and append it to the end.

# print the swapped list
print("After :", li)
