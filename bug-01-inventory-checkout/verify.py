import sys
from challenge import get_stock, has_sufficient_stock, deduct_stock, place_order

# ANSI escape codes for colors
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def check(name, condition):
    if condition:
        print(f"{GREEN}✅ PASS{RESET} - {name}")
    else:
        print(f"{RED}❌ FAIL{RESET} - {name}")
    return bool(condition)

def main():
    ok = True

    # get_stock basics
    inv = {"A": 3}
    ok &= check("get_stock existing", get_stock("A", inv) == 3)
    ok &= check("get_stock missing", get_stock("X", inv) == 0)

    # has_sufficient_stock should require enough quantity
    inv = {"A": 1}
    cart = {"A": 2}
    ok &= check("has_sufficient_stock quantity-aware", has_sufficient_stock(cart, inv) is False)

    # deduct_stock should mutate inventory
    inv = {"A": 5, "B": 2}
    cart = {"A": 2, "B": 1}
    deduct_stock(cart, inv)
    ok &= check("deduct_stock A reduced", inv["A"] == 3)
    ok &= check("deduct_stock B reduced", inv["B"] == 1)

    # place_order should be all-or-nothing
    inv = {"A": 3, "B": 1}
    cart_ok = {"A": 1, "B": 1}
    res_ok = place_order(cart_ok, inv)
    ok &= check("place_order ok flag", res_ok.get("ok") is True)
    ok &= check("place_order totals", res_ok.get("total_items") == 2)
    ok &= check("place_order inventory updated A", inv["A"] == 2)
    ok &= check("place_order inventory updated B", inv["B"] == 0)

    before = dict(inv)
    cart_bad = {"A": 5}
    res_bad = place_order(cart_bad, inv)
    ok &= check("place_order rejects insufficient", res_bad.get("ok") is False)
    ok &= check("place_order no partial changes", inv == before)

    sys.exit(0 if ok else 1)

if __name__ == "__main__":
    main()
