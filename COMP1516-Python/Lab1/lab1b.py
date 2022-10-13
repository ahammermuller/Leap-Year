# Aline Hammermuller
# A01276569

# a. Get the user's name and print a hello message to the user.
print("Enter your name:")
name = input()
print("Hello,",name)

# b. Ask the user to input two integers and sum both printing the result.
x_value = int(input("Please input an integer value: "))
y_value = int(input("Please input another integer value: "))
xy_sum = x_value + y_value
print(x_value, "+", y_value, "=", xy_sum)

# c. Multiply two float numbers and print the result.
a_value = 10.5
b_value = 4.0
c_value = a_value * b_value
print(a_value, "*", b_value, "=", c_value)

# d. Print the difference between c_value and xy_sum.
# The c_value was converted to an integer, so the result is 27.
# Otherwise, the result will a float (27.0)
print(int(c_value) - xy_sum)

# e. Print the string “This program is done.”
print("This program is done.")