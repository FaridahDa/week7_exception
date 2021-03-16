from person_errors import InvalidAge
class Person:
    def __init__(self, first_name, surname, age):
        self.first_name = first_name
        self.surname = surname
        self.age = age

    def firstName(self, first_name):
        self.first_name = first_name

    def surname(self, surname):
        self.surname = surname

    def age(self, age):
        self.age = int(age)
        if self.age < 0:
            raise InvalidAge("Please enter a correct age")

    def get_profile(self):
        return f"First Name: {self.first_name}\n" + f"Surname: {self.surname}\n" + f"Age: {self.age}"

person1 = Person('Asia','Sharif',23)
print(person1.get_profile())


