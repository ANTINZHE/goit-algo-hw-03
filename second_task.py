import random

def get_numbers_ticket(min: int, max: int, quantity: int) -> list:
    set_of_numbers = set()

    if min >= 1 and max < 1000 and max - min >= quantity:
        while len(set_of_numbers) < quantity:
            set_of_numbers.add(random.randint(min, max))

        list_of_numbers = list(set_of_numbers)
    else:
        list_of_numbers = []

    return sorted(list_of_numbers)

print(get_numbers_ticket(10, 26, 6))