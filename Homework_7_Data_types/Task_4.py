# Список ролей, переданный в запросе на авторизацию (содержит повторы)
requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
# Набор обязательных ролей для выполнения административных функций
required_admin_roles = {"admin", "security_officer", "audit_manager"}

# convert the list to a set
req_roles = set(requested_roles)
print(f"Unique requested roles: {req_roles}")

# roles present in both sets
roles_intersection = req_roles.intersection(required_admin_roles)
print(f"Common roles: {roles_intersection}")

# required admin roles that were not requested (difference)
roles_diff = required_admin_roles.difference(req_roles)
print(f"Lacking admin roles: {roles_diff}")

# membership check using the `in` operator
has_security_officer = "security_officer" in req_roles
print(f"The role security_officer in request: {has_security_officer}")
