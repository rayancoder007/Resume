# Calculator Addition Program
# Rayan Chowdhury
# Enrollment Number - BT20HCS364

# Starting with the code

print("Addtion Program for calculator")
x1 = int(input("Enter the first number"))
x2 = int(input("Enter the second number"))

print("Do you want to add more numbers?")
print("Type 1 for 'Yes' and 2 for 'No'")
x = int(input())

y = int(input("How many times you want to add?"))
h = 0
if x == 1:
    for i in range(y):
        d = int(input("Enter number"))
        h = h + d
else:
    print("Only two variables selected for default addition")

x3 = x1 + x2 + h
print("The final result of addition is : ",x3)

# Ending with the code


    