# Define global variables and functions out here
bread = input("What kind of bread would you like?\r\n")
peanutButter = input("Would you like crunchy or smooth peanut butter?\r\n")
jellyJamPreserves = input("Would you like jelly, jam, or preserves?\r\n")
knife = ""
jar = ""
plate = input("Will you be using a plate today?\r\n")


def getSandwichInfo():
    return bread, peanutButter, jellyJamPreserves, plate


if __name__ == "__main__":  # This is where our program begins
    print(getSandwichInfo())
