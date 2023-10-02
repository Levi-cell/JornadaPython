from ErrorHandling import*
class Person:
    def __init__(self, name, age, weight, height):
        self.age = age
        self.name = name
        self.weight = weight
        self.height = height
        self.weightUpdate = 0
        self.agingYears = 0

    def agePerson(self):
        self.agingYears = input("How many years has the person aged?")
        self.agingYears = convertIntWithTry(self.agingYears)

        if self.age < 21:
            self.height += 0.5 * (21 - self.age)
        self.age += self.agingYears
        return self.age, self.height

    def updateWeight(self):
        correctChoice = False
        while not correctChoice:
            choice = input("Type 1 if the person gained weight or type 2 if the person lost weight")
            if choice == "1":
                self.weightUpdate = input("How many kg did the person gain?")
                # self.weightUpdate = convertFloatWithTry(self.weightUpdate)

                self.weight += self.weightUpdate
                correctChoice = True
                return self.weight
            elif choice == "2":
                self.weightUpdate = input("How many kg did the person lose?")
                # self.weightUpdate = convertFloatWithTry(self.weightUpdate)

                self.weight -= self.weightUpdate
                correctChoice = True
                return self.weight
            else:
                print("Invalid choice, please try again.")

