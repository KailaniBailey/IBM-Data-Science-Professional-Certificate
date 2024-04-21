# Quotation marks for defining string
"Michael Jackson"
# Can use single quotes
'Michael Jackson'

# Combination of spaces and strings
'1, 2, 3, 4, 5 "

# Combination of special characters
"!@$%^& *()_+"

# Using a print statement
print('Hello!')

# Assign string to a variable
name = "Michael Jackson"
name

# Indexing starts at 0; the first index is located at 0
# Print first element in the string
print(name[0])
# Result is M

# Access index 6
print(name[6])
# Result is l

# Access index 13
print(name[13])
# Result is o

# Negative indexing starts at -1, not 0
print(name[-1])
# Result is n

# Obtain first element by using index -15
print(name[-15])
# Result is M

# Can find the number of characters in a string by using 'len'
len("Michael Jackson")
# Result is 15

# Can obtain multiple characters in a string by SLICING; FIRST NUMBER is start point, SECOND NUMBER is one index before the given point; 
# Using slice on the variable 'name' with only index  0 to 3
name[0:4]
# Result is "Mich"
name[8:11]
# Result is "Jack"

# Can skip every other index by using STRIDE; For example 2 selects every 2 instances
name[::2]
# Result is "McalJcsn"

# Can incorporate SLICING with the STRIDE
# Get every 2nd element in the range from index 0 to index 4
name[0:5:2]
# Eligible indexes from 0 to 4 are "Micha", then every 2nd is "Mca"
# Result is "Mca"

# CONCATENATE (combine, add using + symbol) 2 strings together, Result is a new string of both
statement = name + "is the best"
statement
# Result is "Michael Jacksonis the best"

# REPLICATE values of a string by multiplying by a number, Result is the number of times the string was being multipled by
# Print string for 3 times
3 * "Michael Jackson"
# Result is "Michael JacksonMichael JacksonMichael Jackson"

# Can create a new string by setting it to the original variable, CONCATENATED (+) with a new string
# Concatenate strings
name = "Michael Jackson"
name = name + " is the best"
name
# Result is "Michael Jackson is the best"

# ESCAPE sequences are represented by back slashes; Represent strings that may be difficult to input; 'back slash n' represents a new line
print("Michael Jackson \n is the best")
# Result will print on two separate lines

# TAB ESCAPE sequence is represented by a 'black slash t' that includes a new tab
print("Michael Jackson \t is the best")
# Result will print a tab within the string, between "Michael Jackson" and "is the best"

# Include a double back slash (\\) in a string to include a back slash within the string
print("Michael Jackson \\ is the best")
# Result will print Michael Jackson \ is the best

# r before a string tells python that string will print as a raw string
print(r"Michael Jackson \ is the best")
# Result will print Michael Jackson \ is the best

# STRING MANIPULATION OPERATIONS
# UPPER converts elements in a string from lowercase to uppercase
a = "Thriller is the sixth studio album"
print("before upper:", a)
b = a.upper()
print("After upper:", b)
# First line result is Thriller is the sixth studio album
# Second line result is THRILLER IS THE SIXTH STUDIO ALBUM

# LOWER converts elements in a string from uppercase to lowercase
f2 = "YOU ARE RIGHT"
f2.lower()
# Result will print "you are right"

# REPLACE replaces a part of the string; include the part of the string you'd like to replace, also include the new string that you'd like to replace the string with
# Replace the old 'substring' with the new 'target substring'
a = "Michael Jackson is the best"
b = a.replace("Michael", "Janet")
b
# Result will print '"Janet Jackson is the best"

# FIND is a method that will find a substring; the argument is the substring you want to find; the output is the first input of the sequence
# Find the substring in the string
name = "Michael Jackson"
name.find(el)
# Result will print 5; 'el' would be '5,6' but only the first element will print as an output, so the output is 5

# If python cannot find the substring in the string; if it isn't found in the string; Result will print output as negative 1 (-1)
name.find("alskdfjaweoifj")
# Result is -1

# SPLIT cuts the string at the designated separator and returns a list
# Split substring into a list
name = "Michael Jackson"
split_string = (name.split())
split_string
# Result is ["Michael", "Jackson"]

# REGEX (RegEx), short for Regular Expression, is a tool for matching and handling strings
# Provides several functions for SEARCH, SPLIT, FINDALL, and SUB
import re 
# imports the python module for the RegEx tool
re.search() # Function that searches for specific info within a string

# DONE!!!
