import numpy as np
import json

# Đặt seed để đảm bảo tính tái lập
np.random.seed(42)

# Số lượng rounds
num_rounds = 50

# Số lượng clients
num_clients = 8

# Số lượng nhãn (label)
num_labels = 10

# Số lượng mẫu cho mỗi client
samples_per_client = 200

# Tham số alpha cho phân phối Dirichlet
alpha = [0.5] * num_labels

# Tạo dictionary để lưu 50 ma trận phân phối dữ liệu
rounds_data_dict = {}

# Sinh dữ liệu cho mỗi round
for round_idx in range(1, num_rounds + 1):
    client_data_matrix = np.zeros((num_clients, num_labels), dtype=int)
    
    for i in range(num_clients):
        label_distribution = np.random.dirichlet(alpha)
        label_data_count = np.round(label_distribution * samples_per_client).astype(int)
        label_data_count[-1] += samples_per_client - np.sum(label_data_count)
        client_data_matrix[i, :] = label_data_count
    
    # Lưu ma trận của round hiện tại vào dictionary
    rounds_data_dict[f'round{round_idx}'] = client_data_matrix.tolist()

# Lưu các ma trận vào file JSON
with open("rounds_data_matrix.json", "w") as f:
    json.dump(rounds_data_dict, f, indent=4)

print("Đã lưu 50 ma trận vào file 'rounds_data_matrix.json'.")
