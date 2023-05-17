
# Ques 1
Yes, it is permissible to use several import statements to import the same module. It is used in case when we have to import multiple functions from same module.
import module and using clear naming conventions or aliases can help maintain code clarity and reduce confusion.

# Ques 2
__name__
__file__
__dict__


# ques 3
Circular importing means importing the two modules in each other.

lets say we are doing some work in xyz.py and it import some function from other yyz.py file , it gonna give import error.

To avoid this error just do one thing we can use if __name__ == '__main__'

In the function, you can't directly refer to the function in the program. The addition of this sentence avoids the endless loop of the program .



# Ques 4
it provides list of alll modules present in library.


# Ques 5
if we want to refer module in which we start working on then we uses name attribute.

The current module in which we are working is refer to the string __main __. main provides a way to control the execution of the code.
if __name__ == "__main__":
    print("This script is being run directly.")

# Ques 6
program control and flow
error handling and debugging
looping and interation
Script Analysis and Optimization

attaching a program counter to an RPN interpreter application provides control over 
program execution, aids in error handling and debugging, facilitates looping and iteration, and supports script analysis and optimization. it increases the capabilities of the interpreter.


# Ques 7
to create basic programmming language like rpn  that is, capable of carrying out any
computerised task theoretically possible, we need a need a set of minimum expressions
or statements that provide the necessary building blocks for computation.

language should include:
stack operation
arithmetic operations
conditional statements
looping
varaible assignment
input and output operations



