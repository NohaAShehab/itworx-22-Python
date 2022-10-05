# class Parent1:
#     # def __init__(self, fname):
#     #     self.fname = fname
#
#     pass


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
#################################################3

class Parent2:
    def __init__(self, lname):
        self.lname = lname


class Parent1:
    def __init__(self, fname):
        self.fname = fname

    pass


class Child(Parent1, Parent2):
    def __init__(self, email):
        super(Child, self).__init__("test")
        Parent2.__init__(self, "my last name")
        self.email = email


c = Child("Ahmed")
