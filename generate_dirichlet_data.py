import random
import numpy as np
import argparse
import json
import sys



def corebot(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'corebot'
   
    for i in range(1, number_file+1):
        n = random.randint(1, 28)
        m = random.randint(1, 12)
        y = random.randint(1000, 5000)
        command = f'python {type_dga}.py -s {n} -d "{y}-{m}-{n}" -n {number_of_sample} --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)

def dircypt(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'dircrypt'
    
    for i in range(1,number_file+1):
        n = random.randint(432, 9348)
        command = f'python {type_dga}.py {n} -n {number_of_sample} --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)

def dnschanger(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'dnschanger'
    for i in range (1, number_file+1):
        n = random.randint(432, 9348)
        command = f'python {type_dga}.py {n} -n {number_of_sample} --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)

def fobber(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'fobber'
    # print(f'mkdir {client_id}\\{type_dga}')
    for i in range(1,number_file+1):
        n = random.randint(1, 2)
        command = f'python {type_dga}.py {n} -n {number_of_sample} --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)
        
def newgoz(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'newgoz'
    for i in range (1,number_file+1):
        command = f'python {type_dga}.py -n {number_of_sample} --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)

def necurs(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'necurs'
    for i in range(1,number_file+1):
        n = random.randint(1,28)
        m = random.randint(1, 12)
        y = random.randint(1000, 5000)
        command = f'python {type_dga}.py -n {number_of_sample} -d "{y}-{m}-{n}" --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)

def ramnit(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'ramnit'
    for i in range (1,number_file+1):
        n = random.randint(56, 230928)
        tail_list = ['.com', '.net','.org']
        tail = random.choice(tail_list)
        command = f'python {type_dga}.py {n} -n {number_of_sample} -t {tail} --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)

def rambo(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'rambo'
    for i in range(1,number_file+1):
        command = f'python {type_dga}.py -n {number_of_sample} --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)
        
def qakbot(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'qakbot'
    for i in range (1,number_file+1):
        n = random.randint(1,28)
        m = random.randint(1, 12)
        y = random.randint(1000, 5000)
        x = random.randint(0,1)
        command = f'python {type_dga}.py -n {number_of_sample} --date "{y}-{m}-{n}" --seed {x} --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)

def banjori(number_of_sample, number_file, type_dga, machine, file_handle):
    type_dga = 'banjori'
 
    for i in range(1,number_file+1):
        command = f'python {type_dga}.py -n {number_of_sample} --output_file {machine}_dga_malware.txt\n'
        file_handle.write(command)



def generate_samples_for_clients(number_of_sample, number_file, dga_labels, machine):
    with open("generated_commands.sh", "a") as f:
        for label in dga_labels:
            if label == 'corebot':
                corebot(number_of_sample, number_file, label, machine, f)
            elif label == 'dircrypt':
                dircypt(number_of_sample, number_file, label, machine, f)
            elif label == 'dnschanger':
                dnschanger(number_of_sample, number_file, label, machine, f)
            elif label == 'fobber':
                fobber(number_of_sample, number_file, label, machine, f)
            elif label == 'necurs':
                necurs(number_of_sample, number_file, label, machine, f)
            elif label == 'newgoz':
                newgoz(number_of_sample, number_file, label, machine, f)
            elif label == 'qakbot':
                qakbot(number_of_sample, number_file, label, machine, f)
            elif label == 'rambo':
                rambo(number_of_sample, number_file, label, machine, f)
            elif label == 'ramnit':
                ramnit(number_of_sample, number_file, label, machine, f)
            elif label == 'banjori':
                banjori(number_of_sample, number_file, label, machine, f)

    
if __name__ == "__main__":

    # Số lượng rounds
    num_rounds = 50
    # Số lượng clients
    num_clients = 8
    # Số lượng nhãn (label)
    num_labels = 10
    # Đọc dữ liệu từ file JSON
    with open("clients_data_matrix.json", "r") as f:
        rounds_data_dict = json.load(f)

    dga_labels = ['corebot', 'dircrypt', 'dnschanger', 'fobber', 'necurs', 'newgoz', 'qakbot', 'rambo', 'ramnit', 'banjori',]
    
    # Kiểm tra xem số lượng loại DGA có khớp với kích thước của mảng `data` không
    num_dga_labels = len(dga_labels)
    if num_labels != num_dga_labels:
        raise ValueError(f"Số lượng loại DGA ({num_dga_labels}) không khớp với số lượng giá trị trong mảng `data` ({num_labels})")
    
    np.random.seed(0)

    parser = argparse.ArgumentParser(description='Test Algorithms.')
    parser.add_argument('--type', default='normal', type=str, help='choose type to generate scripts')
    parser.add_argument('--n', default='100', type=int, help='input number of sample for each file')
    parser.add_argument('--num_file', default='1', type=int, help='input number of file in each type data')
    parser.add_argument('--num_client', default=8, type=int, help='so luong client')
    args = parser.parse_args()

    num_file = args.num_file 
    num_clients = args.num_client
    # client_folder_name = "dga_data"

    # Redirect stdout to a file
    sys.stdout = open("generated_commands.sh", "a")

    
    # Sinh dữ liệu cho từng loại DGA với số lượng mẫu cụ thể
    for i in range(1, num_clients + 1): # duyet qua tung client
        # print(f"Client{i}:\n")
        client_data = rounds_data_dict[f"client{i}"] 
        for j in range(num_rounds): # duyet qua tung round
            data = client_data[j] # mang data cua round j
            for k, label in enumerate(dga_labels): 
                number_of_sample = data[k]  # Lấy số lượng mẫu tương ứng với loại DGA
                if number_of_sample > 0:  # Chỉ sinh dữ liệu nếu số lượng mẫu lớn hơn 0
                    generate_samples_for_clients(number_of_sample, num_file, [label], f"machine{i}")

    # Close the file
    sys.stdout.close()


