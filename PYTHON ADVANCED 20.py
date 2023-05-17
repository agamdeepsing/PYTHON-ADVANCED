
# Ques 1
Both the float and decimal types store numerical values in Python.

float benefits : convenience and speed, gives you approximate value you 
declare, efficiency, familarity
drawback: limited precision, not suitable for financial calculations.
    
decimal benefits  :  Accurate Decimal, Decimal Precision

drawback : Performance Overhead, Memory Usage, limitd range.


# Ques 2
Decimal('1.200') and Decimal('1.2') are different objects representing 
the same numerical value of 1.2. Both values are same but internal representation
at storage is differen


# Ques 3
both the values are equal but one difference is in precision.


# Ques 4
Starting with a string representation allows to control the precision and accuracy
of the Decimal object from the beginning, ensuring that obtain the desired results
in calculations and comparisons.


# Ques 5
We can do it with use of Decimal().


# Ques 6
No Decimal objects and floating-point values cannot be combined easily. it will give error.


# Ques 7
Value of 0.5 will be represented as ½.



# Ques 8
One example of a quantity that can be accurately expressed by the Decimal or Fraction classes 
but not by a floating-point value is 1/3.

from decimal import Decimal
from fractions import Fraction

decimal = Decimal('1') / Decimal('3')
fraction = Fraction(1, 3)
floating_point_value = 1 / 3

print(decimal)         
print(fraction)        
print(floating_point_value)  

by using deciaml and fraction classes we can get exact value of 1/3 without compromising loss of accuracy.

# Ques 9
Fraction(1, 2) and Fraction(5, 10) represent the same mathematical value of 1/2, the internal 
states of these Fraction objects differ initially. 


# Ques 10
Fraction class and the int type are separate and distinct types in Python, each with its own 
purpose and functionality for representing different kinds of numeric values.