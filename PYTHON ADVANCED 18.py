
# Ques 1
both are common types of files format. text file store data as pllain text 
makeing them human readable and easy to understand. on the other hand binary 
files stores data which is not human readable. it consists of binary digits, 
represent information as image audio and video.


# Ques 2
text files are human readable  and can be edited easily, while binary files 
take plus point when we talk about performance, security and efficient storage of data.


# Ques 3
Using binary operations to read and write a Python integer directly to disk can lead to 
several issues i.e
porability
data integrity
readability
maintainance


# Ques 4
When a file is opened using the with keyword, if some exceptions occur after 
opening a file, or at the end of the file it automatically does the closing 
of the file. Then it does not leave the file in open mode and there would no need 
to explicitly close a file.



# Ques 5
Yes, Python have the trailing newline while reading a line of text. When we 
write a newline has to be provided in python excpicitly.


# Ques 6
The file operations enable for random-access operation are seek() and tell().


# Ques 7
The struct package is mostly used while converting a common python types 
into C language types.


# QUes 8
Pickling is best option for creating a new binary file using python.


# Ques 9
Shelve package is used to pickle data but treats the entire file as dictionary.


# Ques 10
if attempting to use a non-string key with shelve, you will encounter a TypeError 
indicating that the key must be a string.

special restriction is about the keys used in the data dictionary.
This restriction is due to the underlying implementation of shelve, 
which uses a database to store the data.