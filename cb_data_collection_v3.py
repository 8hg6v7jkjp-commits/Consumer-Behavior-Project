
import csv
import datetime as dt
from dataclasses import asdict, dataclass
from pathlib import Path

import questionary


FILENAME = Path("cb_data.csv")


# =========================================================
# OPTIONS
# =========================================================

AGE_RANGES = [
    "10-19",
    "20-29",
    "30-39",
    "40-49",
    "50-59",
    "60-69",
    "70+",
]

SEXES = [
    "male",
    "female",
]

ATTIRE = [
    "recreational",
    "workout",
    "pajamas",
    "leisure",
    "streetwear",
    "outdoor",
    "fashion_casual",
    "casual_other",
    "business_professional",
    "business_casual",
    "medical",
    "work_uniform",
    "law_enforcement",
    "formal",
    "school_academic",
    "religious_ceremonial",
    "noncasual_other",
]

ORDERS = [
    "coffee",
    "espresso",
    "latte",
    "americano",
    "mocha",
    "cappuccino",
    "tea",
    "iced_drink",
    "food",
    "pastry",
    "sandwich",
    "snack",
    "dessert",
    "breakfast",
    "non_coffee_drink",
    "water",
    "juice",
    "None",
]


# =========================================================
# DATA MODEL
# =========================================================

@dataclass
class Customer:
    time: str
    day: str
    age: str
    sex: str
    attire: str
    order: str


# =========================================================
# QUESTIONARY
# =========================================================

def display_name(value: str) -> str:
    """Make snake_case values readable."""

    return value.replace("_", " ").title()


def select(question: str, options: list[str]) -> str:
    """Display a keyboard-navigable selection menu."""

    answer = questionary.select(
        question,
        choices=[display_name(option) for option in options],
    ).ask()

    return answer.lower().replace(" ", "_")


# =========================================================
# DATA COLLECTION
# =========================================================

def collect_customer() -> Customer:
    """Collect one customer's information."""

    now = dt.datetime.now()

    return Customer(
        time=now.strftime("%H:%M"),
        day=now.strftime("%A"),
        age=select("Age:", AGE_RANGES),
        sex=select("Sex:", SEXES),
        attire=select("Attire:", ATTIRE),
        order=select("Order:", ORDERS),
    )


# =========================================================
# CSV
# =========================================================

def save_customer(customer: Customer) -> None:
    """Append a customer to the CSV file."""

    file_exists = FILENAME.exists()

    with FILENAME.open("a", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=asdict(customer).keys(),
        )

        if not file_exists:
            writer.writeheader()

        writer.writerow(asdict(customer))


# =========================================================
# DISPLAY
# =========================================================

def print_customer(customer: Customer) -> None:
    """Display the recorded customer."""

    print()
    print("-" * 40)
    print("       CUSTOMER RECORDED")
    print("-" * 40)

    print(f"  Time:   {customer.time}")
    print(f"  Day:    {customer.day}")
    print(f"  Age:    {customer.age}")
    print(f"  Sex:    {display_name(customer.sex)}")
    print(f"  Attire: {display_name(customer.attire)}")
    print(f"  Order:  {display_name(customer.order)}")

    print("-" * 40)


# =========================================================
# MAIN
# =========================================================

def main() -> None:
    """Run the customer data collection program."""

    print("=" * 40)
    print("       CUSTOMER DATA COLLECTION")
    print("=" * 40)

    while True:
        customer = collect_customer()

        save_customer(customer)
        print_customer(customer)

        if not questionary.confirm("Record another customer?").ask():
            break

    print("\nData collection ended.")


if __name__ == "__main__":
    main()

