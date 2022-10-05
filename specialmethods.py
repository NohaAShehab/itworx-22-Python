# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
#
#     def __str__(self):  # user
#         # must return with string
#         return f"Car('{self.brand}', {self.year})"
#
#
#
# c =  Car("BMW", 2023)  # address
# print(c)
# print(c.__str__())

# l = [3,4,5,]
# print(l)

#
# class Car:
#     def __init__(self, brand, year):
#         self.brand = brand
#         self.year = year
#
#
#     def __str__(self):
#         return f"{self.brand}"
#
#     def __repr__(self):
#         # must return with string
#         return f"Car('{self.brand}', {self.year}) ---> repr"
#
#
#
# c =  Car("BMW", 2023)  # address
# print(c)
# print(c.__repr__())

###################################################################
# class Car:
#     call_counters = []
#     def __init__(self, brand):
#         self.brand = brand
#
#     def __call__(self):
#         print("---- object called -----")
#         # print object
#         # list what object can
#         # specialfunction
#         Car.call_counters.append(self)
#
# c = Car("KIA")
# print(c)
# c()


#################################
# l = [4,5,6]
# print(len(l))

class Car:
    call_counters = []
    def __init__(self, brand, year):
        self.brand = brand
        self.year = year
        self.country = 'Germany'


    def __len__(self):
        # must return with number
        return len(self.__dict__)

c= Car('Kia',2022)
c.expensive = True
print(len(c))







