def main():
    # Defining multiple variables in one line
    data1, data2, data3, data4 = 15, 12, 10, 9

    # check type of a variable
    print(type(data1))

    # length of a string
    my_string = 'my string has n characters.'
    print(my_string)
    n = len(my_string)
    print("n =", n)

    # String formatting
    name = "Murat"
    print(f"Hello {name}")

    """Doc strings....
    this is a docstring
    it is also a string
    """
    # strings
    string = " Murat"
    print(string[-6])

    city = "afyonkarahisar"
    print(city)
    print(city[::2])
    print(city[:-1])
    print(city[-1])


if __name__ == '__main__':
    main()
