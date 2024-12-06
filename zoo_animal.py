from animal_enums import AnimalClassification, Gender

class ZooAnimal:
    def __init__(self, name="", cage=0, aClass=None, age=0, gen=None, weight=0, injured=False, handler=""):
        self.name = name
        self.cageNumber = cage
        self.aClass = aClass
        self.age = age
        self.gender = gen
        self.weight = weight
        self.injured = injured
        self.handler = handler

    def __del__(self):
        pass

    def getName(self):
        return self.name

    def getCageNumber(self):
        return self.cageNumber

    def getClass(self):
        return self.aClass

    def getAge(self):
        return self.age

    def getGender(self):
        return self.gender

    def getWeight(self):
        return self.weight

    def getInjured(self):
        return self.injured

    def getHandler(self):
        return self.handler

    def setName(self, name):
        self.name = name

    def setCageNumber(self, cage):
        self.cageNumber = cage

    def setClass(self, aClass):
        self.aClass = aClass

    def setAge(self, age):
        self.age = age

    def setGender(self, gen):
        self.gender = gen

    def setWeight(self, weight):
        self.weight = weight

    def setInjured(self, injured):
        self.injured = injured

    def setHandler(self, handler):
        self.handler = handler
