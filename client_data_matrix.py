import json
import numpy as np

# Đọc dữ liệu từ file JSON
with open("rounds_data_matrix.json", "r") as f:
    rounds_data_dict = json.load(f)

# Số lượng rounds
num_rounds = 50

# Số lượng clients
num_clients = 8

# Số lượng nhãn (label)
num_labels = 10
# Tạo dictionary để lưu dữ liệu mới
clients_data_dict = {f'client{i + 1}': np.zeros((num_rounds, num_labels), dtype=int) for i in range(num_clients)}

# Chuyển đổi dữ liệu từ cấu trúc cũ sang cấu trúc mới
for round_idx, (round_name, matrix) in enumerate(rounds_data_dict.items()):
    # Kiểm tra kích thước của matrix
    if len(matrix) != num_clients or len(matrix[0]) != num_labels:
        raise ValueError(f"Ma trận cho {round_name} có kích thước không hợp lệ: {np.shape(matrix)}")
    
    for client_idx in range(num_clients):
        # Kiểm tra kích thước của dữ liệu cho từng client
        if len(matrix[client_idx]) != num_labels:
            raise ValueError(f"Dữ liệu cho client{client_idx + 1} trong {round_name} có kích thước không hợp lệ: {np.shape(matrix[client_idx])}")
        
        clients_data_dict[f'client{client_idx + 1}'][round_idx, :] = matrix[client_idx]

# Chuyển dữ liệu NumPy thành danh sách để lưu vào JSON
clients_data_dict = {key: value.tolist() for key, value in clients_data_dict.items()}

# Lưu dữ liệu mới vào file JSON
with open("clients_data_matrix.json", "w") as f:
    json.dump(clients_data_dict, f, indent=4)

print("Đã chuyển đổi và lưu dữ liệu vào file 'clients_data_matrix.json'.")
