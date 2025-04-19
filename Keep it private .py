class MyClass:
    __privateVar=27;
    def __privMeth(self):
        print("I'm inside MyClas")
    def hello(self):
        print("private variable value :",MyClass.__privateVar)
foo = MyClass()
foo.hello()
foo.__privMeth