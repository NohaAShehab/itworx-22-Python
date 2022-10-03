def askForInt(message):
    num = input(message)
    if num.isdigit():
        return int(num)

    print("---- You should valid digit----")
    return askForInt(message)


# print("----------------welcome to the inputs module ----------")
#
# age = askForInt("please enter your age : ")
# print(age)


def askForAlphaString(message):
    userinput = input(message)
    if userinput.isalpha():
        return userinput
    print("----- please enter valid alpha string : ")
    return askForAlphaString(message)

print("---------------------- Hello World --------------------- ")
# username  = askForAlphaString("please enter username: ")
# print(username)


g = 9.8