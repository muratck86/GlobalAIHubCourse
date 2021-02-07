class Employee:
    _employees = set()  # this is a class property keeps the set of every object of this kind.

    def __init__(self, name, age, salary):  # Object properties.
        self.name = name
        self.age = age
        self.salary = salary
        Employee._employees.add(self)  # add this new object to the set

    def raise_salary(self, amount=0, percent=0):  # raise salary by one of two ways.
        if amount > 0 and percent > 0:  # If both values are given, raise an Exception
            raise ValueError("Please provide only one of 'amount' or 'percentage' to raise salary")
        elif amount == 0:
            self.salary *= (percent + 100) / 100
        else:
            self.salary += amount

    # Class methods...
    @classmethod
    def get_employees(cls):  # Get the set of employee objects
        return cls._employees

    @classmethod
    def print_employees(cls):  # Print the names of the employees
        print("List of All Employees: ")
        for emp in cls._employees:
            print(emp.name)

    # Special method, called in print() function. When we pass an object directly to the print() function directly
    # it will call and print the returning value of this method instead of object reference
    def __str__(self):
        return "Name: " + self.name + " Age: " + str(self.age) + " Salary: "\
               + str(self.salary)


# Manager is also an employee, it has an additional property of department and languages.
class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.department = department
        self.langs = set()

    def get_langs(self):
        return str(self.langs)

    def add_lang(self, lang):
        self.langs.add(lang.capitalize())

    @classmethod
    def get_managers(cls):  # gives a list of manager objects
        employees = cls.get_employees()
        return [m for m in employees if isinstance(m, Manager)]

    @classmethod
    def print_managers(cls):  # Prints names and departments of managers
        print("List of Managers: ")
        managers = cls.get_managers()
        for man in managers:
            print(man.name, " / " +man.department)

    def __str__(self):
        return super().__str__() + "\n" + self.department + " Manager, Spoken languages: " + str(self.langs)


"""-------------------TESTS----------------------"""

# Object instantiation
manager1 = Manager("Murat Can Kurt", 34, 12000, "Software")
emp1 = Employee("Mahmut tas", 35, 7500)
emp2 = Employee("Ali baş", 42, 6750)
emp3 = Employee("Selim kaş", 48, 7000)

# __str__ method check
print(manager1)
print(emp1)

# language property and add_lang check
manager1.add_lang("engLISH")
manager1.add_lang("turkish")
print(manager1)

# Employee and Manager sets check
Employee.print_employees()
Manager.print_managers()


# Raise salary method check
emp1.raise_salary(500)
print(emp1)

manager1.raise_salary(percent=12)
print(manager1)
# emp1.raise_salary(500, 20) #raises ValueError
