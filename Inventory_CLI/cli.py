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

def print_items(lst):
    for l in lst:
        print(f"ID: {l['id']}, Name: {l['name']}, Quantity: {l['quantity']}, Price: {l['price']}")

def handle_command(command_line):
    if command_line.startswith("list"):
        lst = storage.load_inventory(filename)
        print_items(lst)
        return True
    if command_line.startswith("exit"):
        print("Exiting the program.")
        return False
    if command_line.startswith("add"):
        cls= command_line.split()
        inventory.add_item(filename, cls[1], int(cls[2]), float(cls[3]))
        print(f"Item '{cls[1]}' added successfully.")
        return True
    if command_line.startswith("remove"):
        cls = command_line.split()
        success = inventory.remove_item(filename, cls[1])
        if success:
            print(f"Item '{cls[1]}' removed successfully.")
        else:
            print(f"Item '{cls[1]}' not found.")
        return True
    if command_line.startswith("restock"):
        cls = command_line.split()
        inventory.restock_item(filename, cls[1], int(cls[2]))
        print(f"Item '{cls[1]}' restocked successfully.")
        return True
    if command_line.startswith("value"):
        total = inventory.total_value(filename)
        print(f"Total inventory value: {total}")
        return True
    if command_line.startswith("low"):
        cls = command_line.split()
        threshold = int(cls[1]) if len(cls) > 1 else 5
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