# Write a function finds the prime numbers between 0 and 100

# this function checks if a number is prime, returns True if it is...
def is_prime(n):
    if n == 2:  # check if the number is 2, return True if so
        return True
    elif n > 2:  # if the number is greater than 2,
        if n % 2 == 0:  # check if it is even or not, if it is even, so it can't be prime
            return False
        else:  # The number is odd, so check all the number from 2 to  the half of n
            for i in range(2, n // 2 + 1):
                if n % i == 0:  # if one of these numbers is a divisor, than n is not prime
                    return False
            return True  # if the code makes it through here, n is prime...
    else:  # If the number is not greater then 2 return False
        return False


# Wrapper function calls is_prime function for each of the numbers in range(n) and appends the numbers
# with True result to a list and returns the list.
def primes_to(n):
    return [x for x in range(n) if is_prime(x)]


# print prime numbers less than 100
print(primes_to(100))
