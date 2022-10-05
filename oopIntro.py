# #
# l = [4, 5, 6]  # object from list
# print(type(l))


# l.append('test')

# employee = {
#     "name":"Ahmed",
#     "address":"Cairo"
# }
#
# emp = {
#     "fname":"Ahmed",
#     "city": "October"
# }

# classes ----> add functionality to these classes

# class Employee:
#     pass
#
#
# e = Employee()
# print(type(e))
###############################################################3

# class Employee:
#     pass
#
#
# e = Employee()
# e.name = 'Ahmed'
# e.email = 'Ahmed@gmail.com'
#
# e2 = Employee()
# e2.firstname = 'Noha'
#################################
# class Employee:
#     def __init__(self):
#         print('----- object created -------')
#         print(self)
#
#
# e = Employee()
# print(e)
# print('##########################################')
# # e.name = 'Ahmed'
# # e.email = 'Ahmed@gmail.com'
#
# e2 = Employee()
# # e2.firstname = 'Noha'
#
#
########################################
# class Employee:
#     def __init__(self):
#         self.name = 'Ahmed'
#         self.email = 'ahmed@gmail.com'
#
#
# e = Employee()
# print(e)
# print('##########################################')
#
#
# e2 = Employee()
# # e2.firstname = 'Noha'

#########################################################
# class Employee:
#     def __init__(self, name, email):
#         self.name = name
#         self.email = email
#
#
# e = Employee('Ahmed', 'ahmed@gmail.com')
# print(e)
# print('##########################################')
#
#
# e2 = Employee('noha', 'noha@gmail.com')
# # e2.firstname = 'Noha'

#########################################

# class Employee:
#     def __init__(self, name='', email=''):
#         self.name = name  # instance variables
#         self.email = email
#
#
# e = Employee('Ahmed', 'ahmed@gmail.com')
# print(e)
# print(e.__dict__)
# print('##########################################')
#
#
# e2 = Employee('noha', 'noha@gmail.com')
# # e2.firstname = 'Noha'
# #######################################
# class Employee:
#     # __slots__ = ["name", 'email', 'age']
#     def __init__(self, name='', email=''): # arguments
#         self.name = name  #instance variables
#         self.email = email
#         self.age = None
#
#
# e = Employee('Ahmed')
# e.salary = 2222
# object_dict  = e.__dict__  # reprsent the object in a dictionary
# print(object_dict)
# if 'salary' in object_dict:
#     print('found ')
#
# if 'salary' in object_dict.values():
#     print('---found------')
# else:
#     print("-----not found -----")
# e.age = 22
#
# e2 = Employee('noha', 'noha@gmail.com')
# # e2.firstname = 'Noha'
# print(e2.age)
# print("--------------------------")
#
# e3 = Employee()
###############################################3

#
# class Employee:
#     def __init__(self, name='', email=''): # arguments
#         self.name = name  #instance variables
#         self.email = email
#         self.age = None
#
#
#     def sayHello(self, message =''):  # self object from employee
#         print(f"Hello , I am {self.name} {message}")
#
#
#
# emp =  Employee('test', 'abc')
#
# emp.sayHello("Nice to meet you")
# Employee.sayHello(emp)


###################################

#
# class Employee:
#
#     nationality = 'Egyptian'  # class variables
#     def __init__(self, name='', email=''): # arguments
#         self.name = name
#         self.email = email
#
#
#     def sayHello(self, message =''):
#         print(f"Hello , I am {self.name} {message}")
#
#
# emp =  Employee('Mostafa', 'mostafa@gmail.com')
# emp2 = Employee('Shrouk', 'Shrouk@gmail.com')

#####################################################


# class Employee:
#     # ############### class
#     nationality = 'Egyptian'  # class variables
#     no_of_employees = 0
#     # ######################## __init__ ===> this is the constructor ---> is called while creating
#     # the object
#     def __init__(self, name='', email=''):  # arguments
#         self.name = name
#         self.email = email
#         Employee.no_of_employees += 1
#
#     # instance method, # self ---> represnet the instance
#     def sayHello(self, message=''):
#         print(f"Hello , I am {self.name} {message}")
#
#     # # class method
#     @classmethod
#     def get_no_of_employees(cls):  # the first function parameter represent the class
#         print(cls)  # represent the Employee
#         print(cls.no_of_employees)
#
#     @classmethod
#     def createEmployee(cls):
#         return  cls("Ahmed", 'Ahmed@gmail.com')
#
# e = Employee("Ahmed", 'Ahmed@gmail.com')
# Employee.get_no_of_employees()
# print(Employee.no_of_employees)
#
# e3 = Employee.createEmployee()

##############################################################

# class Complex_:
#
#     def __init__(self, real=0, img=0):
#         self.real = real
#         self.img = img
#
#     @classmethod
#     def add_complex(cls, c1, c2):  # cls ==== Complex_ ---> cls ---> represent the class you are in
#         if isinstance(c1, cls) and isinstance(c2, cls):
#             newreal = c1.real + c2.real  # local variable in the add_complex
#             newimg = c1.img + c2.img
#             return cls(newreal,newimg)
#             # return (c1.real+c2.real, c1.img+c2.img)
#
#
# " c1 +  c2  --->  c3 ((return instance from this class))"
#
# c1 = Complex_(4,5)

# ################################### static methods ##############################
class Employee:
    def __init__(self, name, salary):
        print(self)
        self.name = name
        self.salary = salary

    def abc(self):
        print(self.name)
        print(self)

    @staticmethod
    def calNetSal(salary):
        return salary * .86


e = Employee('Mostafa', 20000)
print(Employee.calNetSal(10000))
print(Employee.calNetSal(e.salary))
print(e.calNetSal(e.salary))
e.abc()