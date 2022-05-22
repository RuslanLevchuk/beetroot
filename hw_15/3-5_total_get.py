with open('access-log', 'r') as file:
    lines = [i for i in file]
    
    gets = sum(1 for i in lines if i.rsplit(maxsplit=5)[1] == '"GET')
    print(f"Total GET requests: {gets}")

    posts_200 = sum(1 for i in lines if i.rsplit(maxsplit=5)[1] == '"POST' and i.rsplit(maxsplit=5)[4] == '200')
    print(f"Total POST requests with code 200: {posts_200}")

    posts_404 = sum(1 for i in lines if i.rsplit(maxsplit=5)[1] == '"POST' and i.rsplit(maxsplit=5)[4] == '404')
    print(f"Total POST requests with code 404: {posts_404}")

    gets_404 = sum(1 for i in lines if i.rsplit(maxsplit=5)[1] == '"GET' and i.rsplit(maxsplit=5)[4] == '404')
    print(f"Total GET requests with code 404: {gets_404}")