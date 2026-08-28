raw_transactions = [
    "SUCCESS:100",
    "FAILED:50",
    "SUCCESS:-10",
    "SUCCESS:0",
    "SUCCESS:250",
    "ERROR:200",
]

res = [
    int(amount)  # convert to int
    for item in raw_transactions
    if item.startswith("SUCCESS:")
    for amount in [
        item.split(":")[1]  # extracts the numeric value of the payment amount.
    ]  # filters out all transactions that do not have a SUCCESS status.
    if int(amount) > 0  # check for non-positive amount
]  # amount is used for not to use split 2 times
print(res)
