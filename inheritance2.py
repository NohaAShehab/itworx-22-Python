class Parent:
    def __init__(self,name):
        print("parent called")
        self.name =name
        self.email = ''

    def speak(self):
        print(f"my name is {self.name}")


# class Test(Parent):
#     def __init__(self, name='default'):
#         super().__init__(name)
#         print("child called")

class Test(Parent):
    def __init__(self, name='default'):
        self.name = name
        print("child called")


t = Test()
t.speak()