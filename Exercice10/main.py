## Écrivez votre code ici !
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_details(self):
        print("Name:", self.name)
        print("Age:", self.age)

class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def display_details(self):
        super().display_details()
        print("Salary:", self.salary)


def main():
    employee1 = Employee("Martin", 26, 2000)
    employee1.display_details()

if __name__ == "__main__":
    main()
