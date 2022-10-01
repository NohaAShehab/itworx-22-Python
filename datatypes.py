"1- to get the datatype of variable "

# name = 'Ahmed'
# print(type(name))  # get the type of the object --->  <class 'str'> ---> object from class Type
#
# ##############################3
# num = 10 # int
# print(type(num))
# ##############################
# """ loosely dynamically lang. ---> change datatype of variable runtime"""
# "convert int to str"
# num = str(num)
# print("-----------------")
#
# """ Boolean variable"""
# b = True
# c = False
# b = int(b) #  1
# m = 100
# m = bool(m)
#
# """   conversion between types ---> from the same category ---(primitive to another primitive )"""
# age = '30'# ## numeric string
# age = int(age)

#
# message = 'hi'
# message = int(message)  # runtime error --->

#######################################################################################################
"""-------------------------------------- String ----------------------------------------"""
"""
    STRING ===> SEQUENCE OF CHARS (SYMBOLS)
    ---> "abcde"  #string  
    ## is treated like an array ---> 
    ----> access chars in the string using char index ? 
    index start from Zero 
    --> get the lenght of the string ---> 
"""


# "1- to define string "
#
# messsage = 'Nice to meet you all'
#
# "2- get the length of the string"
# print(len(messsage))
#
# "3- can access part of the string using index"
# print(messsage[2])
# print(messsage[-3])
# print(messsage[2:9])  # get substring from start index :: 2 to index  end-1
# "4- string is immutable datatype ---> once created cannot be changed"
#
# # messsage[3]='b'
#
#
# "5- examine the content in the string "
# "check if the content is digit"
# print(messsage.isdigit())   ### check if the string contains only numbers --> will return with True
#
# if messsage.isdigit():
#     messsage =  int(messsage)
#
#
# # isnumeric ---->
#
#
# if messsage.isalpha(): # check the string consists from only alphas ----> no spaces no numbers or special chars
#     print("--- valid user name ")
#
#
# name = 'Ahmed'
# print(name.isalpha())
#
#
# "ask the user to enter string"
#
# name = input("please enter name :  ")  # input function always return string
# print(name, type(name))
#
# """ isfloat ? ----> how to check if the string contains float value .... """
#
# if name.isspace():
#     print("---------- spaces are not allowed here ......")
#
#
# "CHeck the status of the string "
# name = 'NOHA'
# print(name.isupper())  # check if the string in upper cases or not .....
# print(name.islower())
#
#
# "6- string concatenation ---> is allowed only between strings "
# fname = 'Noha '
# midname ='AbdelHady '
# lname = 'Shehab'
#
# fullname = fname + midname + midname + lname
# print(fullname)
#
# "7- string interpolation"
#
# fullname = fname + midname*2 + lname
# print(fullname)


"8- string replacement"
# name = 'Ahmed   e e e e '
# # name[3]='E'
#
# # name = name.replace('e', 'E')  #replace all the occurrences
# # print(name)
# print(name.replace('e', 'E'))
# print(name)
#
# name = name.replace('e', 'E', 1)  # replace only the first occurrence
# print(name)

"9- string formatting"

# message = "My name is {0} , I works at {1}"
#
# print(message.format('noha', 'iti'))
# print(message.format('Ahmed', 'itworx'))
# print(message.format('Carol', 'itworx'))
# print(message.format('itworx', 'Mostafa'))

# message = "My name is {nn} , I works at {place}"
# print(message.format(place='iti', nn='Mostafa'))



#
# " 10 f- format string "
# """ format string using values from existing variables"""
# name = input("please enter your name: ")
# company = input("please enter your company .... : ")
#
# info = f" My name is {name}, I works at {company}"
# print(info)


# "11- count occurance of char in the string"
# message = 'i love iti'
# print(message.count('i'))
#
# "12 - get the index of char in the string"
# print(message.index('i')) # get the index of the first occurrence of the char.
#
# "13- captilize the string "
# print(message.capitalize())  # upper case the first char in the string

"14- strip string ===="

# message = '     I lives in Cairo .               '
#
# print(len(message))
# # remove spaces from the string
# m = message.strip()   # remove spaces from the beginning and the end if the string only
# print(m)
# print(len(m))


# ### strip can accept set of chars
# msg = ' $    My name is Ahmed $ @ #  '
# print(msg.strip("$ #"))



# # msg = ' $    My name is Ahmed $ @ #  '
# # print(msg.lstrip("$ #"))  # strip the string from the left only
#
# msg = ' $    My name is Ahmed $ @ #  '
# print(msg.rstrip("$ #"))  # strip the string from the left only
#





########################################################

# num = 20 + 50j
#
# print(num, type(num))
#
# mynum = complex(5,7)
# print(mynum)

#
# print(max(4,56,67,555))
# print(min(4,56,67,555))
#
# print(round(4.6))


# year = 2021
# year +=1 # assigment and increment operator


##############################################

print(100 and True)  #######3
"""

    1111111111111111111111111
                            1
    -------------------------
                            1
                            
                            

"""

print(True and 100) #############
"""
 1111111111111111111111111111111
                        11111110
                        -----------
                        11111110

"""
print(False and 100)
"""
    and expression ---> True  ---> something means True ? all parts of the expression are True or means True .
    
    100 and True  ----> True 
    
    True and 100 =====> means True ? 
    
    
    Values ---


"""

print("Ahmed" and 'iti')

print('ahmed' or 'iti')














