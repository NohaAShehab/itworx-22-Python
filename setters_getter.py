# class Engineer:
#     def __init__(self,name, email, salary):
#         self.name= name
#         self._email = email
#         self.__salary =salary
#
#     def get_Salary(self):
#         if self.__salary:
#             return self.__salary
#
#     def set_Salary(self, value):
#         if isinstance(value, int) or isinstance(value, float):
#             self.__salary = value
#         else:
#             self.__salary= None
#
# e = Engineer("Ahmed", 'ahmed@gmail.com', 50000)
# print(e.get_Salary())
# e.set_Salary(1000)
#####################################################

class Engineer:
    def __init__(self,name, email, salary):
        self.name= name
        self._email = email
        self.salary =salary


    @property
    def salary(self):
        if self.__salary:
            return self.__salary

    @salary.setter
    def salary(self, value):
        if isinstance(value, int) or isinstance(value, float):
            self.__salary = value
        else:
            self.__salary= None

    @property
    def get_net_sal(self):
        if self.__salary:
            return self.__salary*.86

e = Engineer("Ahmed", 'ahmed@gmail.com', "iti")

# print(e.salary)
#
e.salary =1000
# print(e.get_net_sal)













