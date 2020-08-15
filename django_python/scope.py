# Scope in Python
# |-> Python Scope follows the LEGB Rule:
#       * Local
#       * Enclosing Function Locals
#       * Global
#       * Built-in

x = 25

def my_fun():
    x = 50
    return x

# print(x)            #expected output - 25
# print(my_fun())     #expected output - 50

my_fun()            #expected out ? - take a while and think..
print(x)            #expected output - 25 -> this is due to Global Scope

# Local

lambda x: x ** 2

        #  another Example
x = 50
def fun(x):
    print("x is: ",x)                   #output Global x = 50, because x isnot declared locally yet
    x = 1000                            #local x
    print("local x changed to: ",x)     #output local x = 1000

fun(x)

# Enclosing Function Locals

name = "This is global name"

def greet():
    name = "Sammy"

    def hello():
        print("Hello",name)
    hello()

greet()         #EFL -> Hello Sammy
print(name)     #Global - This is global name

# Built-in
    # len()

# Global

x = 50

def fun():
    global x
    x = 1000

print("Before fun call, x is: ",x)
fun()
print("After fun call, x is: ",x)    
