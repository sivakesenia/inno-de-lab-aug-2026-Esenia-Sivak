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
        movie_name(str): original name of movie

    Returns:
        tuple[float, float] | None: a tuple containing:
            - total_fine (float): total fine amount
            - return_index (float): return index

    Errors:
        - TypeError: invalid data type
        - ValueError: days_overdue cannot be converted to a number
        - ZeroDivisionError: days_overdue is zero

    """
    try:
        numeric_days = float(days_overdue)  # convert to float
        total_fine = numeric_days * fine_rate  # calculate total fine

        return_index = (
            DEFAULT_RETURN_INDEX_BASE / numeric_days
        )  # calculate return index
        print(
            f"Фильм: '{test['movie']}' | Итоговый штраф:  {total_fine}$ | Индекс: {return_index}"
        )
        return (total_fine, return_index)

    # errors
    except TypeError as e:
        print(f"[ОШИБКА ТИПА] Некорректный тип данных для " f"'{movie_name}': {e}")
    except ValueError as e:
        print(
            f"[ОШИБКА ЗНАЧЕНИЯ] Невозможно преобразовать дни в число "
            f"для '{movie_name}': {e}"
        )
    except ZeroDivisionError as e:
        print(
            f"[ОШИБКА ДЕЛЕНИЯ НА НОЛЬ] Возврат без просрочки "
            f"для '{movie_name}': {e}"
        )

    finally:
        print("\n--- Проверка транзакции возврата завершена ---\n")
    return None


# test
test_cases = [
    {"movie": "Matrix", "days_overdue": 5, "fine_rate": 1.5},
    {"movie": "Inception", "days_overdue": "пять", "fine_rate": 2.0},
    {"movie": "Avatar", "days_overdue": 0, "fine_rate": 2.5},
    {
        "movie": "Interstellar",
        "days_overdue": [
            3,
        ],
        "fine_rate": 3.0,
    },
]

print("=== ПРОВЕРКА ВОЗВРАТОВ ===\n")

for test in test_cases:

    result = calculate_overdue_fine(
        test["days_overdue"], test["fine_rate"], test["movie"]
    )
