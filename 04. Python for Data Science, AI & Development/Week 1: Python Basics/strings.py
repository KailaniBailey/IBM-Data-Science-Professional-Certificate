# Quotation marks for defining string
"Michael Jackson"
# Can use single quotes
'Michael Jackson'

# Combination of spaces and strings
'1, 2, 3, 4, 5 "

# Combination of special characters
"!@#$%^& *()_+"

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

