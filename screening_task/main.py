from abc import ABC, abstractmethod


def replace_original_str(file_path:str, original_str:str, replace_str:str) -> str:
    """
    file_path: path where file is located
    original_str: string contained in file
    replace_str: string used to replace original str
    """
    try:
        f = open(file_path, "r")
        contents = f.read()
        if original_str in contents:
            contents = contents.replace(original_str, replace_str)
            f.close()
            
            with open(file_path, "w") as f:
                f.write(contents)
            return "Matching string(s) replaced!"
        else:
            return "No matching strings found!"
    except FileNotFoundError as e:
        return e


# Uncomment the code below to run the program
# print("<------- Code to replace a string in a file ------>")
# print(replace_original_str("example.txt", "placement", "screening"))


"""Q2 i): Abstract class example"""
class Parent:
    """Abstract class to create child details"""
    
    @abstractmethod
    def father(self, name: str) -> None:
        pass
    
    @abstractmethod
    def mother(self, name: str) -> None:
        pass
    
    
class ChildInfo(Parent):
    """A class to provide info about a child"""
    
    def __init__(self, name):
        self.name = name
        
    def father(self, name: Parent) -> str:
        self.f_name = name
        
    def mother(self, name: Parent) -> str:
        self.m_name = name
        
    def child_info(self) -> str:
        return f"Your details are: \n\
                Name: {self.name} \n\
                Fathers' name: {self.f_name} \n\
                Mothers' name: {self.m_name} \n"
                
                
# Uncomment the code below to run the program
# print("<---------- Abstract class Example --------->")
# paul = ChildInfo("Paul Jackson")
# paul.father("Anthony Jackson")
# paul.mother("Mary Jackson")
# print(paul.child_info())


"""Q2 ii): Multiple inheritance example"""
class School:
    
    def __init__(self, sch_id):
        self.sch_id = sch_id
        

class ClassRoom:
    
    def __init__(self, class_id):
        self.class_id = class_id
        
    
class StudentInfo(School, ClassRoom):
    
    def __init__(self, sch_id: int, class_id: int, fname: str, lname: str):
        School.__init__(self, sch_id)
        ClassRoom.__init__(self, class_id)
        self.fname = fname
        self.lname = lname
        
    def student_details(self) -> str:
        return f"Your student details are: \n\
            Firstname: {self.fname} \n\
            Lastname: {self.lname} \n\
            School id: {self.sch_id} \n\
            Class id: {self.class_id}"
            
# Uncomment the code below to run the program
# print("<-------- Multiple Inheritance Example ----------->")
# std1 = StudentInfo(1234, 777, "Tony", "Stark")
# print(std1.student_details())


"""Q2 iii): Decorator Example"""

def div(a: int, b: int) -> int:
    return a/b

def bigger_numerator_as_dividend(func):
    
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)
    return inner


# Uncomment the code below to run the program
# print("<--------- Code to show decorators example ------->")
# new_div = bigger_numerator_as_dividend(div)
# print("Division result: "new_div(2,4))
