
# Ques 1
class is used for creating objects , on the other hand instances are specific
objects created from the class.

The relationship between a class and its instances is a one-to-many relationship.credits


class ineuron:
    def __init__(self, teacher, start_date, placement, quality):
        self.teacher = teacher
        self.start_date = start_date
        self.placement = placement
        self.quality = quality

a = ineuron("sudhanshu_sir",2022,"no","5star" )
b = ineuron("krishsir",2022,"applied","5 star")
c = ineuron("paulsir",2023,"no response","5 starrrrr")


# Ques 2
Instances hold data specific to the individual objects
created from a class. 
    
print(a.quality)
print(c.teacher)
print(b.placement)


# Ques 3
a class stores knowledge in form of atrributes and methods
and it can be categorized into two main types data and behaviour.


# Ques 4
method is a funciton which is associated with an object or class.
methods have access to instance data also have an self parameter to call the instance.

while regular expression are not associated with any object or class.


# Ques 5
yes inheritence is supported in python.

class ParentClass:
class ChildClass(ParentClass):
    pass


# Ques 6
In Python, encapsulation can be achieved using conventions and some language features, 
although it does not have strict access modifiers like some other programming languages 
(e.g., private, public, protected).

naming
double underscore
getter and setters


# Ques 7

class is used for creating objects , on the other hand instances are specific
objects created from the class.
    

# Ques 8
Yes, self can included in class method definations to access the instance variables
inside class methods.
    

# Ques 9
In summary, __add__ is used when the left operand is an instance of the class, while
__radd__ is used when the left operand is not an instance of the class but the 
right operand is. 

# Ques 10
Reflection methods, such as __getattr__ and __setattr__, are used in Python to provide 
customized behavior for attribute access and assignment. 
reflection method provide flexibility and dynamic behaivour.

# Ques 11
__iadd__ method is called when we use implementation like a+=b which is a.__iadd__(b).


# Ques 12
Yes, __init__ method will be inherited by subclasses. if we want to customize its behaviour
within a subclass we can use super() method.