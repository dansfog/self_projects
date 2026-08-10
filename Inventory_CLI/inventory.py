import storage

def add_item(filename, name, quantity, price):
    lst = storage.load_inventory(filename)
    new_id = max(record["id"] for record in lst) + 1 if lst else 1
    new_lst = {
        "id": new_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }
    lst.append(new_lst)
    storage.save_inventory(filename, lst)
    return new_lst

def remove_item(filename, name):
    lst = storage.load_inventory(filename)
    for l in lst:
        if l["name"].casefold() == name.casefold():
            lst.remove(l)
            storage.save_inventory(filename, lst)
            return True
    return False

def restock_item(filename, name, amount):
    lst = storage.load_inventory(filename)
    for l in lst:
        if l["name"].casefold() == name.casefold():
            l["quantity"] += amount
            storage.save_inventory(filename, lst)
            return l
    return None

def total_value(filename):
    lst = storage.load_inventory(filename)
    total = float(sum(l["quantity"] * l["price"] for l in lst))
    return total

def low_stock_items(filename, threshold=5):
    lst = storage.load_inventory(filename)
    low_stock = [l for l in lst if l["quantity"] < threshold]
    return low_stock
