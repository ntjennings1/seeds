# Python 

Incremental programming examples written in Python.

## About

Python is a high-level scripting language that was created by Guido Van Rossum in 1989. Since its release in 1991, Python has
become a general purpose tool tailored to Unix and C hackers. The scripting language emphasizes code readability through
significant indentation and hefty support of the structured, object-oriented, and functional programming paradigms. You can see
Python implemented in many STEM settings for Web Development, Data Science, Machine Learning (ML), Cybersecurity, the Internet
of Things (IoT), and general education.

The programs in this repository will use all supported paradigms to help users build on their programming abilities,
improve their attention to detail, increase their knowledge base, and refine their adaptability over time. In development, we
will study an Object-Oriented Programming approach and apply it to different disciplines such as Scientific Computing,
Data Visualization, Automation, and more!

## Software Requirements

The following open-source programming language and subsystems were used to develop the educational examples included in
this portion of the seeds:

```
    - Python 3.13.0
    - Pip 24.2.0
```

## Principles 

The examples included in this repository will systematically educate users on the following programming principles:

```
    - Program Structure
    - Documentation
    - Packages / Imports
    - Functions
    - Naming Conventions
    - Variables
    - Scoping
    - Looping
    - Conditions
    - Error Handling
    - Abstraction
    - Encapsulation
    - Inheritance
    - Execution
    - Input / Output
    - Parallelism 
```

## Data Types

This section will discuss different data types provided by Python. They were leveraged to create the examples and will be
necessary to progress further.

### Numeric Types
These are integers, floating points, or complex numbers. Each numeric type is accompanied by their own set of operations but are
used to represent some quantity. integers (int) are plain numbers without a decimal point whereas floating points (float) are plain
numbers with values after a decimal. Complex numbers (comlex) are imaginary numbers or numbers that contain the square root of
negative one.

Here are some examples:

Type | Value | Description
---|---|---
int | 1 | Plain number with no decimal point
float | 1.0 | Plain number with some value(s) after the decimal point
complex | 1j | Plain number and **j** representing $\sqrt{-1}$

### Boolean Type
These represent truth values and can only represent instances of **True** or **False**. The Boolean type **bool** can also behave
like numeric types where zero is False and any nonzero value is True. 

Here are some examples:

Type | Value | Description
---|---|---
bool | False | A characteristic between of two dissimilar variables
bool | True | The logical calculus of set membership 
bool | True | The complex number 1j or $\sqrt{-1}$
bool | False | The integer 0

### Sequence Types
These represent collections and consist of lists, tuples, dictionarys, ranges, etc. These variables are iterable, either changeable
or not, and have their own unique set of operations.

Here are some examples:

Type | Value | Description
---|---|---
list | [1, 2, 3] | A small list of ordered integers.
tuple | (4, 5, 6) | A small tuple of ordered integers.
dict | {'seven'=7, 'eight'=8, 'nine'=9} | A small dictionary of strings with their corresponding integer values.

### Text Sequence Type
These represent textual data, otherwise known as strings (str). Often accompanied by quotation marks, this data type is used in the
place of words or characters and supports its own set of operations.

Here are some examples:

Type | Value | Description
---|---|---
str | 'c' | A single character.
str | 'Hello World' | Two words.

## Operators

This section will discuss the different operators provided by this programming language. They are leveraged to create the examples
and will be necessary to progress further.

### Numeric Types
These can be used to manipulate or compare the values of int and float data, not complex data. They are associated with int, float,
or bool data types depending on the nature of the mathematical operation/comparison.

Here are some examples:

Operation | Result | Description
---|---|---
1 $+$ 1 | 2 | 1 $+$ 1 $=$ 2
1.0 $-$ 0.5 | 0.5 | 1.0 $-$ 0.5 $=$ 0.5
1 $*$ 2.5 | 2.5 | 1 $*$ 025 $=$ 2.5
2 $**$ 2.0| 4.0 | 2^2.0 $=$ 4.0
$\sqrt{-1}$ $/$ $\sqrt{-1}$ | 1 + 0j| $\sqrt{-1}$ $/$ $\sqrt{-1}$ $=$ 1 

### Boolean Type
These can be used to test truth value of statements. They are used within *if* or *while* conditions and typically define set
membership or a relationship between two variables. 

Here are some examples:

Var | Operation | Result | Description
---|---|---|---
c = 4 | if c is (5 or 6)  | False | Applies comparison of some variable, c, to other variables in a condition  
c = 'o' | if c in ('ok and 'no') | True | Applies existence of some variable, c, in other expressions to a condition 
c = True | if not c | True | Applies truth of some statement, c, to a condition 

### Sequence Types
These can be used to evaluate and manipulate the different sequence types. They are often used by themselves or in conjunction with
boolean operators. 

Here are some examples:

Var | Operation | Result | Description
---|---|---|---
c = [1, 2, 3]| if 2 is c  | True | Checks the contents of some list, c, for the existence of the number 2 
c = (1, 2, 3)| print(len(c))  | 3 | Outputs the length of some tuple, c
c = dict(one=1, two=2, two=2, three=3) | print(c['one'])  | 1 | Prints the value of the key 'one' in some dictionary, c 

### Text Sequence Type
These can be used to alter and characterize strings. Strings support many of the other operation types but also have methods unique
to themselves.


Here are some examples:

Var | Operation | Result | Description
---|---|---|---
c = 'Hello World' | "Hell" in c  | True | Checks the existence of 'Hell' in some string, c 
c = 'This "is" it.' | c.isalnum() | False | Determines if the string, c, consists of only alphanumeric symbols 
c = "Another" | c.isalpha() | True | Determines if the string, c, consists of only alphabetic symbols
c = "0,1,2,3" | print(c.split(",")) | ['0', '1', '2', '3'] | Prints a list of words in some string, c, seperated by the delimiter "," 

## Acknowledgements

A huge shoutout to these folks for contributing to the continued development of the examples in this repository:

```
Noah Jennings 
    TC 
    ntjennings1@gmail.com
    Virginia Beach, VA
    
TC 
    th3orycc@gmail.com
    Virginia Beach, VA
```

## Sources

Also, I would like to recognize external organizations and websites that contributed to the content in this repository:

1. [The Python homepage](https://www.python.org/)
2. [The Python GitHub](https://github.com/python)
3. [The Python Wikipedia](https://en.wikipedia.org/wiki/Python_(programming_language))
4. [Python Documentations](https://docs.python.org/3/)
5. [Python Module Documentations](https://docs.python.org/3/py-modindex.html)
5. [Python Tutorials (Geeks)](https://www.geeksforgeeks.org/python-programming-language-tutorial/)
6. [Python Tutorials (Real)](https://realpython.com/)
7. [Python Content](https://pythonprogramming.net/)