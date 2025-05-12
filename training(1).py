

inventory = {}

# Function to add a product to the inventory
def add_product(name, price, quantity):
    if name in inventory:
        print("Product already exists.")
    else:
        inventory[name] = (price, quantity)
        print(f"Product '{name}' added successfully.")

# Function to search for a product by name
def search_product(name):
    if name in inventory:
        price, quantity = inventory[name]
        print(f"Product: {name}")
        print(f"Price: ${price}")
        print(f"Quantity: {quantity}")
    else:
        print("Product not found.")

# Function to update the price of a product
def update_price(name, new_price):
    if name in inventory:
        _, quantity = inventory[name]
        inventory[name] = (new_price, quantity)
        print(f"Price of '{name}' updated successfully.")
    else:
        print("Product not found.")

# Function to delete a product from the inventory
def delete_product(name):
    if name in inventory:
        del inventory[name]
        print(f"Product '{name}' deleted successfully.")
    else:
        print("Product not found.")

# Function to calculate the total inventory value using a lambda function
def calculate_total_value():
    total_value = sum(map(lambda item: item[0] * item[1], inventory.values()))
    print(f"Total inventory value: ${total_value}")

# Function to safely get a float input
def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

# Function to safely get an integer input
def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

# Main menu loop
def main():
    while True:
        print("\n=== Inventory Management Menu ===")
        print("1. Add product")
        print("2. Search product")
        print("3. Update product price")
        print("4. Delete product")
        print("5. Calculate total inventory value")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            name = input("Enter product name: ").strip()
            price = get_float_input("Enter product price: ")
            quantity = get_int_input("Enter product quantity: ")
            add_product(name, price, quantity)

        elif choice == "2":
            name = input("Enter product name to search: ").strip()
            search_product(name)

        elif choice == "3":
            name = input("Enter product name to update: ").strip()
            new_price = get_float_input("Enter new price: ")
            update_price(name, new_price)

        elif choice == "4":
            name = input("Enter product name to delete: ").strip()
            delete_product(name)

        elif choice == "5":
            calculate_total_value()

        elif choice == "6":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid option. Please select a number between 1 and 6.")

# Run the program
main()
