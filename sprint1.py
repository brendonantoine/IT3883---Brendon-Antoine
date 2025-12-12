

#Coin Mapping
COINS = {
    "penny": 0.01,
    "pennies": 0.01,
    "nickel": 0.05,
    "nickels": 0.05,
    "dime": 0.10,
    "dimes": 0.10,
    "quarter": 0.25,
    "quarters": 0.25
}


def parse_sentence(sentence: str) -> float:
    """
    Takes a sentence like '1 penny and 2 nickels'
    and returns the total value as a float (dollars).
    """
    # Normalize text
    sentence = sentence.strip().lower()

    # Split into groups on ' and '
    groups = sentence.split(" and ")

    total_value = 0.0

    for group in groups:
        group = group.strip()
        if not group:
            continue  

        parts = group.split()

        quantity_str = parts[0]
        denomination = parts[1]

        quantity = int(quantity_str)
        
        coin_value = COINS[denomination]

        total_value += quantity * coin_value

    return total_value


def main():
    # Read user sentence
    sentence = input().strip()

    amount = parse_sentence(sentence)

    # Print output to 2 decimal places
    print(f"{amount:.2f}")

if __name__ == "__main__":
    main()
