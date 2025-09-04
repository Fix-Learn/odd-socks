# 🐛 Fix and Learn — Odd Socks challenges repository

Welcome to **Fix and Learn**, a collection of coding simulations where you practice solving real-world style bugs inside different business domains (ecommerce, fintech, booking apps, etc.).

Each repository represents a **self-contained challenge** with broken or poorly written code.
Your mission: **analyze, fix, and improve the codebase while thinking like a product-minded developer**.

---

## 🎯 Goal of this repo

This repository is part of the **Fix and Learn challenge series**.Here you will:

- Work with buggy or incomplete Python code that simulates a real business scenario.
- Practice debugging, refactoring, and writing cleaner solutions.
- Learn how coding decisions affect the business context (e.g., overselling stock, miscalculating discounts, etc.).
- Build the habit of **thinking beyond syntax** and focusing on how code supports the product.

---

## 📂 Repository structure

- `bug-XX-challenge-name/`
  - `challenge.py` → Buggy/bad-practice code for this challenge.
  - `verify.py` → Lightweight script to validate your fix (prints PASS/FAIL).
  - `__pycache__/` → Auto-generated Python cache files (can be ignored).
- `.gitignore` → Specifies files and folders Git should ignore.
- `LICENSE` → License information for this repository.
- `README.md` → General context, story, and instructions.

---

## 🚀 How to work on the challenge

1. Read the **Story / Context** section in the README inside each challenge.
2. Explore the code in `challenge.py`.
3. Run the validator with:
   ```bash
   python verify.py
   ```
