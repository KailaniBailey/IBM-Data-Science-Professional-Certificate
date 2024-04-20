# IBM SKILLS NETWORK LAB
# This is not the official document with the Skills Network Logo
# These are my notes from the lab

# Trying first python output for Course 4
print('Hello, Python!')

# Check the python version
import sys
print(sys.version)

# Practice writing comments
print('Hello, Python!') # This prints a string

# print('Hi')... this line of code has been 'commented out'

# Prints string as error message due to the typo
frint('Hello, Python!')

# Prints syntax error due to open string... interpreted language: python interprets script line by line as it's executed.
# Python will stop executing entire program when it encounters an error... script following the error will not get printed.
print('Hello, Python!)

# Integer (integers can be negative or positive, includes zero)
11

# Float (decimal points, aka real numbers)
2.14
# System settings about float type
sys.float_info

# String
"Hello, Python 101"

# Type of 12 is integer
type(12)

# Type of 2.14 is float
type(2.14)

# Type of "Hello, Python 101!" is string
type('Hello, Python 101!')

# Typecasting: changing from one type to another
float(2) # Converting integers to floats
# Result is 2.0

# Converting 2 to a float then checking it's type
type(float(2)) # Type will be a float

# Changing 1.1 to an integer will lose the additional information of .1
int(1.1) # Result will be 1 (with the lost information of .1)

# Convert string into an integer
int('1') # Result is 1

# Convert string '1.2' into a float
float('1.2') # Result is 1.2

# Strings can be represented using single quotes or double quotes but not both at the same time

# Convert integer into a string
str(1) # Result is '1'

# Convert float into a string
str(1.2) # Result is '1.2'

# A BOOLEAN (BOOL) type can be either True or False
type(True) # Result is BOOL or Boolean
type(False) # Result is BOOL or Boolean

# Convert True to an integer
int(True) # Result is 1
# Convert False to an integer
int(False) # Result is 0

bool(1) # Result is True
bool(0) # Result is False
float(True) # Result is 1.0

type(6/2) # Result is float (one slash); 3.0
type(6//2) # Result is integer (double slash); 3

# Addition operation expression
43 + 60 + 16 + 41 # Result is 160

# Subtraction operation expression
50 - 60 # Result is a negative number; -10

# Multiplication operation expression
5 * 5 # Result is 25

# Division operation expression with forward slash
25 / 5 # Result is 5.0

# Division operation expression with double forward slash (rounds the integer down)
25 // 5 # Result is 5

# Mathematical expression where Python follows traditional processes in mathematics
30 + 2 * 60 # Python will perform the multiplication first as in PEMDAS; 150
(30 + 2) * 60 # Parenthesis are eliminated first as in PEMDAS; Result is 1920

# Store value into a variable 
x = 43 + 60 + 16 + 41
x # Placing x on the last line will print the value for x; Result is 160

# Can overwrite the value of a variable with a new value
y = x / 60
y
x = x / 60
x

# DONE!!!
