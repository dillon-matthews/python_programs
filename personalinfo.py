class PersonalData:
    def __init__(self, name='', address='', age=0, phone_number=''):
        self.__name = name
        self.__address = address
        self.__age = age
        self.__phone_number = phone_number

    def set_name(self, name):
        self.__name = name

    def set_address(self, address):
        self.__address = address

    def set_age(self, age):
        self.__age = age

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_name(self):
        return self.__name

    def get_address(self):
        return self.__address

    def get_age(self):
        return self.__age

    def get_phone_number(self):
        return self.__phone_number


def main():
    person1 = PersonalData("Dillon Matthews", "123 Main Street", 28, "555-123-4567")
    person2 = PersonalData("John Smith", "456 Elm Street", 32, "555-987-6543")
    person3 = PersonalData("Emily Johnson", "789 Oak Avenue", 25, "555-654-7890")

    print("Person 1")
    print(f"Name: {person1.get_name()}")
    print(f"Address: {person1.get_address()}")
    print(f"Age: {person1.get_age()}")
    print(f"Phone Number: {person1.get_phone_number()}")

    print("\nPerson 2")
    print(f"Name: {person2.get_name()}")
    print(f"Address: {person2.get_address()}")
    print(f"Age: {person2.get_age()}")
    print(f"Phone Number: {person2.get_phone_number()}")

    print("\nPerson 3")
    print(f"Name: {person3.get_name()}")
    print(f"Address: {person3.get_address()}")
    print(f"Age: {person3.get_age()}")
    print(f"Phone Number: {person3.get_phone_number()}")

main()
