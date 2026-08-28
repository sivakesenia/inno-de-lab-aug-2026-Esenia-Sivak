# Поток данных телеметрии от серверов кластера
system_telemetry = [
    ("srv_01", 12.5, 64, "online"),
    ("srv_02", 85.0, 92, "online"),
    ("srv_03", 0.0, 0, "offline"),
    ("srv_04", 45.2, 78, "online"),
    ("srv_05", 95.1, 99, "online"),
]

online_servers = [
    (node_name, cpu_load, ram_usage, status)
    for node_name, cpu_load, ram_usage, status in system_telemetry
    if status != "offline"
]  # 1 - unpacking + 2 - filter

# 3 - list of active services
active_server_names = [node_name for node_name, _, _, _ in online_servers]
print(f"Active services: {active_server_names}")

# 4 - metrics
total_servers = len(online_servers)
avg_cpu = round(
    sum(cpu_load for _, cpu_load, _, _ in online_servers) / total_servers, 2
)
max_ram = max(ram_usage for _, _, ram_usage, _ in online_servers)

# 5 - summary report
system_res = {
    "active_nodes_count": total_servers,
    "metrics": {"average_cpu": avg_cpu, "max_ram": max_ram},
}

print(f"Summary report: {system_res}")
