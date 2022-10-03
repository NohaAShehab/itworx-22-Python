"""
    python file is considered to be a module (.py)

"""
#
# "1- import part of the module ------"
# from InputsModule import askForInt
#
# def addnums():
#     num1 = askForInt("please enter num1 : ")
#     num2 = askForInt("please enter num2 :  ")
#     res = num1 + num2
#     return res
#
#
# r = addnums()
# print(r)


# from InputsModule import askForInt,askForAlphaString
#
# day = askForInt("please enter day ")
# print(day)
#
#
# opinion= askForAlphaString("-0000000000000")
#
# print(opinion)

"2- ------- import all the module ---------------"
# import  InputsModule
#
# year = InputsModule.askForInt("please enter year : ")
# print(year)
#
# message = InputsModule.askForAlphaString("please leave your message: ")
# print(message)

# "3- alais the module name "
# import InputsModule as im
#
# num = im.askForInt("please enter number: ")
# print(num)
#
#
# print(im.g)
#
#
# im.g = 10
#
# print(im.g)
#
# # import InputsModule as nn
# # print(nn.g)import InputsModule as nn
# # print(nn.g)












from InputsModule import  *
askForInt("please enter num ")
askForAlphaString("please enter -000")
print(g)





