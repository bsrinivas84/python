from baseClass import ParentClass
from gradeClass import GradeClass
from abstractClass import AbstractClass
class child(ParentClass,GradeClass,AbstractClass):
    def __init__(self, name, grade):
        ParentClass.__init__(self, name)
        GradeClass.__init__(self, grade)
        AbstractClass.__init__(self)

    
    def greet_child(self):
        return f"Hello from the child class, my name is {super().greet()} from grade {super().get_grade()}"
    
    def greet_diff_lang(self):
        return f"Hola, my name is {super().greet()} from grade {super().get_grade()}"

if __name__ == "__main__":
    child_instance = child("Alice", "A+")
    print(child_instance.greet_child())
    print(child_instance.greet_diff_lang())