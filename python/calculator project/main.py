# Store all calculation history
history = []


# Function for addition
def add(a, b):
    return a + b


# Function for subtraction
def subtract(a, b):
    return a - b


# Function for multiplication
def multiply(a, b):
    return a * b


# Function for division
def divide(a, b):

    # Check divide by zero
    if b != 0:
        return a / b

    else:
        return "Cannot divide by zero"


# Infinite loop to keep calculator running
while True:

    # Show menu
    print("\n==== Calculator ====")

    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("6. Show History")

    # Take user choice
    choice = input("Enter your choice: ")


    # Exit condition
    if choice == "5":
        print("Goodbye!")
        break


    # Show history
    elif choice == "6":

        print("\n=== History ===")

        for item in history:
            print(item)

        continue


    # Try taking numbers safely
    try:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

    except:

        print("Please enter valid numbers")
        continue


    # Addition
    if choice == "1":

        result = add(num1, num2)

        print("Result:", result)

        history.append(f"{num1} + {num2} = {result}")


    # Subtraction
    elif choice == "2":

        result = subtract(num1, num2)

        print("Result:", result)

        history.append(f"{num1} - {num2} = {result}")


    # Multiplication
    elif choice == "3":

        result = multiply(num1, num2)

        print("Result:", result)

        history.append(f"{num1} * {num2} = {result}")


    # Division
    elif choice == "4":

        result = divide(num1, num2)

        print("Result:", result)

        history.append(f"{num1} / {num2} = {result}")


    # Invalid menu choice
    else:
        print("Invalid choice")