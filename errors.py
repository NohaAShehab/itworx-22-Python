"""
    ------------------- Errors ------------------

    1- syntax error
        ----> must be fixed

    2- runtime error
            ----> exception ----> must be handled ---> application stop working


    3- logical error
        ---> must be fixed



"""
# print("---------------- syntax error  -----------------")
# x = 10
# print(x)


# "logical error "
#
# def sumnum(num1 , num2):
#     return num1 * num2
#
# r = sumnum(2,2)
# m = sumnum(4,5)


""" run time error """
# print("--------------- logical error ------------------------")
# print(course)





""" try =---> except """

# try:
#     print(course)
# except:
#     print("--------------- error happened ------------")
#
#
# print("-----------------------------------------------------")
# n = input("please enter number : ")
# print(n)


###################################### handle exception

#
#
# try:
#     print(course)
# except:
#     # handle exception
#     course = None
#     print("--------------- error happened ------------")
#
#
# print("-----------------------------------------------------")
# n = input("please enter number : ")
# print(course, n)

################################ exception type or message



# try:
#     print(course)
# except Exception as e :
#     # handle exception
#     course = None
#     print(f"--------------- error happened ------------ {e}")
#
#
# print("-----------------------------------------------------")
# n = input("please enter number : ")
# print(course, n)



#####################
# print(name)
# print(8/0)o exception

# m = int("m")


# try:
#     # print(course)
#     # print(8/0)
#     m =  int('r')
# except NameError as ne:
#     print(ne)
#     course = None
# except ZeroDivisionError as ze:
#     print(ze)
# except ValueError as ve:
#     print(ve)
# except Exception as e:
#     print(e)
############################################################
# student = "Hossam"
# try:
#     print(student)
#     print(8/0)
# except Exception as e:
#     print(e)
#     print("---------------- the program will close shortly, please restart it ")
#     student = None
#     # exit(1)
# else:
#     print("----------------Nice to meet you -------------")
#     ## this block will be executed when there is n
#
#
# print("----------- Hello World ---------------------")
# print(student)

"""
    try:
        pass
    except:
        pass
        
    else:
        # this block will be executed ---> when there is no exception 
        pass
        
    finally:
        # this block will be executed ---> if there is an exception or not 

"""





try:
    x = 8/0
except Exception as e :
    print(e)
    x = None
else:
    print(x)

finally:

    print("----- all is well -------------------")







