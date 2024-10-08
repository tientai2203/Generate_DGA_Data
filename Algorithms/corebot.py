import argparse
from datetime import datetime

def init_rand_and_chars(year, month, day, nr_b, r):
    r = (r + year + ((nr_b << 16) + (month << 8) | day)) & 0xFFFFFFFF
    charset = [chr(x) for x in range(ord("a"), ord("z"))] + [
        chr(x) for x in range(ord("0"), ord("9"))
    ]
    return charset, r

def generate_domain(charset, r):
    len_l = 0xC
    len_u = 0x18
    r = (1664525 * r + 1013904223) & 0xFFFFFFFF
    domain_len = len_l + r % (len_u - len_l)
    domain = ""
    for i in range(domain_len, 0, -1):
        r = ((1664525 * r) + 1013904223) & 0xFFFFFFFF
        domain += charset[r % len(charset)]
    domain += ".ddns.net"
    return domain, r

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--seed", help="seed", default="1DBA8930")
    parser.add_argument("-d", "--date", help="date for which to generate domains")
    parser.add_argument("-t", "--debug", help="debug DGA (day set to 8)")
    parser.add_argument(
        "-n", "--nr", help="nr of domains to generate", type=int, default=40
    )
    parser.add_argument("--output_file", help="output file name", default="domains.txt")
    args = parser.parse_args()

    d = datetime.strptime(args.date, "%Y-%m-%d") if args.date else datetime.now()
    day = 8 if args.debug else d.day

    charset, r = init_rand_and_chars(d.year, d.month, day, 1, int(args.seed, 16))
    #output_file == dga_data
    with open(args.output_file, "a") as file:
        for _ in range(args.nr):
            domain, r = generate_domain(charset, r)
            # print(domain)  # In domain ra console
            file.write(domain + "\n")  # Ghi domain vào file .txt
