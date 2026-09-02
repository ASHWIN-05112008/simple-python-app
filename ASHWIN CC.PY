def add_numbers(a, b):
    return a + b

if __name__ == "__main__":
    print("--- Simple Addition App ---")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    result = add_numbers(num1, num2)
    print(f"The sum is: {result}")
