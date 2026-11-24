import math
from manufacturing_utils import (
    calculate_batch_cost,
    overall_defect_percentage
)

production = [
    (501, "Circuit Board", 100, 5, 250),
    (502, "Power Supply", 80, 12, 400),
    (503, "Sensor", 150, 8, 180),
    (504, "Controller", 60, 3, 650),
    (505, "Connector", 200, 15, 50)
]


def read_non_negative_int(prompt):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")
            continue

        if value < 0:
            print("Value cannot be negative.")
            continue

        return value


def read_non_negative_float(prompt):
    while True:
        try:
            value = float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if not math.isfinite(value) or value < 0:
            print("Value must be a finite, non-negative number.")
            continue

        return value


def add_batch():
    batch_id = read_non_negative_int("Enter batch ID: ")
    product_name = input("Enter product name: ")
    quantity = read_non_negative_int("Enter quantity produced: ")

    while True:
        defective = read_non_negative_int("Enter defective quantity: ")
        if defective <= quantity:
            break
        print("Defective quantity cannot exceed production quantity.")

    unit_cost = read_non_negative_float("Enter cost per unit: ")
    production.append((batch_id, product_name, quantity, defective, unit_cost))
    print("New production batch added successfully.")


def main():
    while True:
        print("\nProduction Records Management")
        print("1. Display all production records")
        print("2. Add a new production batch")
        print("3. Calculate batch costs (using imported function)")
        print("4. Calculate overall defect percentage")
        print("5. Show batches with more than 10 defective units")
        print("6. Show accepted production quantities (using map)")
        print("7. Calculate batch costs (using lambda)")
        print("8. Exit")

        choice = read_non_negative_int("Enter your choice: ")

        if choice == 1:
            for record in production:
                print(
                    f"Batch {record[0]} | {record[1]} | "
                    f"Quantity: {record[2]} | Defective: {record[3]} | "
                    f"Cost per unit: {record[4]}"
                )

        elif choice == 2:
            add_batch()

        elif choice == 3:
            for record in production:
                cost = calculate_batch_cost(record)
                print(f"Batch {record[0]} ({record[1]}): {cost:.2f}")

        elif choice == 4:
            try:
                percentage = overall_defect_percentage(production)
                print(f"Overall defect percentage: {percentage:.2f}%")
            except ValueError as error:
                print(error)

        elif choice == 5:
            batches = filter(lambda record: record[3] > 10, production)
            print("Batches with more than 10 defective units:")
            for record in batches:
                print(f"Batch {record[0]} ({record[1]}): {record[3]} defective")

        elif choice == 6:
            accepted_quantities = list(
                map(lambda record: record[2] - record[3], production)
            )
            print("Accepted production quantities:", accepted_quantities)

        elif choice == 7:
            for record in production:
                batch_cost = (lambda r: r[2] * r[4])(record)
                print(f"Batch {record[0]} ({record[1]}): {batch_cost:.2f}")

        elif choice == 8:
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Enter a number from 1 to 8.")


try:
    main()
except (KeyboardInterrupt, EOFError):
    print("\nInput cancelled.")
finally:
    print("Manufacturing program ended.")