def askForNoneEmptyString(message):
    mystr = input(message)
    if not mystr or mystr.isspace():
        print("------------- Invalid input-----------")
        return askForNoneEmptyString(message)

    return mystr


def askForInt(message):
    myint = input(message)
    if myint.isdigit():
        return myint

    print("------------- Invalid input-----------")
    return askForInt(message)




