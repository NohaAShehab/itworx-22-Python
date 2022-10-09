""" os module """

# import  os
#
#
# print(os.getcwd())
#
# # os.system("mkdir itworx2022")
# os.system('ls -l')
#
# print(os.getlogin())
#
# # os.chdir('/home/noha')
# print(os.getcwd())
#
# os.chdir('$HOME')
#
# print(os.getcwd())

####################################

# import math
# print(math.pi)
#
# # print(math.sin(.25))
# print(math.pow(3,4))


##############################
import re  # regular expression
""" 
    fullmatch ===> check if the all the string matches the expression 
"""
# "noha@it-worx.com"
# pattern = r'\w+@[a-zA-Z_\-]+?\.[a-zA-Z]{2,3}$'
# email = input("please enter your eamil : ")
# if re.fullmatch(pattern, email):
#     print("correct email")
# else:
#     print("--- invaid email")

"noha@it-worx.com"
""" 
    check if part of the string matches the expression 
"""
# pattern = r'\w+@[a-zA-Z_\-]+?\.[a-zA-Z]{2,3}$'
pattern =  r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
email = input("please enter your eamil : ")
# if re.match(pattern, email):
#     print("correct email")
# else:
#     print("--- invaid email")


m= re.search(pattern, email)  # scan the string- --> get the part that matches
# the pattern
print(m)







