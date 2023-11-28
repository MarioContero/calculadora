from calculator import Calculator

class UI:
    def __init__(self):
        self.calculator = Calculator()

    def run(self):
        while True:
            print("Select an operation:")
            print("1. Add")
            print("2. Subtract")
            print("3. Multiply")
            print("4. Divide")
            print("5. Quit")

            choice = input("Enter choice (1/2/3/4/5): ")

            if choice == '1':
                num1 = self.get_float_input("Enter first number: ")
                num2 = self.get_float_input("Enter second number: ")
                result = self.calculator.add(num1, num2)
                self.display_result(result)
            elif choice == '2':
                num1 = self.get_float_input("Enter first number: ")
                num2 = self.get_float_input("Enter second number: ")
                result = self.calculator.subtract(num1, num2)
                self.display_result(result)
            elif choice == '3':
                num1 = self.get_float_input("Enter first number: ")
                num2 = self.get_float_input("Enter second number: ")
                result = self.calculator.multiply(num1, num2)
                self.display_result(result)
            elif choice == '4':
                num1 = self.get_float_input("Enter first number: ")
                num2 = self.get_float_input("Enter second number: ")
                try:
                    result = self.calculator.divide(num1, num2)
                    self.display_result(result)
                except ZeroDivisionError:
                    print("Error: Cannot divide by zero")
            elif choice == '5':
                break
            else:
                print("Invalid choice")

    def get_float_input(self, prompt):
        while True:
            try:
                num = float(input(prompt))
                return num
            except ValueError:
                print("Error: Invalid input")

    def display_result(self, result):
        print("Result: {}".format(result))