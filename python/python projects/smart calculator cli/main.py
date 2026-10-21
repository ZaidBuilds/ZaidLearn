print("===== SMART CALCULATOR CLI =====")


# ---------- Calculator Functions ----------

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return None
    return a / b


def modulus(a, b):
    if b == 0:
        return None
    return a % b


def power(a, b):
    return a ** b


# ---------- Calculation Function ----------

def calculate(num1, num2, operator):
    
    if operator == "1":
        return add(num1, num2), "+"

    elif operator == "2":
        return subtract(num1, num2), "-"

    elif operator == "3":
        return multiply(num1, num2), "*"

    elif operator == "4":
        return divide(num1, num2), "/"

    elif operator == "5":
        return modulus(num1, num2), "%"

    elif operator == "6":
        return power(num1, num2), "**"

    else:
        return None, None


# ---------- Get Number Function ----------

def get_number(message):

    while True:

        try:
            return float(input(message))

        except ValueError:
            print("❌ Please enter a valid number.")


# ---------- Show Calculator Menu ----------

def show_calculator_menu():

    print("\nSelect an operator:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponent (**)")


# ---------- Main Program ----------

history = []

while True:

    print("\n===== SMART CALCULATOR =====")
    print("1. New Calculation")
    print("2. View History")
    print("3. Clear History")
    print("4. Exit")

    choice = input("Choose an option: ")

    # ---------- New Calculation ----------

    if choice == "1":

        num1 = get_number("\nEnter the first number: ")
        num2 = get_number("Enter the second number: ")

        show_calculator_menu()

        operator = input("Enter your choice (1-6): ")

        result, symbol = calculate(num1, num2, operator)

        if symbol is None:
            print("❌ Invalid operator choice.")
            continue

        if result is None:
            print("❌ Cannot divide or perform modulus by zero.")
            continue

        print("✅ Result:", result)

        calculation = f"{num1} {symbol} {num2} = {result}"

        history.append(calculation)

    # ---------- View History ----------

    elif choice == "2":

        print("\n===== CALCULATION HISTORY =====")

        if len(history) == 0:
            print("No calculations yet.")

        else:
            for calculation in history:
                print(calculation)

    # ---------- Clear History ----------

    elif choice == "3":

        history.clear()

        print("🗑️ History cleared.")

    # ---------- Exit ----------

    elif choice == "4":

        print("\nGoodbye! 👋")
        break

    # ---------- Invalid Menu Choice ----------

    else:

        print("❌ Invalid choice. Please select 1-4.")