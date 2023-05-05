
# Ques 1
Metaclass in Python is a class of a class that defines how a class behaves. A class is itself a instance of Metaclass, and any Instance of Class in Python is an Instance of type metaclass. E.g. Type of of int, str, float, list, tuple.

# Ques 2
A way to declare a class metaclass is by using metaclass keyword in class definition.

# Ques 3
Anything you can do with a class decorator, you can do with a custom metaclass (just apply the functionality of the "decorator function", i.e., the one that takes a class object and modifies it, in the course of the metaclass's __new__ or __init__ that make the class object!).

# Ques 4
Anything you can do with a class decorator, you do with a custom metaclass (just apply the functionality of the "decorator function", i.e., the one that takes a class object and modifies it, in the course of the metaclass's __new__ or __init__ that make the class object!).