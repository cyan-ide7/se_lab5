import json
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s")

stock_data = {}


def addItem(item="default", qty=0, logs=None):
    """Add a given quantity of an item to stock."""
    if logs is None:
        logs = []

    if not isinstance(item, str) or not isinstance(qty, int):
        logging.warning("Invalid input types for addItem: %s, %s", item, qty)
        return

    stock_data[item] = stock_data.get(item, 0) + qty
    logs.append(f"{datetime.now()}: Added {qty} of {item}")
    logging.info("Added %d of %s", qty, item)


def removeItem(item, qty):
    """Remove quantity of item from stock safely."""
    try:
        stock_data[item] -= qty
        if stock_data[item] <= 0:
            del stock_data[item]
            logging.info("Removed %s from stock", item)
    except KeyError:
        logging.warning("Attempted to remove non-existent item: %s", item)


def getQty(item):
    """Return quantity of item."""
    return stock_data.get(item, 0)


def loadData(file="inventory.json"):
    """Load inventory data safely."""
    global stock_data
    try:
        with open(file, "r") as f:
            stock_data = json.load(f)
    except FileNotFoundError:
        logging.warning("File not found: %s. Starting with empty stock.", file)
        stock_data = {}


def saveData(file="inventory.json"):
    """Save inventory data safely."""
    with open(file, "w") as f:
        json.dump(stock_data, f, indent=4)


def printData():
    """Display current stock data."""
    print("Items Report")
    for item, qty in stock_data.items():
        print(f"{item} -> {qty}")


def checkLowItems(threshold=5):
    """Return list of items below threshold."""
    return [i for i, qty in stock_data.items() if qty < threshold]


def main():
    addItem("apple", 10)
    addItem("banana", -2)
    addItem(123, "ten")  # Invalid; warning logged
    removeItem("apple", 3)
    removeItem("orange", 1)
    print("Apple stock:", getQty("apple"))
    print("Low items:", checkLowItems())
    saveData()
    loadData()
    printData()


if __name__ == "__main__":
    main()
