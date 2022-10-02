"""

    python file is called module

    any varaible defined in the python file  in the global scope can be accessed
    anywhere in the module

"""
# "1- read the value"
# course = 'python'  ### global variable
#
#
#
# def testfun():
#     print(f"from the testfun ... {course}")
#
#
# testfun()
# print(f"-----{course}-------------")
"""
    local scope 
     any variable defined inside a function is considered to have 'local scope '---> and this
     variable can be accessed only in the class 
"""
"1- modify the  global value"
# course = 'python'  ### global variable
# def testfun():
#     course = 'Django'  # any variable defined inside a function is considered to have 'local scope '
#     print(f"from the testfun ... {course}")
#
# testfun()
#
# print(f"-----{course}-------------")

################################################################
course = 'python'  ### global variable
def testfun():
    global course
    course = 'Django'  # any variable defined inside a function is considered to have 'local scope '
    print(f"from the testfun ... {course}")

testfun()

print(f"-----{course}-------------")

#################################### local scope #############################3


"""
    any variable defined in the function ---> scope localscope ---> variable can be accessed only 
    inside this function..
"""
#
# def testFunction():
#     name = "Aya"
#
#     print(name)
#
# testFunction()
# print(name)
######################################33 inner function

# def outerFun():
#     name = 'Ahmed'
#
#     def innerfun():
#         print(f'from inner function  name {name}')
#
#     innerfun()
#
#     print(f"from outerfunction name = {name}")
#
#
# outerFun()

#########################################################3

# def outerFun():
#     name = 'Ahmed'
#
#     def innerfun():
#         name = 'Shehab' # new local variable in the inner function scope
#         print(f'from inner function  name {name}')
#
#     innerfun()
#
#     print(f"from outerfunction name = {name}")
#
#
# outerFun()


####################################### modify the variable from the inner function


# def outerFun():
#     name = 'Ahmed'
#
#     def innerfun():
#         nonlocal name  # search about name in the upper functions scope
#         name = 'Shehab' # new local variable in the inner function scope
#         print(f'from inner function  name {name}')
#
#     innerfun()
#
#     print(f"from outerfunction name = {name}")


# outerFun()

#############################################3333

# def outerFun():
#     name = 'Ahmed'
#     course = "python"
#
#     def innerfun():
#         nonlocal name, course  # search about name in the upper functions scope
#         name = 'Shehab' # new local variable in the inner function scope
#         print(f'from inner function  name {name}')
#
#         def deepfun():
#             nonlocal  course
#             course = 'django'
#
#
#         deepfun()
#     innerfun()
#
#     print(f"from outerfunction name = {name}, {course}")
#
#
#
#
# m,n =24,5






for i in range(10):

    print(i)

print(f"--------------------- {i}")




name = input("please enter name ")
if name.isalpha():
    email = f'{name}@itworx.com'

print(email)



































