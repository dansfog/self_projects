import storage

def add_item(filename, name, quantity, price):
    records = storage.load_inventory(filename)
    new_id = max(record["id"] for record in records) + 1 if records else 1
    new_record = {
        "id": new_id,
        "name": name,
        "quantity": quantity,
        "price": price
    }
    records.append(new_record)
    storage.save_inventory(filename, records)
    return new_record

def remove_item(filename, name):
    records = storage.load_inventory(filename)
    for record in records:
        if record["name"].casefold() == name.casefold():
            records.remove(record)
            storage.save_inventory(filename, records)
            return True
    return False

def restock_item(filename, name, amount):
    records = storage.load_inventory(filename)
    for record in records:
        if record["name"].casefold() == name.casefold():
            record["quantity"] += amount
            storage.save_inventory(filename, records)
            return record
    return None

def total_value(filename):
    records = storage.load_inventory(filename)
    total = float(sum(record["quantity"] * record["price"] for record in records))
    return total

def low_stock_items(filename, threshold=5):
    records = storage.load_inventory(filename)
    low_stock = [record for record in records if record["quantity"] < threshold]
    return low_stock
