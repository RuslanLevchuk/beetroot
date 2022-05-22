import time

with open('new_red_apple.log', 'r') as file:
    lines = (i.replace(' - - ', ' ').replace('\n', '') for i in file)
    early_requests = [request for request in lines if time.strptime(request.split()[1][-8:-1], "%H:%M:%S") < time.strptime('12:00:00', "%H:%M:%S")]
    request_berfore_12 = len(early_requests)

    print(f"Requests berfore 12:00: {request_berfore_12}")


    #for line in early_requests:
     #b   print(line)