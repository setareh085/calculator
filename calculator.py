from calculator_oop import calculators
from to_check import get_number
from to_check import is_empty

calc = calculators()

while (True):
    print("Choose from the options below: ")
    print("1. add")
    print("2. sum")
    print("3. minus")
    print("4. multi")
    print("5. div")
    print("6. exit")
    choice = input("your choice: ")

    if choice == "1":
        numbers = int(input("Enter the number of numbers you want to operate on(2 or more): "))
        for i in range(numbers):
            num = get_number(f"Enter number {i+1}: ")
            calc.add_cal(num)
        
    elif choice == "2":
            if is_empty(calc.calculator):
                print("Please enter numbers first!")
            else:
                print("Sum:", calc.sum_cal())

    elif choice == "3":
            if is_empty(calc.calculator):
                print("Please enter numbers first!")
            else:
                print("Minus:", calc.minus_cal())

    elif choice == "4":
            if is_empty(calc.calculator):
                print("❌ Please enter numbers first!")
            else:
                print("Multi:", calc.multi_cal())

    elif choice == "5":
            if is_empty(calc.calculator):
                print("Please enter numbers first!")
            else:
                print("Div:", calc.div_cal())
    elif choice == "6":
         break
    print("You have been logged out.")