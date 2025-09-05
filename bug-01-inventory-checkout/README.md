# 🛒 BUG #1: Inventory not reduced after checkout

## 📖 Context

The full issue description has been logged on GitHub Projects.
👉 [View the issue here](https://github.com/Fix-Learn/odd-socks/issues/1)

## 📝 Task instructions

Your mission is to fix and refactor the code in `challenge.py` so that inventory management behaves correctly.

- **Investigate** why stock levels don’t change after orders.
- **Fix** `has_sufficient_stock` so it checks **quantities**, not just existence.
- **Fix** `deduct_stock` so it properly updates inventory state.
- **Refactor** into small, reusable helpers (e.g., `validate_cart`, `update_inventory`) if needed.
- Ensure **all-or-nothing logic**: If any SKU lacks stock, reject the order and do **not** partially update inventory.

Remember:
✅ Write code that is simple, clear, and testable.
❌ Don’t hardcode values or bypass the validator.

## 🚀 How to work on this challenge

1. Open and read the code in `challenge.py`.Notice the intentional bugs and comments pointing you in the right direction.
2. Run the lightweight validator:

   ```bash
   python verify.py
   ```

   → You’ll see **PASS/FAIL** messages in green/red.

   Your goal: all checks must be  **PASS ✅** .
3. (Optional) Run the demo simulation:

   ```bash
   python challenge.py
   ```

   → This prints the  **inventory before and after an order** .

   With the bug, you’ll notice the stock never decreases (overselling).

   After your fix, the inventory should update correctly.

## 📤 Submission

When everything is working:

- Verify that `python verify.py` shows all **PASS ✅**.
- Submit your solution link via [this form](https://tally.so/r/fake-form-id).

## 💡 Why this matters

Fixing this bug is not only about Python dictionaries:

- It teaches you to **map real-world problems** (overselling) into code.
- You practice **state management** and **all-or-nothing logic**, both common in real ecommerce systems.
- You learn to **decompose problems** into smaller functions that can be tested in isolation.
