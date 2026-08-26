db_config = {
    "connection": {"host": "production-db.internal", "port": 5432, "user": "postgres"}
}

# 1 subpoint
connection_host = db_config["connection"]["host"]
connection_port = db_config["connection"]["port"]
print(
    f"Host name: {connection_host}, port: {connection_port}"
)  # extract the host and port values

# 2 subpoint
ssl_check = db_config.get("ssl_settings", {}).get(
    "ssl_mode", "verify-full"
)  # use of get()
print(f"SSL Mode: {ssl_check}")

# other
db_config["connection"]["user"] = "admin"  # change the value
db_config["connection"]["max_connections"] = 100  # add the value

for key, value in db_config["connection"].items():
    print(f"* {key}: {value}")  # iteration
