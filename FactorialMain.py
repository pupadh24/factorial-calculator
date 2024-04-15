def Factorial():
    number = int(input("Enter a Number: "))
    fact = 1

    if number < 0:
        print("Factorial cannot be found for negative numbers!")
    elif number == 0:
        print(f"The Factorial of {number} is: 1")
    else:
        for i in range(1, number+1):
            fact = fact * i
        print(f"The Factorial of {number} is: {fact}")

Factorial()
    