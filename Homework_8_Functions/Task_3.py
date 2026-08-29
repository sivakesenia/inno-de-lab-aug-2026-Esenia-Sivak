from typing import Any

# module-level constant
DEFAULT_RETURN_INDEX_BASE = 10.0


def calculate_overdue_fine(
    days_overdue: Any, fine_rate: float, movie_name: str
) -> tuple[float, float] | None:
    """
    Safely calculates overdue fine and return index with error handling

    Args:
        days_overdue (Any): raw input data representing overdue days
        fine_rate (float): cost per overdue day in dollars

    Returns:
        tuple[float, float] | None: a tuple containing:
            - total_fine (float): total fine amount
            - return_index (float): return index

    """
    try:
        numeric_days = float(days_overdue)  # convert to float
        total_fine = numeric_days * fine_rate  # calculate total fine

        return_index = (
            DEFAULT_RETURN_INDEX_BASE / numeric_days
        )  # calculate return index

        return (total_fine, return_index)

    # errors
    except TypeError as e:
        print(f"[TYPE ERROR] Invalid data type for {movie_name}: {e}")
    except ValueError as e:
        print(f"[VALUE ERROR] Cannot convert days to number for {movie_name}: {e}")
    except ZeroDivisionError as e:
        print(f"[ZERO DIVISION ERROR] Return without overdue for {movie_name}: {e}")

    finally:
        print("\n--- Return transaction check completed ---")
    return None


# test
test_cases = [
    {"movie": "Matrix", "days_overdue": 5, "fine_rate": 1.5, "expected_success": True},
    {
        "movie": "Inception",
        "days_overdue": "пять",
        "fine_rate": 2.0,
        "expected_success": False,
    },
    {"movie": "Avatar", "days_overdue": 0, "fine_rate": 2.5, "expected_success": False},
    {
        "movie": "Interstellar",
        "days_overdue": [
            3,
        ],
        "fine_rate": 3.0,
        "expected_success": False,
    },
]

print("TESTING")

for test in test_cases:
    print(f"\nFilm: '{test['movie']}'")

    result = calculate_overdue_fine(
        test["days_overdue"], test["fine_rate"], test["movie"]
    )

    if result is not None:
        total_fine, return_index = result
        print(f"Total fine:  {total_fine}$ Index: {return_index}")
