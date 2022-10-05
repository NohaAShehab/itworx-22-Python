""" inheritance
    child ----> can see the parents' functions (methods) and the properties (variables)

"""


# class Parent:
#     pass
#
#
# class Child(Parent):
#     pass
#
#
# # is-a relationship
# obj = Child()
# print(type(obj))
# print(isinstance(obj, Parent))

###########################################################

# class Person:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Student(Person):
#     pass
#
#
# s = Student("Ahmed", "male")
# s.speak()
######################################################33


class Person:
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def speak(self):
        print(f"My name is {self.name}")
#
#
class Student(Person):
    def __init__(self, name, gender , email, grade ):
        # I need to call the parent constructor
        # super().__init__(name, gender)
        self.email = email
        self.grade= grade


s = Student("Ahmed", "male", 'ahmed@mail', 100)
print(isinstance(s, Person))
s.speak()
########################################
# class Person:
#     def __init__(self, name=None, gender=None):
#         self.name = name
#         self.gender = gender
#
#     def speak(self):
#         print(f"My name is {self.name}")
#
#
# class Student(Person):
#     def __init__(self,email, grade ):
#         # I need to call the parent constructor
#         # super().__init__()  # implicit ask the parent to fill student self with the instance variables
#         # super(Student, self).__init__()
#         Person.__init__(self)
#         self.email = email
#         self.grade= grade
#
#
# s = Student('ahmed@mail', 100)
# s.speak()


# ######################## multiple inheritance


# class Parent1:
#     pass
#
#
# class Parent2:
#     pass
#
#
# class Child(Parent1, Parent2):
#     pass
#
#
# c = Child()
# print(isinstance(c, Parent1))
# print(isinstance(c, Parent2))


###########################################################
# class Parent1:
#     # def __init__(self, fname):
#     #     self.fname = fname
#
#     pass
#
#
# class Parent2:
#     def __init__(self, lname):
#         self.lname = lname
#
#
# class Child(Parent1, Parent2):
#     pass
#
#
# c = Child("Ahmed")
# print(isinstance(c, Parent1))
# print(isinstance(c, Parent2))
