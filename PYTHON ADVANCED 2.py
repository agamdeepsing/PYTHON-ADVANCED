Q1. What is the relationship between classes and modules?
1. a python class is like blueprint for creating a new object.
whereas modules are files with .py extension consisting of a python code that can be used inside another program using import function.

Q2.How do you make instances and classes?
2. for making instance we call a class by its anme and pass the argument which init methods accept.
 whereas class are made using classs keyword

Q3.Where and how should be class attributes created?
3.class attributes belongs to the class itself. Hence these attributes are defined in the top of class definition outside all methods.


Q4.Where and how are instance attributes created?
4.instances methods are passed to the class when an object of class is created. instances are not shared by all objects of the class. instances are defined within __init__ method.


Q5.What does the term "self" in a Python class mean?
5.self represents the instanace of the class.By using the “self” keyword we can access the attributes and methods of the class within the class in python.


Q6.How does a Python class handle operator overloading?
6.Python Classes handle operator overloading by using special methods called Magic methods. these special methods usually begin and end with __ (double underscore).
/ -> __div__()
* -> __mul__()
+ -> __add__()
- -> __sub__()

Q7.When do you consider allowing operator overloading of your classes?
7.when we wanted to have the different meaning for the same operator.

Q8.What is the most popular form of operator overloading?
8.Magic methods.

Q9. What are the two most important concepts to grasp in order to comprehend Python OOP code?
9.classes and objects are the two important concepts. except these there are 4 more imp topics that you can grasp are
1.polymorphism
2.abstraction
3.encapsulations
4.inheritense