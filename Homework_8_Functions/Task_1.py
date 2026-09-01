MAX_RENTAL_BATCH_LIMIT = 150.0  # global constant/ module-level constant


def calculate_rental_batch(
    quantity: int, rental_rate: float, discount: float = 0.0
) -> tuple[float, bool]:
    """
    Calculates the total cost of a rental batch with genre-based discount
    and checks if it exceeds the automatic approval limit

    Args:
        quantity (int): number of DVDs
        rental_rate (float): rental cost per DVD
        discount (float, dafault = 0.0): genre-based discount

    Returns:
        tuple[float, bool]:
            - final_sum (float): total batch cost rounded to 2 decimals
            - is_limit_exceeded (bool): True if final_sum > MAX_RENTAL_BATCH_LIMIT,
              False otherwise

    """
    final_sum = round(
        quantity * rental_rate * (1 - discount), 2
    )  # calculates the total cost and rounded to 2 decimals
    is_limit_exceeded = (
        final_sum > MAX_RENTAL_BATCH_LIMIT
    )  # check if it exceeds the automatic approval limit
    return final_sum, is_limit_exceeded


print("=== ОТЧЕТ ПО ПАРТИЯМ АРЕНДЫ ===")

# test 1
test1 = calculate_rental_batch(quantity=30, rental_rate=2.99)
print(f"Партия 1 (Academy Dinosaur): Сумма  ${test1[0]}. Превышение лимита: {test1[1]}")

# test 2
test2 = calculate_rental_batch(quantity=40, rental_rate=4.99, discount=0.1)
print(f"Партия 2 (Affair Prejudice): Сумма ${test2[0]}. Превышение лимита: {test2[1]}")

# test 3
test3 = calculate_rental_batch(quantity=10, rental_rate=1.99)
print(f"Партия 3 (Agent Truman): Сумма ${test3[0]}. Превышение лимита: {test3[1]}")

# test 4
test4 = calculate_rental_batch(quantity=50, rental_rate=3.50, discount=0.2)
print(f"Партия 4 (African Egg): Сумма ${test4[0]}. Превышение лимита: {test4[1]}")
