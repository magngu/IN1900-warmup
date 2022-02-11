# UiO // IN1900 - Introduction to Programming
Repository for all my [IN1900](https://www.uio.no/studier/emner/matnat/ifi/IN1900/index-eng.html)
excercise answers and related documents. Primarily notes of course contents for
reference and committing to memory.

![](https://img.shields.io/badge/python-numpy-blueviolet)
### Short overview of course
<details>
  <summary>Modules</summary>

  * math
  * cmath
  * numpy
  * sys

</details>

<details>
  <summary>Working with strings</summary>

  * F-string formatting
  * Format specifiers
  * print()

  ```python
  # f-string formatting
  print(f'Evaluate {variable} at runtime')

  # format specifieer
  print(f'Set space for output {x:8.2f}.')
  ```

</details>

<details>
  <summary>Working with files</summary>

  * close()
  * open()
  * write()
  * [.read()]()
  * [.readlines()]()

</details>

<details>
  <summary>Lists</summary>

  * Lists are mutable
  * List comprehension
  * List slicing
  * .append()
  * .split()
  * len()

  ```python
    # List comprehension
    # new_list = = [expression for element in iterable]
    my_list = [x**2 for x in range(10)]

  ```

</details>

<details>
  <summary>Loops</summary>

  * While-loop
  * For-loop
  * Mathematical sum as for-loop
  * len()
  * range()
  * zip()

</details>

<details>
  <summary>Exception handling</summary>

  * try-except-finally
  * raise

</details>




## Subjects, concepts and must knows

* Inline if-tests
* Lambda function
* Traversing nested lists
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
* [eval()]()
* [exec()]()
* [exit()]()
* [input()]()
* [write()]()
* [sys.argv[i]]()



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
