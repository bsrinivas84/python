def Testfunc(self):
    print("This is a test function.")

name="MyClass"
base = (object,)
func_dict = {"Testfunc": Testfunc}

myClass = type(name, base, func_dict)  # Create a new class dynamically

myobj = myClass()
myobj.Testfunc()  # Call the method from the dynamically created class