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
