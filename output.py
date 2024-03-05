#variable declaration
x = 25
message = "Wow!"
ratio = 3.14

#checking the type of data with type() method.
print(type(message))
print(type(ratio))
print(type(x))
#String formatting
print(message + "my name is name . I am " + str(x) + " years old" )
print(f"{message} my name is name . I am {x} years old.")