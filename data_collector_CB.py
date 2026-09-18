import csv
import datetime as dt
import os


# Age ranges
age_ranges = {
    1: "10-19",
    2: "20-29",
    3: "30-39",
    4: "40-49",
    5: "50-59",
    6: "60-69",
    7: "70+"
}


# Write data to CSV
def write_data(filename, data):
    file_exists = os.path.exists(filename)

    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Add headers if this is a new file
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

        writer.writerow(data)


# Customer data collection
while True:

    print("\n--- New Customer ---")
    print("Type Q at the age prompt to quit.")

    # Get time for this customer
    now = dt.datetime.now()

    day_of_week = now.strftime("%A")
    arrival_time = now.strftime("%H:%M")


    # Age range
    while True:
        age_input = input("Age Range (1-7): ").strip().lower()

        # Exit before starting a new customer
        if age_input == "q":
            print("Data collection ended.")
            exit()

        try:
            age = int(age_input)

            if age in age_ranges:
                age_range = age_ranges[age]
                break
            else:
                print("Enter a number from 1-7.")

        except ValueError:
            print("Enter a number from 1-7.")


    # Sex
    while True:
        sex_male = input("Male? (T/F): ").strip().upper()

        if sex_male == "T":
            sex_male = True
            break
        elif sex_male == "F":
            sex_male = False
            break
        else:
            print("Enter T or F.")



    # Content Purchased
    content_options = {
        "c": "coffee",
        "coffee": "coffee",

        "e": "espresso",
        "espresso": "espresso",

        "l": "latte",
        "latte": "latte",

        "a": "americano",
        "americano": "americano",

        "m": "mocha",
        "mocha": "mocha",

        "cap": "cappuccino",
        "cappuccino": "cappuccino",

        "b": "tea",
        "tea": "tea",

        "i": "iced_drink",
        "iced_drink": "iced_drink",

        "f": "food",
        "food": "food",

        "p": "pastry",
        "pastry": "pastry",

        "s": "sandwich",
        "sandwich": "sandwich",

        "sn": "snack",
        "snack": "snack",

        "d": "dessert",
        "dessert": "dessert",

        "br": "breakfast",
        "breakfast": "breakfast",

        "n": "non_coffee_drink",
        "non_coffee_drink": "non_coffee_drink",

        "w": "water",
        "water": "water",

        "j": "juice",
        "juice": "juice",

        "none": None
    }

    while True:
        content_purchased = input(
            "Content Purchased "
            "(C)offee, (E)spresso, (L)atte, (A)mericano, "
            "(M)ocha, (Cap)puccino, (B)tea, (I)ced drink, "
            "(F)ood, (P)astry, (S)andwich, (Sn)nack, "
            "(D)essert, (Br)reakfast, (N)on-coffee drink, "
            "(W)ater, (J)uice, or none: "
        ).strip().lower()

        if content_purchased in content_options:
            content_purchased = content_options[content_purchased]
            break

        print("Enter a valid option or the full item name.")



    # Attire
    while True:
        attire_casual_input = input("Casual attire? (T/F): ").strip().upper()

        if attire_casual_input == "T":
            attire_casual = True
            break
        elif attire_casual_input == "F":
            attire_casual = False
            break
        else:
            print("Enter T or F.")


    # Casual attire type
    if attire_casual:

        casual_attire_options = {
            "r": "recreational",
            "recreational": "recreational",

            "w": "workout",
            "workout": "workout",
            "gym": "workout",

            "p": "pajamas",
            "pajamas": "pajamas",
            "sleepwear": "pajamas",

            "l": "leisure",
            "leisure": "leisure",
            "lounge": "leisure",
            "lounge_wear": "leisure",

            "s": "streetwear",
            "streetwear": "streetwear",

            "o": "outdoor",
            "outdoor": "outdoor",
            "outdoors": "outdoor",

            "f": "fashion_casual",
            "fashion": "fashion_casual",
            "fashion_casual": "fashion_casual",

            "n": "casual_other",
            "other": "casual_other"
        }

        while True:
            attire_type = input(
                "Casual attire type "
                "((R)ecreational, (W)orkout, (P)ajamas, "
                "(L)eisure, (S)treetwear, (O)utdoor, "
                "(F)ashion casual, (N)Other): "
            ).strip().lower()

            if attire_type in casual_attire_options:
                attire_type = casual_attire_options[attire_type]
                break

            print("Enter R, W, P, L, S, O, F, or N.")


    # Non-casual attire type
    else:

        noncasual_attire_options = {
            "b": "business_professional",
            "business": "business_professional",
            "business_professional": "business_professional",

            "a": "business_casual",
            "business_casual": "business_casual",

            "m": "medical",
            "medical": "medical",
            "scrubs": "medical",

            "u": "work_uniform",
            "uniform": "work_uniform",
            "work_uniform": "work_uniform",

            "l": "law_enforcement",
            "law": "law_enforcement",
            "law_enforcement": "law_enforcement",

            "f": "formal",
            "formal": "formal",

            "s": "school_academic",
            "school": "school_academic",
            "academic": "school_academic",

            "r": "religious_ceremonial",
            "religious": "religious_ceremonial",
            "ceremonial": "religious_ceremonial",

            "o": "noncasual_other",
            "other": "noncasual_other"
        }

        while True:
            attire_type = input(
                "Non-casual attire type "
                "((B)usiness professional, (A)Business casual, "
                "(M)edical, (U)niform, (L)aw enforcement, "
                "(F)ormal, (S)chool/academic, "
                "(R)eligious/ceremonial, (O)ther): "
            ).strip().lower()

            if attire_type in noncasual_attire_options:
                attire_type = noncasual_attire_options[attire_type]
                break

            print("Enter B, A, M, U, L, F, S, R, or O.")


    # Occupation
    occupation_options = {
        "c": "construction",
        "construction": "construction",

        "b": "business",
        "business": "business",

        "m": "medical",
        "medical": "medical",

        "l": "law_enforcement",
        "law": "law_enforcement",
        "law_enforcement": "law_enforcement",

        "s": "student",
        "student": "student",

        "t": "trades",
        "trades": "trades",

        "e": "education",
        "education": "education",

        "h": "hospitality",
        "hospitality": "hospitality",

        "r": "retail",
        "retail": "retail",

        "o": "office",
        "office": "office",

        "u": "unemployed",
        "unemployed": "unemployed",

        "n": None,
        "none": None
    }

    while True:
        occupation = input(
            "Occupation "
            "((C)onstruction, (B)usiness, (M)edical, "
            "(L)aw enforcement, (S)tudent, (T)rades, "
            "(E)ducation, (H)ospitality, (R)etail, "
            "(O)ffice, (U)n-employed, (N)one): "
        ).strip().lower()

        if occupation in occupation_options:
            occupation = occupation_options[occupation]
            break

        print("Enter a valid option or the full occupation.")


    # Dine in
    while True:
        dine_in = input("Dine in? (T/F): ").strip().upper()

        if dine_in == "T":
            dine_in = True
            break
        elif dine_in == "F":
            dine_in = False
            break
        else:
            print("Enter T or F.")


# Device
    if dine_in:
        device_options = {
            "c": "computer",
            "computer": "computer",
            "t": "tablet",
            "tablet": "tablet",
            "p": "phone",
            "phone": "phone",
            "n": None,
            "nothing": None
        }

        while True:
            device_type = input(
                "Device ((C)omputer, (T)ablet, (P)hone, (N)othing): "
            ).strip().lower()

            if device_type in device_options:
                device_type = device_options[device_type]
                break

            print("Enter C, T, P, N, or the full device name.")
    else:
        device_type = None


    # Create one complete customer record
    data = [
        day_of_week,
        arrival_time,
        age_range,
        sex_male,
        content_purchased,
        attire_casual,
        occupation,
        dine_in,
        device_type
    ]


    # Write the completed customer to CSV
    write_data("cb_data.csv", data)

    print("Customer recorded!")

    # Loop automatically starts the next customer

