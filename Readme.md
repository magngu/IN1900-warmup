# UiO // IN1900 - Introduction to Programming
Repository for all my [IN1900](https://www.uio.no/studier/emner/matnat/ifi/IN1900/index-eng.html) 
excercise answers and related documents. Readme is primarily notes of course contents for 
reference and commiting to memory. 

## Subjects, concepts and must knows

* Write mathematical sum as for-loop
* List comprehension
* Inline if-tests
* Lambda function
* Traversing nested lists
* List slicing
* Difference between functions and methods
* Doc-string vs comment
* Positional keywords arguments
* Local vs global namespace and variables
* Default arguments
* Writing test functions & pytest
* Reading data from files
* Writing data to files
* Exception handling & try-except blocks
* How to make and import modules

## Functions, Methods and expressions
* [.append()]() 
* [eval()]() 
* [exec()]()
* [exit()]()
* [input()]() 
* [len()]()
* [open()]()
* [.read()]()
* [.readlines()]()
* [close()]()
* [print()]()
* [range()]()
* [.split()]()
* [write()]()
* [zip()]()
* [sys.argv[i]]()

## Tips & Tricks
* Always compare floats by using a tolerance value. Typical machine precision is 10^-16
* Two questions for writing for-loop:
   1. What should the iterable contain?
   2. What operations should be performed on the iterable?
* A for loop can always be transformed to a while-loop, but not vice versa





## UNSORTED
```python
int     # Integers  
float   # Floating point numbers
str     # String
list    # List
dict    # Dictionary [Hash table]
bool    # Boolean
tuple   # Tuple [Immutable list]



# KEYWORDS
assert
global
for
while
with
return
yield
if
elif
else
tryexcept
finally
raise

# MODULES
import math
import cmath
import sys
import numpy
import matplotlib.pyplot

#Other
ValueError
IndexError
raise ExceptionType(message)

```



```python
# General syntax for list comprehension
new_list = [expression for element in iterable]
````


##### String formatting
```python
# f-string formatting
print(f'Evaluate {variable} at runtime')

# format specifieer
print(f'Set space for output {x:8.2f}.')
```





