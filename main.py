# Here we go again, blank main.py
class Sandwich:
    def __init__(self, breadPieces, pbType, jType, presJelJam, breadType, cutOrNo, crustOrNo, cutDirection):
        self.breadPieces = breadPieces
        self.pbType = pbType
        self.jType = jType
        self.breadType = breadType
        self.cutOrNo = cutOrNo
        self.crustOrNo = crustOrNo
        self.presJelJam = presJelJam
        self.cutDirection = cutDirection

    def make_sandwich(self):
        if self.breadPieces < 2:
            print(f"Getting {self.breadPieces} piece of {self.breadType} bread")
        else:
            print(f"Getting {self.breadPieces} pieces of {self.breadType} bread")
        input("Press enter to continue")
        print(f"Getting {self.pbType} peanut butter")
        input("Press enter to continue")
        print(f"Putting peanut butter on bread")
        input("Press enter to continue")
        print(f"Getting {self.jType} {self.presJelJam}")
        input("Press enter to continue")
        print(f"Putting {self.jType} {self.presJelJam} on bread")
        if self.crustOrNo[0].lower() == "n":
            print(f"Cutting off crust")
            input("Press enter to continue")
        else:
            print("Leaving crust on")
        if self.cutOrNo[0].lower() == "y":

            print(f"Cutting sandwich {self.cutDirection}")
            input("Press enter to continue")
        else:
            print("Not Cutting Sandwich")

    def describe_sandwich(self):
        pass

    def serve_sandwich(self):
        if self.crustOrNo[0].lower() == "n":
            self.crustOrNo = "crust removed"
        else:
            self.crustOrNo = "crust on"
        if self.cutOrNo[0].lower() == "y":
            self.cutOrNo = f"{self.cutDirection} cut"
        else:
            self.cutOrNo = "uncut"
        print(f"Here is your {self.cutOrNo} {self.pbType} peanut butter "
              f"and {self.jType} {self.presJelJam} on {self.breadType} bread with {self.crustOrNo}")


def user_sandwich():
    breadPieces = int(input("How many pieces of bread would you like?\r\n"))
    breadType = input("What type of bread would you like to use?\r\n")
    pbType = input("Would you like smooth or crunchy peanut butter?\r\n")
    presJelJam = input("Would you like preserves, jelly, or jam?\r\n")
    jType = input(f"What fruit base would you like for your {presJelJam}\r\n")
    cutOrNo = input("Would you like your sandwich cut or no?\r\n")
    if cutOrNo[0].lower() == "y":
        cutDirection = input("What direction would you like the sandwich to be cut?\r\n")
    else:
        cutDirection = ""
    crustOrNo = input("Would you like the crust on?\r\n")
    sandwich = Sandwich(breadPieces=breadPieces, breadType=breadType, pbType=pbType,
                        presJelJam=presJelJam, jType=jType, cutOrNo=cutOrNo, crustOrNo=crustOrNo, cutDirection=cutDirection)
    return sandwich


if __name__ == "__main__":
    pizzas_sandwich = user_sandwich()
    pizzas_sandwich.make_sandwich()
    pizzas_sandwich.serve_sandwich()
