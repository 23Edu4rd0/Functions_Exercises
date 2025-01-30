def add(n1, n2):
    return n1 + n2


def minus(n1, n2):
    return n1 - n2


def times(n1, n2):
    return n1 * n2

# 
def over(n1, n2):
    return n1 / n2

# Dictionary to map operation symbols to their corresponding functions
operations = {"+": add, "-": minus, "*": times, "/": over}

"""_loop to start the calculations_
"""
while True:
   
    Number1 = int(input("What's the first number? "))
    """new loop opened in case the user wants to use the previous number from the old calculation
    """
    while True:
        
        operation = input("+\n-\n*\n/\nPick an operation: ")
        
    
        if operation not in operations:
            print("Invalid operation. Try again")
            continue

      
        Number2 = int(input("What's the second number? "))

        # Perform the operation and store the result
        result = operations[operation](Number1, Number2)
        print(f"{Number1} {operation} {Number2} = {result}")

        # Ask the user if they want to continue calculating with the result, start a new calculation, or exit
        response = input(f"\nType 'y' to continue calculating with {result}, or type 'n' to start a new calculation, or 'exit' to quit: \n").lower()

        if response == "y":
            
            Number1 = result
        elif response == "n":
            
            break
        elif response == "exit":
            
            exit()
        else:
            
            print("Invalid keyword. Starting a new calculation.")
            break
