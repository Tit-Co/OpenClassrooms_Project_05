class MyClass:
    def __init__(self, full_name):
        self.full_name=full_name
 
    def display_name(self):
        print(f"Le nom complet est : {self.full_name}")


class OtherClass:
    def __init__(self, first_name, name):
        self.first_name=first_name
        self.name=name
 
    def display_name(self):
        print(f"Nom complet : {self.first_name} {self.name}")


def main():
    my_class = MyClass('Nicolas MARIE')
    my_class.display_name()

    my_other_class = OtherClass('Nicolas', 'MARIE')
    my_other_class.display_name()

if __name__ == '__main__':
    main()
