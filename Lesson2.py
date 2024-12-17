from operator import truediv

# evaluate values
print(bool("hi"))
print(bool(15))

bool("abc")
bool(123)
bool(["apple", "ornge"])

bool(False)
bool(None)
bool(9)
bool("")
bool(())
bool([])

def myfunction():
    return True
if myfunction():
    print("yes")

else:
    print("no")

x = 100
print(isinstance(x, int))

b = str(x) # b

type(b)

# operators
# + addition
# - subtraction
# * multiplication
# / division
# + = x + 3 x = x + 3


x = 5
x += 5
print(x)


x =+ 3
x

x = 100
x -= 3

x = 100
x *= 3
print(x)



# ==equal x==y
# is not equal x!= y
# >= less then or equal to z >= y
# <= less then or equal to z <= y

x = 3
y = 3
print(x != y)

# and operator
print(x < 4 and x < 18)

print(x >1 and x < 4 and x <10)

# or opeator
x = 3
print(x < 4 or x > 10)

# not operator
x = 3
print(not(x < 5 and x))

x = 5
print(not(x < 5 and x < 10))

# is
x = 3
y = 3
print(x is y)


# is not
x = 3
y = 3
print(x is not y)




# check python version
import sys

print(sys.version)

print("hello ai")


# for hashtag press alt + 3
# run selection
# first select the code and then shift + alt + e
print("hello ai")


# if you want to bring your code press cmd + 2



# numbers
3

5.5

3 + 2

4 * 5

if 9 > 3
    print("nine is greater then three")

type(3) # integer
type(5.5) # float
type(5,5) # type error, will not work

print("rana")
type("rana")


# comments
## comments can be used to explain python code
## comments can be used to make the code more readable
## comments can be used to prevent when testing code



# this is a comment
print("hello world")


# comments can be placed at the end of a line and python will ignore the rest of the line
print("hello world") # test


# to end a multi-line comment, you can add a # to each line.

# it's a comment
# you need to fix this code
# look at the data again
print("rana")


# if you want to add a multi-line string to your script, you can do so with triple """ quotes.

def multiplication(x, y):
   """
   this is a function comment
   :param x:
   :param y:
   :return:
   """

  print(x * y)
   multiplication(5, 7)



def add(x, y)

    """this is addition function add two numbers for x and y"""

    print(x + y)

    add(10, 8)


# python variables
# A variable is created the first time you assign a value to a variable

var1 = 5
var2 = 10
print(var1)
print(var2)

var1 + var2


# variables can change type after they are set and are not required to be staded with a certain
# example
x = 9 # x is of type int
type(x)

x = "james" # x is now of type str
type(x)

# casting
# if you want to specify the data type of variable, this can be done with casting
x = str(9)

x = int(9) # x will be integer

x = float(9) # x will be float
type(x)
print(type(x))

# get type
# you can get data type of variable with the type() function

x = 9
y = "jason"
print(type(x))
print(type(y))

# single or double quotes?
## you can use single or double quotes

x = "rana"
x = 'rana'
# they are the same


# case-sensitive
# variable names are case-sensetive.

x = 9
X = "rana"

myvar = "rana"
my_var = "rana"
_my_var = "rana"
myVar = "rana"
MYVAR = "rana"
myvar2 = "rana"


# give a short name or a more descriptive name (age,name,total etc.)
# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number

# not assagined or used
2myvar = "rana"
my-var = "rana"
my var = "rana"


# one value to multiple variables

x = y = z = "cat"
print(x)
print(y)
print(z)


# unpack collection

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# print() function is often used to output variables
print(x)

print(x, y, z)

# you can also use the + operator to output multiple variables
x = "python "
y = "is "
z = "great "
print(x, y, z,)

x = 5
y = "jhon"
print(x + y)
print(x , y)


x = str(5)
y = " jhon"
print(x + y)

# global variables
x = "awesome"

def myfunc():
    print("python is " +x)

myfunc()



# if you create a variable with the same name inside a function, this variable will be local, and
# can be used inside the function. Global variable with thw same name will remain as it was,
# global and with th original value

x = "awesome"

def myfunc():
    x = "fantastic"
    print("python is " + x)

myfunc()

x



def myfunc():
    global x
    x = "fantastic"

myfunc()

print("python is " + x)












