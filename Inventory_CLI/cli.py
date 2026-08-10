import storage
import inventory
filename = "/home/daniel/self_projects/Inventory_CLI/inventory_data.txt"

def print_menu():
    print("list")
    print("add <name> <quantity> <price>")
    print("remove <name>")
    print("restock <name> <amount>")
    print("value")
    print("low or low <threshold>")
    print("help")
    print("exit")

def print_items(records):
    if not records:
        print("No items found.")
    for record in records:
        print(f"ID: {record['id']}, Name: {record['name']}, Quantity: {record['quantity']}, Price: {record['price']}")

def handle_command(command_line):
    if command_line.startswith("list"):
        records = storage.load_inventory(filename)
        print_items(records)
        return True
    if command_line.startswith("exit"):
        print("Exiting the program.")
        return False
    if command_line.startswith("add"):
        parts = command_line.split()
        inventory.add_item(filename, parts[1], int(parts[2]), float(parts[3]))
        print(f"Item '{parts[1]}' added successfully.")
        return True
    if command_line.startswith("remove"):
        parts = command_line.split()
        success = inventory.remove_item(filename, parts[1])
        if success:
            print(f"Item '{parts[1]}' removed successfully.")
        else:
            print(f"Item '{parts[1]}' not found.")
        return True
    if command_line.startswith("restock"):
        parts = command_line.split()
        inventory.restock_item(filename, parts[1], int(parts[2]))
        print(f"Item '{parts[1]}' restocked successfully.")
        return True
    if command_line.startswith("value"):
        total = inventory.total_value(filename)
        print(f"Total inventory value: {total}")
        return True
    if command_line.startswith("low"):
        parts = command_line.split()
        threshold = int(parts[1]) if len(parts) > 1 else 5
        low_stock = inventory.low_stock_items(filename, threshold)
        print_items(low_stock)
        return True
    if command_line.startswith("help"):
        print_menu()
        return True

def main():
    print("Welcome to the Inventory Management CLI!")
    print_menu()
    status = True
    while status:
        command_line = input("Enter a command: ")
        status = handle_command(command_line)

if __name__ == "__main__":
    main()