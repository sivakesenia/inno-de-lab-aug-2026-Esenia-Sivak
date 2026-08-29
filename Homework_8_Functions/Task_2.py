from typing import Callable, Any
import time

# module-level constants
PERFORMANCE_LOG_PREFIX = "[PERF_LOG]"
TIME_DECIMALS = 8


def performance_logger(func: Callable) -> Callable:
    """
    Decorator that measures and logs the execution time of the wrapped function

    Args:
        func (Callable): The function to be wrapped and measured

    Returns:
        Callable: Wrapped function that logs performance metrics
    """

    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start_time = time.perf_counter()
        result = func(*args, **kwargs)

        # calculate execution time
        elapsed_time = time.perf_counter() - start_time

        print(
            f"{PERFORMANCE_LOG_PREFIX} Function '{func.__name__}' executed in {elapsed_time:.{TIME_DECIMALS}f} sec."
        )

        # return the result of the original function
        return result

    return wrapper


@performance_logger
def get_sorted_report(
    sales_data: list[dict[str, str | float]],
) -> list[dict[str, str | float]]:
    """
    Sorts genre sales data by total_sales in descending order

    Args:
        sales_data (list[dict[str, str | float]]): list of dictionaries where each
            dictionary contains:
            - "category" (str): genre name
            - "total_sales" (float): total revenue for that genre

    Returns:
        list[dict[str, str | float]]: a new list sorted by total_sales descending

    """
    # sort by total_sales in descending order
    return sorted(sales_data, key=lambda x: x["total_sales"], reverse=True)


# test
test_cases = [
    {
        "name": "TEST 1",
        "data": [
            {"category": "Action", "total_sales": 4311.85},
            {"category": "Animation", "total_sales": 4656.30},
            {"category": "Children", "total_sales": 3655.55},
        ],
    },
    {
        "name": "TEST 2",
        "data": [
            {"category": "Classics", "total_sales": 1200.10},
            {"category": "Comedy", "total_sales": 4000.00},
            {"category": "Documentary", "total_sales": 4000.00},
        ],
    },
    {"name": "TEST 3", "data": [{"category": "Drama", "total_sales": 500.00}]},
]

print("TESTING")

for test_case in test_cases:
    print(f"\n--- {test_case['name']} ---")

    sorted_report = get_sorted_report(test_case["data"])

    print("Top categories by revenue:")
    for idx, item in enumerate(sorted_report, 1):
        print(f"{idx}. {item['category']}: {item['total_sales']}")
