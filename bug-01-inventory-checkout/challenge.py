# Example inventory and cart dictionaries.
# These are here so you can quickly run the file and experiment.
inventory = {
    "SKU123": 5,
    "SKU999": 2,
}
cart = {
    "SKU123": 2,
    "SKU999": 3,
}

def get_stock(sku, inventory):
    """
    Returns how many units are available for a given SKU.
    If the SKU does not exist, assume 0.
    """
    if sku in inventory:
        return int(inventory[sku])
    return 0


def has_sufficient_stock(cart, inventory):
    """
    Validate that the cart can be fulfilled with current inventory.

    Guidance:
    - Think about the difference between "SKU exists" vs.
      "there are enough units for the requested quantity".
    - Check the *intent* of this function name against what it actually does.

    Hint: If users report overselling, this *validation step* might not be strict enough.
    """
    for sku in cart:
        available = get_stock(sku, inventory)
        # Current behavior only checks for "something > 0".
        if available <= 0:
            return False
    return True


def deduct_stock(cart, inventory):
    """
    Reduce inventory by the quantities in the cart.

    Guidance:
    - Decide clearly: does this function *mutate* the given inventory,
      or should it *return* a new one? Be consistent with your choice.
    - If you choose to mutate, make sure any computed values actually
      end up stored in the inventory structure.

    Hint: If stock appears unchanged after placing an order,
    the issue could be in how updates are applied here.
    """
    for sku in cart:
        quantity_needed = int(cart[sku])
        current = get_stock(sku, inventory)
        new_value = current - quantity_needed  # computed value
        if new_value < 0:
            new_value = 0  # avoid negatives
        # Note: consider whether this function should persist the update.


def place_order(cart, inventory):
    """
    Simplified order flow:
    1) Validate stock (should reject if any SKU is short).
    2) Deduct stock (should reflect the new inventory state).
    3) Return a small summary.

    All-or-nothing:
    - If any item cannot be fulfilled, there should be no partial updates.
    """
    ok = has_sufficient_stock(cart, inventory)
    if not ok:
        return {"ok": False, "reason": "insufficient_stock", "items": dict(cart)}

    deduct_stock(cart, inventory)

    total_items = 0
    for sku in cart:
        total_items += int(cart[sku])

    return {"ok": True, "items": dict(cart), "total_items": total_items}


# You can test quickly by running this file directly:
if __name__ == "__main__":
    print("=== Odd Socks Order Simulation ===\n")

    print("📦 Inventory BEFORE order:", dict(inventory))
    print("🛒 Cart to order:", dict(cart))
    print()

    result = place_order(cart, inventory)

    if result["ok"]:
        print("✅ Order placed successfully!")
        print("  Items in the order:", result["items"])
        print("  Total items ordered:", result["total_items"])
    else:
        print("❌ Order could not be placed.")
        print("  Reason:", result.get("reason"))
        print("  Requested items:", result["items"])

    print("\n📦 Inventory AFTER order:", dict(inventory))


