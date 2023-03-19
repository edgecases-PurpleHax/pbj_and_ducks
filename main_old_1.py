def describe_bread(typeOfBread, numberofPieces, crustOnOrNo):
    if crustOnOrNo == True:
        crustOnOrNo = "crust on"
    else:
        crustOnOrNo = "crust off"
    if numberofPieces < 2:
        return f"You are getting {numberofPieces} piece of {typeOfBread} with {crustOnOrNo}"
    else:
        return f"You are getting {numberofPieces} pieces of {typeOfBread} with {crustOnOrNo}"


my_dictionary = {
    "key": "value"
}
my_pbj = {
    "bread": "White Bread",
    "peanut_butter": "Crunchy",
    "jelly": "Strawberry",
    "crust": True,
    "drink": "Water"
}
if __name__ == "__main__":
    # string
    whiteBread = "White Bread"
    # int
    piecesofBread = 2
    # boolean True False
    crust = True
    # list
    mylist = [whiteBread, piecesofBread, crust, "Strawberry Jelly", "Water"]
    # input: ask user to add to list
    addition = input("Is there anything you want to \"add\" to the list?\r\n")
    if addition.lower()[0] == "y":  # check first (0) index of answer for y
        # if yes, ask for item to add
        whatToAdd = input("What would you like to add?")
        # add to list
        mylist.append(whatToAdd)
    else:  # if not y
        # do nothing
        pass
    for data in mylist:  # for each item in the list
        # print the item
        print(data)
        print(f"For my peanut butter and jelly, I want {my_pbj['bread']} bread.\r\n"
              f"I want {my_pbj['peanut_butter']} PB.\r\nI would like crust {my_pbj['crust']}")
#     print(describe_bread(whiteBread, piecesofBread, crust))
#     print(describe_bread("Honey Wheat", 1, False))
#     print(describe_bread("Honey Wheat", 2, False))
