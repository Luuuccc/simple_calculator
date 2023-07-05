import operator
import re

ops = {"+": operator.add,
       "-": operator.sub,
       "*": operator.mul,
       "/": operator.truediv,
       }

def calculate():
    # Ask the user whether to enter two numbers and an operator or read from a file
    choice = input("Enter '1' to enter two numbers and an operator, '2' to read from a file: ")

    if choice == "1":
        # Get input from the user
        while True:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                break
            except ValueError:
                print("Invalid input. Please renter a number.")
        
        while True:
            op = input("Enter operator (+, -, *, /): ")
            if op not in ["+", "-", "*", "/"]:
                print("Invalid operator. Please enter +, -, * or /.")
            else:
                break

        # Calculate the result
        try:
            result = ops[op](num1, num2)
            equation = f"{num1} {op} {num2} = {result}"
            print(equation)
        except ZeroDivisionError: 
            equation = f"{num1} {op} {num2} = Cannot divide by zero"
            print(equation)
        except Exception as e:
            equation = f"{num1} {op} {num2} = Error: {str(e)}"
            print(equation)

        # Write the equation entered by the user to the file
        with open("equations.txt", "a") as file:
            file.write(equation + "\n")

    elif choice == "2":
        # Get equation input imported from a file
        while True:
            try:
                filename = str(input("Enter the name of the text file: ")+".txt")
                with open(filename,"r") as file:
                    equations = file.readlines()
                    break
            except FileNotFoundError:
                print("File not found. . Please enter the name of an existing text file.")

        # Calculate the results for each equation in the file
        for equation in equations:
            equation = equation.strip()
            try:
                num1, op, num2 = re.findall(r"(\-?\d+\.?\d*)(\+|\-|\*|\/)(\-?\d+\.?\d*)", equation)[0]
                num1 = float(num1)
                num2 = float(num2)
            except Exception as e:
                print(f"Error: {str(e)}")
                continue

            try:
                result = ops[op](num1, num2)
                print(f"{equation} = {result}")
            except ZeroDivisionError:
                print(f"Cannot divide by zero in {equation}")
            except Exception as e:
                print(f"Error in {equation}: {str(e)}")
                
    else:
        print("Invalid choice")

calculate()