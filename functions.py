# def helloworld():
#     print("----- Hello World ----- ")
#
# helloworld()
#

###################
# def helloworld():
#     print("----- Hello World ----- ")
#
# x = helloworld()
# print(x)

####################33
# def helloworld():
#     print("----- Hello World ----- ")
#     return
#
# x = helloworld()
# print(x)

####################################
# def sayHello(name):
#     print(f"----- Hello {name} ----- ")
#     return
#
# sayHello("Ahmed")


########################
# def sumnum(x, y):
#     res = x + y
#     return  res
#
# r = sumnum(10, 20)
# print(r)

#####################################

# def sumnum(x, y):
#     res = x + y
#     return  res
#
# r = sumnum(10, 20)
# print(r)
#
# r = sumnum("Hello", "world")
# print(r)
#
#
# r = sumnum("1", 10)
# print(r)

#########################3
#
# def sumnum(num1 :int, num2 :int):
#     res = num1 + num2
#     return  res
#
# r = sumnum(10, 20)
# print(r)
# #
# r = sumnum("Hello", "world")
# print(r)
# #
# #
# r = sumnum("1", 10)
# print(r)

#####################################
#
# def sumnum(num1 :int, num2 :int):  # just for hints 000
#     # print(isinstance(num1, int))
#     if isinstance(num1, int) and isinstance(num1, int):  # check the datatype of the object
#         res = num1 + num2
#         return  res
#     print("sumnum requires num1, num2 to be integer numbers ")
#     return
#
# r = sumnum(10, 20)
# print(r)
# #
# r = sumnum("Hello", "world")
# print(r)
#
#
#
# name = '12'
# print(name.isdigit())  # isdigit ---> function related to the string
#
#
# # var = '344$'
# # print(var.isnumeric())
#
# x = '3.4'
# print(x.isnumeric())
#
# print(x.isdecimal())

# ########################## function in python ---> default arguments

# def sumnum(num1 =1, num2 =2):
#     if isinstance(num1, int) and isinstance(num2, int):
#         print(f"num1 = {num1}, num2 = {num2}")
#         res = num1 + num2
#         return  res
#
#
# m = sumnum(10,20)
# n = sumnum()
# s = sumnum(10)
# mm = sumnum(num2=50)
# print("noha", end='$')
# print("---- itworx---")

################################ unknown number of arguments ######################333
# print("Ahmed", "ali", "Mohamed", sep="   #    ")
#
# def myfun(* args):
#     # print(args, type(args))  # args __tuple
#     for i in args:
#         print(i)
#
#
# myfun()
# myfun(4,5,6)
# myfun('4', [4,5,6], 'python', 'itworx')
#
#
###########

def introduceYourSelf(** kwargs):
    print(kwargs)

introduceYourSelf(name='Ahmed', track='python')

introduceYourSelf(firstname='shroq',lname='Hussien', city='Cairo')
# def introduceYourSelf(** info):
#     print(info)


introduceYourSelf(info={"name":"Ahmed", "lanme":'fahmy', 'age':22})




