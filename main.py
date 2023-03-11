# Make a peanut butter and jelly sandwich
# 1. Get out bread Exception: What bread
## what is Bread? Get out? Where?
# variable bread -> define
# get out -> function take input, perform an action, return a result
# move to location (pass location) of item (pass item), open location
# 2. Get out peanut butter
## what is PB? What is get out? Where?
# 3. Get out jelly
## what is jelly? What is get out? Where?
# 4. Get out knife
## what is knife? What is get out? Where?
# 5. Open bread
# what is open? How do i open?
# 6. Open jar
# What is a jar? Which jar
# 7. Use knife to get pb
# 8. Spread on bread
# 9. Open jelly
# 10. put dirty knife in jelly
# 11. spread jelly on bread
# 12. close sandwich
# 13. put knife down
# 14. Sandwich


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


print(describe_bread(whiteBread, piecesofBread, crust))
print(describe_bread("Honey Wheat", 1, False))
print(describe_bread("Honey Wheat", 2, False))
