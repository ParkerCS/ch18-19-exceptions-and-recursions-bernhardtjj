# EXCEPTIONS (use me sparingly please)

# Exception = condition that results in abnormal program flow
# Exception handling = what we actively do to for exceptions
# Catch = code that handles abnormal conditions
# Throw/raise = abnormal conditions THROW or RAISE Exceptions
# Unhandled exceptions = Thrown, but not caught.  Program killers

# Common exception handling we might do:
# Divide by zero error (ZeroDivisionError)

my_list = [1, 2, 3]
my_list2 = my_list[:]

print(id(my_list))
print(id(my_list2))

x = 0
y = 2

try:
    print(y / x)
except:
    print("Invalid operation")

# Conversion error (ValueError)

done = False

while not done:
    try:
        user_input = int(input("Enter a valid number: "))
        done = True
    except:
        print("Number entered was not valid")

# File opening (IOError, FileNotFoundError)

try:
    file = open("AliceInWonderLand.txt")
except:
    print("Could not open file")

# Use the built in error types for python

try:
    # my_file = open("myfile.txt")
    # int("Hello")
    print(1 / 0)
except FileNotFoundError:
    print("File not found")
except ZeroDivisionError:
    print("You cannot divide by zero fool!")
except ValueError:
    print("Invalid integer conversion")
except:
    print("Unknown error")

# Exception object (grabbing the caught exception object)

try:
    print(1 / 0)
except ZeroDivisionError as e:
    print(e)
