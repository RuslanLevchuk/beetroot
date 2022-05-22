with open('access-log', 'r') as file:
    lines = [i for i in file]

    gets_200 = sum(1 for i in lines if i.rsplit(maxsplit=5)[1] == '"GET' and i.rsplit(maxsplit=5)[4] == '200')
    bytes_get_200 = sum(int(i.rsplit(maxsplit=5)[5]) for i in lines if i.rsplit(maxsplit=5)[1] == '"GET' and i.rsplit(maxsplit=5)[4] == '200')
    print("Average bytes in GET request with code 200: {:.0f}".format(bytes_get_200/gets_200))


    gets_404 = sum(1 for i in lines if i.rsplit(maxsplit=5)[1] == '"GET' and i.rsplit(maxsplit=5)[4] == '404')
    bytes_get_404 = sum(int(i.rsplit(maxsplit=5)[5]) for i in lines if i.rsplit(maxsplit=5)[1] == '"GET' and i.rsplit(maxsplit=5)[4] == '404')
    print("Average bytes in GET request with code 404: {:.0f}".format(bytes_get_404/gets_404))