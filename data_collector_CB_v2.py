
import csv
import datetime as dt
import os


# =========================================================
# FILE
# =========================================================

FILENAME = "cb_data.csv"


# =========================================================
# AGE RANGES
# =========================================================

age_ranges = {
    "1": "10-19",
    "2": "20-29",
    "3": "30-39",
    "4": "40-49",
    "5": "50-59",
    "6": "60-69",
    "7": "70+"
}


# =========================================================
# CONTENT PURCHASED
# =========================================================

content_options = {
    "1": "coffee",
    "2": "espresso",
    "3": "latte",
    "4": "americano",
    "5": "mocha",
    "6": "cappuccino",
    "7": "tea",
    "8": "iced_drink",
    "9": "food",
    "10": "pastry",
    "11": "sandwich",
    "12": "snack",
    "13": "dessert",
    "14": "breakfast",
    "15": "non_coffee_drink",
    "16": "water",
    "17": "juice",
    "18": None
}


# =========================================================
# CASUAL ATTIRE
# =========================================================

casual_attire_options = {
    "1": "recreational",
    "2": "workout",
    "3": "pajamas",
    "4": "leisure",
    "5": "streetwear",
    "6": "outdoor",
    "7": "fashion_casual",
    "8": "casual_other"
}


# =========================================================
# NON-CASUAL ATTIRE
# =========================================================

noncasual_attire_options = {
    "1": "business_professional",
    "2": "business_casual",
    "3": "medical",
    "4": "work_uniform",
    "5": "law_enforcement",
    "6": "formal",
    "7": "school_academic",
    "8": "religious_ceremonial",
    "9": "noncasual_other"
}


# =========================================================
# OCCUPATION
# =========================================================

occupation_options = {
    "1": "construction",
    "2": "business",
    "3": "medical",
    "4": "law_enforcement",
    "5": "student",
    "6": "trades",
    "7": "education",
    "8": "hospitality",
    "9": "retail",
    "10": "office",
    "11": "unemployed",
    "12": None
}


# =========================================================
# DEVICE
# =========================================================

device_options = {
    "1": "computer",
    "2": "tablet",
    "3": "phone",
    "4": None
}


# =========================================================
# WRITE DATA
# =========================================================


def write_data(filename, data):

    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:

        writer = csv.writer(file)

        if not file_exists:
            writer.writerow([
                "day_of_week",
                "arrival_time",
                "age_range",
                "sex_male",
                "content_purchased",
                "attire_casual",
                "attire_type",
                "occupation",
                "dine_in",
                "device_type"
            ])

        # Convert None values to "None" so they don't create
        # empty-looking fields in the CSV.
        cleaned_data = [
            "None" if value is None else value
            for value in data
        ]

        writer.writerow(cleaned_data)


# =========================================================
# DISPLAY FUNCTIONS
# =========================================================

def show_menu(title, options):

    print()
    print(f"--- {title} ---")

    for key, value in options.items():

        if value is None:
            display_value = "None"
        else:
            display_value = value.replace("_", " ").title()

        print(f"  [{key}] {display_value}")

    print()


def get_menu_choice(prompt, options):

    while True:

        choice = input(prompt).strip().lower()

        if choice in options:
            return options[choice]

        print("  Invalid choice. Try again.")


def get_true_false(prompt):

    while True:

        answer = input(prompt).strip().upper()

        if answer == "T":
            return True

        if answer == "F":
            return False

        print("  Enter T or F.")


# =========================================================
# MAIN DATA COLLECTION
# =========================================================

while True:

    print()
    print("=" * 55)
    print("              NEW CUSTOMER")
    print("=" * 55)
    print("  Press Q at the age prompt to quit.")
    print("=" * 55)


    # -----------------------------------------------------
    # Automatically record time
    # -----------------------------------------------------

    now = dt.datetime.now()

    day_of_week = now.strftime("%A")
    arrival_time = now.strftime("%H:%M")


    # -----------------------------------------------------
    # AGE
    # -----------------------------------------------------

    show_menu("AGE RANGE", age_ranges)

    while True:

        age_input = input("Age: ").strip().lower()

        if age_input == "q":
            print()
            print("Data collection ended.")
            exit()

        if age_input in age_ranges:
            age_range = age_ranges[age_input]
            break

        print("  Enter a number from 1-7.")


    # -----------------------------------------------------
    # SEX
    # -----------------------------------------------------

    sex_male = get_true_false(
        "Male? [T/F]: "
    )


    # -----------------------------------------------------
    # CONTENT PURCHASED
    # -----------------------------------------------------

    show_menu("CONTENT PURCHASED", content_options)

    content_purchased = get_menu_choice(
        "Purchase: ",
        content_options
    )


    # -----------------------------------------------------
    # ATTIRE
    # -----------------------------------------------------

    attire_casual = get_true_false(
        "Casual attire? [T/F]: "
    )


    # -----------------------------------------------------
    # ATTIRE TYPE
    # -----------------------------------------------------

    if attire_casual:

        show_menu(
            "CASUAL ATTIRE TYPE",
            casual_attire_options
        )

        attire_type = get_menu_choice(
            "Attire: ",
            casual_attire_options
        )

    else:

        show_menu(
            "NON-CASUAL ATTIRE TYPE",
            noncasual_attire_options
        )

        attire_type = get_menu_choice(
            "Attire: ",
            noncasual_attire_options
        )


    # -----------------------------------------------------
    # OCCUPATION
    # -----------------------------------------------------

    show_menu("OCCUPATION", occupation_options)

    occupation = get_menu_choice(
        "Occupation: ",
        occupation_options
    )


    # -----------------------------------------------------
    # DINE IN
    # -----------------------------------------------------

    dine_in = get_true_false(
        "Dine in? [T/F]: "
    )


    # -----------------------------------------------------
    # DEVICE
    # -----------------------------------------------------

    if dine_in:

        show_menu("DEVICE", device_options)

        device_type = get_menu_choice(
            "Device: ",
            device_options
        )

    else:

        device_type = None


    # =====================================================
    # CREATE CUSTOMER RECORD
    # =====================================================

    data = [
        day_of_week,
        arrival_time,
        age_range,
        sex_male,
        content_purchased,
        attire_casual,
        attire_type,
        occupation,
        dine_in,
        device_type
    ]


    # =====================================================
    # SAVE CUSTOMER
    # =====================================================

    write_data(FILENAME, data)


    # =====================================================
    # CONFIRMATION
    # =====================================================

    print()
    print("-" * 55)
    print("             CUSTOMER RECORDED")
    print("-" * 55)

    print(f"  Time:       {day_of_week}, {arrival_time}")
    print(f"  Age:        {age_range}")
    print(f"  Male:       {sex_male}")
    print(f"  Purchase:   {content_purchased or 'None'}")
    print(f"  Casual:     {attire_casual}")
    print(f"  Attire:     {attire_type.replace('_', ' ').title()}")
    print(f"  Occupation: {occupation or 'None'}")
    print(f"  Dine in:    {dine_in}")
    print(f"  Device:     {device_type or 'None'}")

    print("-" * 55)
    print("  Ready for next customer.")
    print("=" * 55)

