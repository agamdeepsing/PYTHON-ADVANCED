

# Ques 1
Greedy syntax in regular expressions matches as much as possible, while non-greedy 
syntax matches as little as possible.

to transform a greedy pattern into a non-greedy one, we can introduce a question mark ? 
after a quantifier or change the quantifier from greedy to non-greedy mode.


# Ques 2
in cases where you require a non-greedy match but the only available option is a greedy match, 
you can transform the pattern to a non-greedy one by adding the question mark after the quantifier. 
This modification allows you to achieve the desired behavior of matching the minimum necessary to satisfy 
the pattern.



# Ques 3
 a simple match scenario where we are not capturing any groups or utilizing the matched substring, the 
use of a non-tagged group would not have any practical significance. it all depends on coding styles 
rather than impact the functionality.


# Ques 4
it deals with text classification tasks,i.e sentiment analysis, improving the robustness and also 
enhances the generalization which helps in decison making.


# Ques 5
While counting the number of multiple lines or mutiple sentence in a string the positive look ahead 
makes a difference, without which we wont get the correct count of lines or sentences in a string.


# Ques 6
Positive Look-Ahead: Syntax (?=...)
foo(?=bar) matches "foo" only if it is followed by "bar"
                              
Negative Look-Ahead: Syntax ((?!...))
foo(?!bar) matches "foo" only if it is not followed by "bar"


# Ques 7
it helps to keep the code clear and easy to understand.


# Ques 8
import re
text = "The cow jumped over the moon"
regobj=re.compile(r'(?P<w1>The)',re.I)
regobj.findall(text)


# Ques 9
When parsing a string, one thing that the Scanner interface in Java provides, which the re.findall 
feature in Python does not, is the ability to tokenize the input by using custom delimiters or patterns.

re.findall() function in Python returns all non-overlapping matches of a pattern in a string.

# Ques 10
Yes, It may have any name