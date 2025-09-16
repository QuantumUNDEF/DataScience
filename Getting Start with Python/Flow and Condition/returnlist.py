numbers = []
while True:
    userInput = input("Enter postive number(non positive to stop): ")
    if userInput.replace('.', '',1).isdigit() and float(userInput) >=0:
        numbers.append(float(userInput))
    elif userInput.replace('-', '',1).isdigit() and float(userInput) <0:
        break
    else:
        print("Invalid input")
if numbers:
    print(numbers)
else:
    print("No positive number is entered(" )