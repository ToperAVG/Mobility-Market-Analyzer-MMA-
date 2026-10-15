import json
import os

FILENAME = "expenses.json"

def load_expenses():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_expenses(expenses):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(expenses, f, ensure_ascii=False, indent=2)

def main():
    expenses = load_expenses()
    print("--- Трекер витрат ---")
    title = input("Введіть назву витрати: ")
    amount = float(input("Введіть суму: "))

    expenses.append({"title": title, "amount": amount})
    save_expenses(expenses)

    total = sum(item["amount"] for item in expenses)
    print(f"Загальна сума витрат: {total:.2f}")

if __name__ == "__main__":
    main()