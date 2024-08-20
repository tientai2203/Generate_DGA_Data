import json
import numpy as np

# Đọc dữ liệu từ file JSON
with open("clients_data_matrix.json", "r") as f:
    rounds_data_dict = json.load(f)

# print(rounds_data_dict["client1"])
# print(type(rounds_data_dict["client1"]))
# Số lượng rounds
num_rounds = 50

# Số lượng clients
num_clients = 8

# Số lượng nhãn (label)
num_labels = 10

for i in range(1, num_clients + 1):
    print(f"Client{i}:\n")
    client_data = rounds_data_dict[f"client{i}"] # duyet qua tung client
    for j in range(num_rounds):
        print(f"Round{j}:")
        print(client_data[j])

