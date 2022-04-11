print("This is a Mad Lib creator")
madlibP1 = input("Create your mad lib story before your first hint(adj,noun,verb), but don't include the hint\n")
typeHint1 = input("What kind of word do you want your player to use? (noun, verb, adjective, etc.)\n")
continue1 = input("Is there more to the story? Type 'yes' or 'no'\n")
if 'yes' in continue1:
    madlibP2 = input("Continue your mad lib story after your first hint up until your second hint. If you want two hints right next to each other, just input a space.\n")
    typeHint2 = input("What kind of word do you want your player to use? (noun, verb, adjective, etc.) NOTE: if you want to end your mad lib, just hit enter.\n")
    continue2 = input("Is there more to the story? Type 'yes' or 'no'\n")
    if 'yes' in continue2:
        madlibP3 = input("Continue your mad lib story after your second hint up until your third hint. If you want two hints right next to each other, just input a space.\n")
        typeHint3 = input("What kind of word do you want your player to use? (noun, verb, adjective, etc.) NOTE: if you want to end your mad lib, just hit enter.\n")
        continue3 = input("Is there more to the story? Type 'yes' or 'no' NOTE: The next one is the last iteration.\n")
        if 'yes' in continue3:
            madlibP4 = input("Continue your mad lib story after your third hint up until your fourth and last hint. If you want two hints right next to each other, just input a space.\n")
            typeHint4 = input("What kind of word do you want your player to use? (noun, verb, adjective, etc.\n")
            madlibEnd = input("End off your mad lib. If you want to end your mad lib off with your hint, just hit enter\n")
            print(madlibP1 + " " + "(" + typeHint1 + ")" + " " + madlibP2 + " " + "(" + typeHint2 + ")" + " " + madlibP3 + " " + "(" + typeHint3 + ")" + " " + madlibP4 + " " + "(" + typeHint4 + ")" + " " + madlibEnd)
        else:
            print(madlibP1 + " " + "(" + typeHint1 + ")" + " " + madlibP2 + " " + "(" + typeHint2 + ")" + " " + madlibP3 + " " + "(" + typeHint3 + ")")
    else:
        print( madlibP1 + " " + "(" + typeHint1 + ")" + " " + madlibP2 + " " + "(" + typeHint2 + ")" )
else:
    print(madlibP1 + " " + "(" + typeHint1 + ")")

#learned the "in" function as well as concatenation