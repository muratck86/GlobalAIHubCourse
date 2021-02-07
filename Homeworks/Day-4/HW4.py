def is_prime(n):
    if n == 2:
        return True
    elif n > 2:
        if n % 2 == 0:
            return False
        else:
            for i in range(2, n // 2 + 1):
                if n % i == 0:
                    return False
            return True
    else:
        return False


def primes_to(n):
    return [x for x in range(n) if is_prime(x)]


print(primes_to(100))
