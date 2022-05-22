with open('access-log', 'r') as file:
    lines = [i for i in file]
    byte_n_code = [(i.rsplit(maxsplit=2)[1], i.rsplit(maxsplit=2)[2]) for i in lines]
    total_bytes = (int(byte[1]) for byte in byte_n_code if byte[1].isdigit())
    total_bytes_200 = (int(byte[1]) for byte in byte_n_code if byte[1].isdigit() and byte[0].strip() == '200')
    total_bytes_404 = (int(byte[1]) for byte in byte_n_code if byte[1].isdigit() and byte[0].strip() == '404')

    print(f"Total bytes send: {sum(total_bytes)}")
    print(f"Bytes send with code 200: {sum(total_bytes_200)}")
    print(f"Bytes send with code 404: {sum(total_bytes_404)}")