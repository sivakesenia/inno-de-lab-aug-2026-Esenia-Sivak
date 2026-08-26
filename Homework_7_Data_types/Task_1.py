# 1 subpoint
raw_user_record = " 10827 ; aLeXanDer_vLaDimiRov ; mInSk ; ACTIVE "
raw_user_record_reworked = raw_user_record.split(
    ";"
)  # split the string into individual elements

# 2 subpoint (decided not to create a bunch of different variable for new modified string, they are not needed in future)
raw_user_record_reworked = [
    el.strip() for el in raw_user_record_reworked
]  # strip each resulting element of whitespaces

# 3 subpoint
raw_user_record_reworked[0] = (
    f"UID-{raw_user_record_reworked[0]}"  # apply the UID- prefix to the user ID
)

# 4 subpoint
raw_user_record_reworked[1] = (
    raw_user_record_reworked[1].replace("_", " ").title()
)  # convert the username by replacing the underscore to the correct case

# 5 subpoint
raw_user_record_reworked[2] = raw_user_record_reworked[
    2
].upper()  # convert the city name to uppercase

# 6 subpoint
raw_user_record_reworked[3] = raw_user_record_reworked[
    3
].lower()  # convert the user status to lowercase

# 7 subpoint
res = " | ".join(raw_user_record_reworked)  # join all elements
print(f"Нормализованная запись: {res}")  # result
