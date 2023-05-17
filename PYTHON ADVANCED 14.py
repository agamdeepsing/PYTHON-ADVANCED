
# Ques 1
b+=1 is used to find b adding 1 to it and then storing the value again to b. as a memory address += leads to faster operation.


# Ques 2
Minimum number of lines required to write above code in languages other Python will be 4, two for assigning initial values for variables a and b, and two for reassigning(a=a+b and b=a).


# Ques 3
The Most effective way to set a list of 100 integers to 0 in python is by using repetition operator(*) or by using list comprehension.


# Ques 4
list = [1,2,3]*33
print(list)


# Ques 5
# 2 dimensional List
list = [[1,1],[2,2],[3,3],[4,4],[5,5]] 
for i in range(len(list)):
    for j in range(len(list[i])):
        print(list[i][j],end=" ")


# Ques 6
List comprehension with string is possible.
list = [i for i in 'iNeuron']
print(list)


# Ques 7
Get support with a user-written Python Programme: Start a command prompt (Windows) or terminal window (Linux/Mac). If the current working directory is the same as the location in which you saved the file, simply specify the filename as a command-line argument to the Python interpreter.

Get support with a User-written Python Program from IDLE: You can also create script files and run them in IDLE. From the Shell window menu, select File → New File. Type in the code to be executed. From the menu in that window, select File → Save or File → Save As… and save the file to disk. Then select Run → Run Module. The output should appear back in the interpreter


# Ques 8
You can store them in data structures such as hash tables, lists
You can return the function from a function.
You can pass the function as a parameter to another function.
You can store the function in a variable.
A function is an instance of the Object type.


# Ques 9
all the three terms are often describe as different concepts related to adding functionality or modifying existing function.

wrapper is used to translate between interfaces.

decorator is a language-specific construct used to transparently modify the behavior of functions or methods.

# Ques 10

generator functions returns a lazy iterator. lazy iterators doo not store their contents in memory.


# Ques 11
Generator is a written as normal function but uses yield keyword to return values instead of return keyword.


# Ques 12

return statement sends a specified value back to its caller whereas yield statement can produce a sequence of values. 

we must use generators if we wnat ot iterate over the sequence, but dont want to store entire memory. it takes less time to gives the output of the program, while return function first store the output in the list form in the memory and then show us the result.