# First program
print("Welcome to the first program!")

name = input("What is your name? ")
age = input("How old are you? ")
class1 = input("What is your class? ")
height = input("What is your height? ")
print(f"Hello {name}, you are {age} years old, in class {class1}, and your height is {height}.")
print("Thank you for using the first program!")

# addition
print('sum:', age + class1 + height)

#subtraction
print('subtraction:',int(age) - int(class1) - float(height) )

# multiplication
print('multiplication:', int(age) * int(class1) * float(height))

# division
print('division:', int(age) / int(class1) / float(height))

#floor division
print('floor division:', int(age) // int(class1) // float(height))

# modulus
print('modulus:', int(age) % int(class1) % float(height))


# equal to operator
print('equal to:', int(age) == int(class1) == float(height))

# not equal to operator
print('not equal to:', int(age) != int(class1) != float(height))

# greater than operator
print('greater than:', int(age) > int(class1) > float(height))

# less than operator
print('less than:', int(age) < int(class1) < float(height)) 
# greater than or equal to operator
print('greater than or equal to:', int(age) >= int(class1) >= float(height))    
# less than or equal to operator
print('less than or equal to:', int(age) <= int(class1) <= float(height))
# logical operators
print('and operator:', int(age) > 18 and int(class1) < 10) 


