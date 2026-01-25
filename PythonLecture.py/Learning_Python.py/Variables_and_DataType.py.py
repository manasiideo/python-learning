# Python -> Translator (compiler/Interpreter) -> Machine Language (0,1)
# 1 = high voltage
# 0 = low volateg
# Programming Language -> PYTHON (High Level Language)
# High Level Language -> Translator(works as) - > Low Level Language
# PYTHON -> Interpreter (NOT - compiler)
# PYTHON = simple Programming Language
#         free and open source
#         High Level Language
#         Developed by - GUIDO van Rossum
#         Portable Language - can be same in different operating system (windows, mac, linus, etc)
# Visual Studio Code -> Digital Notebook Code Editor
print("Hello WOrld") #FirstProgram 
#Always use "print" and not "Print"
# "print" = python's function
# INPUT -> CODE -> OUTPUT
# Python Chatacters:
#   1: A to Z and a to z
#   2: Deigits: 0-9
#   3: Symbols: -, +, *, / (keyboard keys)
#   4: WhiteSpaces: 
#                  i: Blank WhiteSpaces
#                 ii: Tab
#                iii: Carriage return
#                 iv: Newline 
#                  v: Formfeed
#   5: Python can process all "ASCII" and "Unicode characters" as part of data or literals
print ("Hey Manasi")
print ("Hey, I am Manasi Deo." "I am starting to learn Python." "And, I am learning from ApnaCollege's Tutorial, by Sraddha Khappra.")
print (43)
print (33+11)
print (33-11)
print (33*11)
print (33/11)
print ("33+11", "33-11", "33*11", "33/11")
print (33+11, 33-11, 33*11, 33/11)
Value1 = 43
print (Value1)
Value2 = 33+11
print (Value2)
Value3 = 33-11
print (Value3)
Value4 = 33*11
print (Value4)
Value5 = 33/11
print (Value5)
print ("Value2", "Value3", "Value4", "Value5") # any thing under "" is a string type
print (Value2, Value3, Value4, Value5)
# # VARIABLES: A variable is a name given to a memory location in a program.
# Column A: Variables Column B Values
name = "Manasi"
age = "23"
height = 170.688
print ("name")
print (name)
print (age)
print (height)
print (name, age, height)
print ("My name is :", name)
#Assignment Operators
age = 23
age2 = age #what is the logoc?????
print(age2)
# RULES FOR IDENTIFIERS
# 1. Combination of uppercase (A-Z), lowercase (a-z), digits (0-9) or an underscore (_).
#       example: 1. Identifiers 2. identifiers 3. Identifiers1 4. Identifiers_1 5. IDENTIFIRES
# 2. cannot start with a digit
#       example: 123names - INCORRECT names123 - CORRECT
# 3. cannot use symbols -> !, @, #, $, %, ^, etc
# 4. NO FIXED LENGHT: AaSsDdFfGgHhJjKkLlBbNnMmVv_012345679 - is acceptable (but not standard)
# VARIABLE NAMES: SIMPLE, SHORT, MEANINGFUL
# Data Type
#       1. INTERGERS: +ve, -ve, 0 (whole number)
#       2. STRINGS: "Hello", 'Hello', """Hello"""
#       3. FLOAT: Decimals (0.23, 1.345, 2.6789)
#       4. BOOLEAN: True & False (T of True and F of False will always be in uppercase)
#       5. NONE: a =  none (no value)
# We can use "" or '' or """""" in PYTHON
print('Hello')
print ("Hello")
print ("""Hello""")
print (type(name))
print (type(age))
print (type(height))
Morning = True
Night = False
Day = None
print (type(Morning))
print (type(Night))
print (type(Day))
# KEYWORDS: Keywords are reserved words in PYTHON.
# Keywords in Python: True, False, None, and, else, in, return, as, except, is, assert, finally, lambda, with, class, for, while, continue, from, not, yield, def, global, or, del, if, pass, elif, import, raise
# KEYWORDS can't be used as VARIABLES.
# PYTHON is CASE SENSITIVE: Apple/apple/APPLE all are different.
# PRINT SUM
a = 15
b = 10
sum1 = a + b
sum2 = a - b
sum3 = a * b
sum4 = a / b
print(sum1)
print(type(sum1))
print(sum2)
print(type(sum2))
print(sum3)
print(type(sum3))
print(sum4)
print(type(sum4))
#whenever DIVISION is performed in PYTHON the final OUTCOME has always a FLOATING value. 
#COMMENTS in python never gets executed in the CODE.
# To make a code as comment -> select the code -> press ctrl +/ (forward slash)
#                                                      it can UNCOMMENT as well.
# OPERATORS: In Python, operators are special symbols used to perform operations on values and variables (operands). They are grouped into categories such as arithmetic, assignment, comparison, logical, identity, membership, and bitwise operators.
# OPERANDS <- a + b -> OPERANDS (+ OPERATORS)
# Types of Operators in Python
# 1: Arithmetic operators: Used for basic mathematical operations:
#       + → Addition (5 + 2 = 7)
#       - → Subtraction (5 - 2 = 3)
#       * → Multiplication (5 * 2 = 10)
#       / → Division (5 / 2 = 2.5)
#       // → Floor Division (5 // 2 = 2)
#       % → Modulus (5 % 2 = 1)
#       ** → Exponentiation (5 ** 2 = 25)
# 2. Assignment Operators: Used to assign values to variables:
#       = → Simple assignment (x = 5)
#       += → Add and assign (x += 3 → x = x + 3)
#       -= → Subtract and assign
#       *= → Multiply and assign
#       /= → Divide and assign
#       //= → Floor divide and assign
#       %= → Modulus and assign
#       **= → Exponent and assign
# 3: Relational/Comparison Operators: Used to compare values:
#      == → Equal to
#      != → Not equal to
#      > → Greater than
#      < → Less than
#      >= → Greater than or equal to
#      <= → Less than or equal to
# 4: Logical Operators: Used to combine conditional statements:
#      and → Returns True if both conditions are true
#      or → Returns True if at least one condition is true
#      not → Returns True if the condition is false
# 5: Identity Operators: Used to compare object identities:
#      is → True if both variables point to the same object
#      is not → True if they do not
# 6: Membership Operators: Used to test membership in sequences:
#      in → True if value is found in sequence
#      not in → True if value is not found
# 7: Bitwise Operators: Operate on binary representations:
#      & → Bitwise AND
#      | → Bitwise OR
#      ^ → Bitwise XOR
#      ~ → Bitwise NOT
#     << → Left shift
#     >> → Right shift
x = 10
y = 3
print(x + y)    # Arithmetic → 13
print(x > y)    # Comparison → True
print(x and y)  # Logical → 3 (since both are non-zero)
print(x is y)   # Identity → False
print(5 in [1,2,3,5])  # Membership → True
print(x & y)    # Bitwise → 2 (binary AND)
# NOTE -> In python, the MODULE OPERATOR (%) calculates the REMAIDER of a division operation.
# It works with both POSITIVE & NEGATIVE integres, as well as floating-point numbers.
# print (a % b) = remainder
print (a % b)
# NOTE -> The Double Asterisk (**) in python has two primary uses:
# 1: Exponentiation (raising a number to a power): the exponentiation operator for mathematical calculations raises the left operand to the power of the right operand "base ** exponent". e.g., a**b = (a) to the power (b)
# example1: Exponentiation with Simple Numbers:
# 2 to the power of 3 = (2*2*2)
result = 2**3 # 2 raised to the power of 3
print (result) # Output: 8
# example2: Exponentiation with Complex Numbers:
complex_number = (2 + 3j) ** 2
print(complex_number)  # Output: (-5+12j)
# example: Exponentiation with Complex Numbers: The ** operator in Python is right-associative. This means if you have multiple exponentiation operations in a row, Python evaluates them from right to left.
result = 2 ** 3 ** 2
print(result)  # Output: 512
# 2: Unpacking keyword arguments into functions: WILL BE DISCUSSED LATER
