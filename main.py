
# string
whiteBread = "White Bread"
# int
piecesofBread = 2
# boolean True False
crust = True


def describe_bread(typeOfBread, numberofPieces, crustOnOrNo):
    if crustOnOrNo == True:
        crustOnOrNo = "crust on"
    else:
        crustOnOrNo = "crust off"
    if numberofPieces < 2:
        return f"You are getting {numberofPieces} piece of {typeOfBread} with {crustOnOrNo}"
    else:
        return f"You are getting {numberofPieces} pieces of {typeOfBread} with {crustOnOrNo}"

if __name__ == "__main__":
    print(describe_bread(whiteBread, piecesofBread, crust))
    print(describe_bread("Honey Wheat", 1, False))
    print(describe_bread("Honey Wheat", 2, False))
