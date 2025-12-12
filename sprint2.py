#Coin mapping
COINS = {
    "penny": 1,
    "pennies": 1,
    "nickel": 5,
    "nickels": 5,
    "dime": 10,
    "dimes": 10,
    "quarter": 25,
    "quarters": 25
}


def parse_sentence(sentence: str) -> int:
    """
    Takes a sentence like '1 penny and 2 nickels'
    and returns the total value in cents (as an integer).
    This avoids floating point rounding errors.
    """
    # Normalize text
    sentence = sentence.strip().lower()

    # Split into groups on ' and '
    groups = sentence.split(" and ")

    total_value = 0  # now tracking total in cents

    for group in groups:
        group = group.strip()
        if not group:
            continue  

        parts = group.split()

        
        quantity_str = parts[0]
        denomination = parts[1]

        quantity = int(quantity_str)

        # Lookup coin value in cents
        coin_value = COINS[denomination]

        # Add to total 
        total_value += quantity * coin_value

    return total_value


def main():
    # Read user sentence
    sentence = input().strip()

    # Convert sentence to total cents
    total_cents = parse_sentence(sentence)

    # Convert cents to dollars 
    amount = total_cents / 100.0

    # Print output to 2 decimal places
    print(f"{amount:.2f}")


if __name__ == "__main__":
    main()
