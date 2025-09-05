# 🛒 BUG #1: Inventory not reduced after checkout

## 📖 Context

**Reported by:** Customer Support

Customer Support reported overselling cases:

Products marked as “In Stock” were sold multiple times, even when only 1 unit was available.
Warehouse records showed no stock reduction after customers placed orders.

**Expected:**
When an order is placed, inventory for each product (SKU) should decrease by the ordered quantity.
If any item cannot be fulfilled, the order should be rejected and the inventory left unchanged.

**Actual:**
Orders complete successfully, but stock in memory remains the same, allowing overselling.

## ✅ Prerequisites

To complete this challenge, you should be comfortable with:
- **Functions** in Python.
- **Dictionaries (`dict`)** and mutability.
- **Control flow:** if/else, loops.
- Understanding how to update state inside data structures.
- Running a script and reading console output (`print()`, `python verify.py`).

## 📝 Task instructions

Your mission is to fix and refactor the code in `challenge.py` so that inventory management behaves correctly.

- **Investigate** why stock levels don’t change after orders.
- **Fix** `has_sufficient_stock` so it checks **quantities**, not just existence.
- **Fix** `deduct_stock` so it properly updates inventory state.
- **Refactor** into small, reusable helpers (e.g., `validate_cart`, `update_inventory`) if needed.
- Ensure **all-or-nothing logic**: If any SKU lacks stock, reject the order and do **not** partially update inventory.

Remember:

- ✅ Write code that is simple, clear, and testable.
- ❌ Don’t hardcode values or bypass the validator.

## 🚀 How to Run

You can run this challenge directly in your browser using **GitHub Codespaces**.  
To make it work, follow these steps:
1. Open the repository in GitHub.  
2. Click the **Code** button → Click on **Codespaces tab**
3. To load the challenge you want to work on, create a Codespace for the specific challenge directory by following the steps below.

   ![create codespace](https://github.com/user-attachments/assets/692085fe-c46d-4be5-8ca5-5156576f9ece)
 
4. Wait for the environment to load, then start working.

Alternatively, you can clone this repo locally:
```bash
git clone https://github.com/Fix-Learn/odd-socks.git
cd odd-socks/bug-01-inventory-checkout
python verify.py
```

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

## 🚀 Keep learning with Fix & Learn
Enjoyed this exercise?
Every week we share a new real-world style bug + fix so you can practice not just coding,
but also thinking like a product-minded developer.

👉 Subscribe to Fix & Learn and get these interactive cases delivered straight to you.
Stay sharp, build better skills, and have fun while learning!

🔗 [Subscribe here](https://dub.sh/lmZT4GP)

See you next week, Fixer! 🛠️✨
