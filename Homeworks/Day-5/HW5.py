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
dog1 = Dog("Karabas", 3, "Dogo")
print(cat1.name, cat1.kind)
cat1.sleep()
cat1.meaw()

print(dog1.name, "is", dog1.age, "years old")
dog1.age += 1
print(dog1.name, " grew old and is now", dog1.age, "years old")
dog1.sleep()
dog1.bark()
