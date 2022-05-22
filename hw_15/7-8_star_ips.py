with open('red_apple_2.log', 'r') as file:
    lines = (i.replace(' - - ', ' ') for i in file)
    ips = set(i.split()[0] for i in lines)
    print(f"total IP addresses: {len(ips)}")
    print(sorted(ips))