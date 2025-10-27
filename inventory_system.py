import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):
    """
    Adds a quantity to an item in the stock_data.
    Updates the logs list if provided.
    """
    # Fix 1: Mutable default argument logs=[] changed to logs=None
    if logs is None:
        logs = []
    
    # Optional Fix (Lab Suggested): Implement input validation
    if not isinstance(item, str) or not isinstance(qty, int):
        print(f"Warning: Skipping invalid item/quantity: {item}, {qty}")
        return

    if not item:
        return
        
    stock_data[item] = stock_data.get(item, 0) + qty
    
    # Style Fix: Using f-strings for cleaner logging (Lab Suggested)
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def removeItem(item, qty):
    """
    Removes a quantity of an item from the stock_data.
    Removes the item from stock_data if quantity is 0 or less.
    """
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    # Fix 2: Replaced bare except: with specific exception (KeyError)
    except KeyError:
        # Item not in stock_data, simply ignore the removal attempt
        pass

def getQty(item):
    """
    Returns the quantity of an item. 
    Returns 0 if the item is not found (Fix 3).
    """
    # Fix 3: Use .get() to prevent KeyError if the item doesn't exist
    return stock_data.get(item, 0)

def loadData(file="inventory.json"):
    """Loads inventory data from a JSON file into the global stock_data."""
    try:
        # Style Fix: Use 'with open' for automatic file closing
        with open(file, "r") as f:
            global stock_data
            stock_data = json.loads(f.read())
    except FileNotFoundError:
        print(f"Warning: Inventory file '{file}' not found. Starting with empty stock.")
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from '{file}'. Starting with empty stock.")

def saveData(file="inventory.json"):
    """Saves the current stock_data to a JSON file."""
    try:
        # Style Fix: Use 'with open' for automatic file closing
        with open(file, "w") as f:
            f.write(json.dumps(stock_data))
    except IOError:
        print(f"Error: Could not write to file '{file}'.")

def printData():
    """Prints a report of all items and their quantities."""
    print("\n--- Items Report ---")
    for i in stock_data:
        # Style Fix: Using f-strings for output
        print(f"{i} -> {stock_data[i]}")

def checkLowItems(threshold=5):
    """Returns a list of items with quantity below the threshold."""
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    # Initialize a list to track logs in this main execution
    logs = []
    
    # Load data before any operations
    loadData()
    
    addItem("apple", 10, logs)
    addItem("banana", 5, logs)
    # The call below now skips the item due to the input validation fix
    addItem(123, "ten", logs) 
    
    removeItem("apple", 3)
    # This is now gracefully ignored by the KeyError fix
    removeItem("orange", 1) 
    
    print("Apple stock:", getQty("apple"))
    print("Orange stock (should be 0):", getQty("orange"))
    print("Low items:", checkLowItems())
    
    saveData()
    printData()
    
    # Fix 4 (Security): Removed dangerous eval() function
    # eval("print('eval used')") 
    
    print("\n--- Execution Logs ---")
    for log_entry in logs:
        print(log_entry)

if __name__ == '__main__':
    main()