class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print("ZZzzZZZZzzz")


class Cat(Animal):
    def __init__(self, name, age, kind ):
        super().__init__(name, age)
        self.kind = kind

    def meaw(self):
        print("Meooooww meeeaww")


class Dog(Animal):
    def __init__(self, name, age, kind):
        super().__init__(name, age)
        self.kind = kind

    def bark(self):
        print("bow-wow, wow...")


cat1 = Cat("Pamuk", 2, "Tekir")
print(cat1.name,cat1.kind)
cat1.sleep()
cat1.meaw()
