from zoo_animal import ZooAnimal
from animal_enums import AnimalClassification, Gender

def read_data_from_file(filename):
    with open(filename, 'r') as file:
        data = file.readlines()
    animals = []
    for line in data:
        parts = line.strip().split(',')
        animal = ZooAnimal(
            name=parts[0],
            cage=int(parts[1]),
            aClass=AnimalClassification[parts[2].upper()],
            age=int(parts[3]),
            gen=Gender[parts[4].upper()],
            weight=int(parts[5]),
            injured=parts[6].strip().lower() == "true",
            handler=parts[7]
        )
        animals.append(animal)
    return animals

def main():
    animal1 = ZooAnimal("Lion", 101, AnimalClassification.MAMMALS, 5, Gender.MALE, 400, False, "Handler1")
    animal2 = ZooAnimal("Parrot", 102, AnimalClassification.BIRDS, 2, Gender.FEMALE, 2, False, "Handler2")
    animal3 = ZooAnimal()
    animal3.setName("Shark")
    animal3.setCageNumber(103)
    animal3.setClass(AnimalClassification.FISH)
    animal3.setAge(10)
    animal3.setGender(Gender.MALE)
    animal3.setWeight(800)
    animal3.setInjured(False)
    animal3.setHandler("Handler3")

    animals_from_file = read_data_from_file("animals.txt")

    all_animals = [animal1, animal2, animal3] + animals_from_file

    for animal in all_animals:
        print(f"Name: {animal.getName()}, Cage: {animal.getCageNumber()}, Class: {animal.getClass().name}, "
              f"Age: {animal.getAge()}, Gender: {animal.getGender().name}, Weight: {animal.getWeight()}, "
              f"Injured: {animal.getInjured()}, Handler: {animal.getHandler()}")

if __name__ == "__main__":
    main()
