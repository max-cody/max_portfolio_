# max's calculator
# this func adds
def add(x, y):
    return x + y 

# this func subs
def subtract(x , y ):
    return x - y

#this func multiplies
def multiply(x, y):
    return x * y

# this func divides
def divide(x, y):
    return x / y

print("Select operation.")
print("1.Add")
print("2.subtract")
print("3.multiply")
print("4.divide")

while True:
    # take input from user
    choice = input("Enter your choice(1/2/3/4):")

    #check if choice is correct and not an error
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter your first number:"))
            num2 = float(input("Enter your second number:"))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))

        elif choice == '44':
            print(num1, "/", num2, "=", divide(num1, num2))

# check if the user wants to continue doing calculations, break loop if answer is no
        next_calc = input("Next calculation (y/n)?:")
        if next_calc == "n":
            break
    else:
        print("invalid input king")
