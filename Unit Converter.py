def length_converter():
    print("\nLength Conversion")
    print("1. Meters to Kilometers")
    print("2. Kilometers to Meters")

    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value / 1000, "km")
    elif choice == 2:
        print("Result:", value * 1000, "m")
    else:
        print("Invalid choice")


def weight_converter():
    print("\nWeight Conversion")
    print("1. Kilograms to Grams")
    print("2. Grams to Kilograms")

    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        print("Result:", value * 1000, "g")
    elif choice == 2:
        print("Result:", value / 1000, "kg")
    else:
        print("Invalid choice")


def temperature_converter():
    print("\nTemperature Conversion")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter choice: "))
    value = float(input("Enter value: "))

    if choice == 1:
        result = (value * 9/5) + 32
        print("Result:", result, "°F")
    elif choice == 2:
        result = (value - 32) * 5/9
        print("Result:", result, "°C")
    else:
        print("Invalid choice")


# Main Menu
while True:
    print("\n=== UNIT CONVERTER ===")
    print("1. Length")
    print("2. Weight")
    print("3. Temperature")
    print("4. Exit")

    option = int(input("Choose an option: "))

    if option == 1:
        length_converter()
    elif option == 2:
        weight_converter()
    elif option == 3:
        temperature_converter()
    elif option == 4:
        print("Exiting Program...")
        break
    else:
        print("Invalid option")