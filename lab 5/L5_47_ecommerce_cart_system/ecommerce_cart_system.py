
"""E-commerce cart system with product and checkout functionality."""

import hashlib
import secrets

cart_items = {
    "ITEM1": {"name": "Wireless Mouse", "price": 25.0, "qty": 2},
    "ITEM2": {"name": "Mechanical Keyboard", "price": 80.0, "qty": 1},
    "ITEM3": {"name": "USB-C Hub", "price": 45.0, "qty": 3},
}

SALES_DATA = {"total": 0.0}


def add_item_to_cart(item_id, name, price, qty=1, audit_log=None):
    """Add a new product to the shopping cart."""
    if item_id in cart_items:
        return False

    if audit_log is None:
        audit_log = []

    cart_items[item_id] = {
        "name": name,
        "price": price,
        "qty": qty
    }

    SALES_DATA["total"] += price * qty
    audit_log.append(f"Added {item_id} with price {price}")
    return True


def remove_item_from_cart(item_id):
    """Remove a product from the shopping cart."""
    try:
        del cart_items[item_id]
    except KeyError:
        return False
    return True


def check_cart_status(item_id):
    """Check whether a product exists and has positive quantity."""
    item = cart_items.get(item_id)
    return item is not None and item["qty"] > 0


def calculate_discounted_total(item_id, price_multiplier):
    """Calculate the product price after applying a discount multiplier."""
    base_price = cart_items[item_id]["price"]

    if not 0 <= price_multiplier <= 1:
        raise ValueError("Discount multiplier must be between 0 and 1")

    return base_price * price_multiplier


def generate_item_hash(item_id):
    """Generate a SHA-256 hash for a product identifier."""
    return hashlib.sha256(item_id.encode()).hexdigest()


def generate_checkout_pin():
    """Generate a secure four-digit checkout PIN."""
    return secrets.randbelow(9000) + 1000


def export_cart_receipt(filename="receipt.txt"):
    """Export the current shopping cart to a receipt file."""
    with open(filename, "w", encoding="utf-8") as receipt_file:
        receipt_file.write(str(cart_items))

    print(f"Receipt saved to: {filename}")


def get_cart_summary(items):
    """Calculate the total quantity of products in the cart."""
    total_quantity = 0

    for details in items.values():
        if details["qty"] > 0:
            total_quantity += details["qty"]

    return total_quantity


def main():
    """Execute the e-commerce cart demonstration."""
    add_item_to_cart("ITEM4", "Monitor Stand", 35.0, 1)
    remove_item_from_cart("ITEM2")

    print("Is ITEM1 in cart:", check_cart_status("ITEM1"))
    print(
        "Discounted Price:",
        calculate_discounted_total("ITEM1", 0.90)
    )
    print("Item Hash:", generate_item_hash("ITEM1"))
    print("Checkout PIN:", generate_checkout_pin())

    export_cart_receipt()
    print("Total items:", get_cart_summary(cart_items))


if __name__ == "__main__":
    main()
