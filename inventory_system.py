import json
import logging
from datetime import datetime

# Global variable
stock_data = {}

def addItem(item="default", qty=0, logs=None):
    """Adds a quantity to an item in the stock_data.""" 
    if logs is None:
        logs = []
        
    if not item:
        return
        
    if not isinstance(item, str) or not isinstance(qty, int):
        print(f"Warning: Skipping invalid item/quantity: {item}, {qty}")
        return
        
    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")

def removeItem(item, qty):
    """Removes a quantity of an item from the stock_data.""" 
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
    except KeyError:
        pass

def getQty(item):
    """Returns the quantity of an item.""" 
    return stock_data.get(item, 0)

def loadData(file="inventory.json"):
    """Loads inventory data from a JSON file.""" 
    try:
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
        with open(file, "w") as f:
            f.write(json.dumps(stock_data))
    except IOError:
        print(f"Error: Could not write to file '{file}'.")

def printData():
    """Prints a report of all items and their quantities.""" 
    print("\n--- Items Report ---")
    for i in stock_data:
        print(f"{i} -> {stock_data[i]}")

def checkLowItems(threshold=5):
    """Returns a list of items with quantity below the threshold.""" 
    result = []
    for i in stock_data:
        if stock_data[i] < threshold:
            result.append(i)
    return result

def main():
    logs = []
    
    loadData()
    
    addItem("apple", 10, logs)
    addItem("banana", 5, logs)
    addItem(123, "ten", logs)
    removeItem("apple", 3)
    removeItem("orange", 1)
    
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    
    saveData()
    printData()
    

    print("\n--- Execution Logs ---")
    for log_entry in logs:
        print(log_entry)

if __name__ == '__main__': 
    main()