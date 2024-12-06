class Pet:
    def __init__(self, name='', animal_type='', age=0):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age


def main():
    pet_name = input("Enter the name of your pet: ")
    pet_type = input("Enter the type of your pet (e.g., Dog, Cat, Bird): ")
    pet_age = input("Enter the age of your pet: ")

    pet = Pet()
    pet.set_name(pet_name)
    pet.set_animal_type(pet_type)
    pet.set_age(pet_age)

    print(f"Pet's Name: {pet.get_name()}")
    print(f"Pet's Type: {pet.get_animal_type()}")
    print(f"Pet's Age: {pet.get_age()}")

main()
