# Did some extra research, just to get a little help to make it flawless.
# https://www.studocu.com/en-za/messages/question/2756297/create-a-simple-calculator-application-that-asks-a-user-to-enter-two-numbers-and-the-operation

# Function to addition two numbers.
def addition(x, y):
    return x + y

# Function to subtraction two numbers.
def subtraction(x, y):
    return x - y

# Function to multiplication two numbers.
def multiplication(x, y):
    return x * y

# Function to division two numbers.
# This prints message if the number is division by zero.
def division(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Division by zero\n"

# Create a file in write mode.
file = open("equations.txt", "a")

while True:

    # Read numbers and operator.
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operator = input("Enter operator: ")
    
    file.write(str(num1)+" "+operator+" "+str(num2)+"\n")
    
    # If else statement to print the answer for the given operator.
    if operator in ('+', '-', '*', '/'):
        if operator == '+':
            print(addition(num1, num2), "\n")

        elif operator == '-':
            print(subtraction(num1, num2), "\n")

        elif operator == '*':
            print(multiplication(num1, num2), "\n")

        elif operator == '/':
            
            print(division(num1, num2), "\n")
        
        prev_equations = input("Would you like to see your previous equations? (Yes - Y / No - N)\n")

        if prev_equations == "Y": # If user wants to see previous equations.
            file = open('equations.txt', 'r')
            read_file = file.read()
            print(read_file)
            file.close()

        else:
                    # Choose whether to continue or not.
                    choice = input("Continue - Y / No - N: ")

        if choice == "N":
            break
    else:
        print("Invalid Input\n")

# Close the file.
file.close()
