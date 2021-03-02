class Calc_app():
    def __init__(self, number_1, number_2):
        self.number_1 = number_1
        self.number_2 = number_2

    def addition(self):
        return self.number_1 + self.number_2

    def subtraction(self):
        return self.number_1 - self.number_2

    def multiplication(self):
        return self.number_1 * self.number_2

    def division(self):
        return self.number_1 / self.number_2


# Inputs from the user
number_1 = int(input("Enter first number"))
number_2 = int(input("Enter second number"))
# Creating Class object
class_obj = Calc_app(number_1, number_2)

# Validating user choice and instantiating functions from class object
user_choice = 1
while user_choice != 0:
    print(f"0 : EXIT")
    print(f"1 : Addition")
    print(f"2 : Subtraction")
    print(f"3 : Multiplication")
    print(f"4 : Division")
    user_choice = int(input("Enter your choice from above menu"))
    if user_choice == 1:
        print(f"Result of the operation is: {class_obj.addition()}")
    elif user_choice == 2:
        print(f"Result of the operation is: {class_obj.subtraction()}")
    elif user_choice == 3:
        print(f"Result of the operation is: {class_obj.multiplication()}")
    elif user_choice == 4:
        print(f"Result of the operation is: {class_obj.division()}")
    elif user_choice == 0:
        print(f"Exiting the operation")
