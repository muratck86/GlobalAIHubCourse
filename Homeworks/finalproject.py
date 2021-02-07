class Employee:
    def __init__(self, name, age, langs, salary):
        self.name = name
        self.age = age
        self.langs = langs
        self.salary = salary

    def __str__(self):
        return "Name: " +self.name + " Age: " + str(self.age) + " Salary: "\
               + str(self.salary) + " \nSpoken langs: " + str(self.langs)


class Manager(Employee):
    def __init__(self, name, age, langs, salary, department):
        super().__init__(name, age, langs, salary)
        self.department = department

    def __str__(self):
        return super().__str__() + "\nManager of: " + self.department


manager1 = Manager("Murat Can Kurt", 34, ["Turkish", "English"], 12000, "Software")
print(manager1)
