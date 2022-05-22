import time

with open('new_red_apple.log', 'r') as file:
    lines = (i.replace(' - - ', ' ').replace('\n', '') for i in file)
    early_requests = (request for request in lines if time.strptime(request.split()[1][-8:-1], "%H:%M:%S") < time.strptime('12:00:00', "%H:%M:%S"))
    request_berfore_12 = len(list(early_requests))
with open('new_red_apple.log', 'r') as file:
    request_after_12 = len(list(file))-request_berfore_12

print(f"Requests berfore 12:00: {request_berfore_12}")
print(f"Requests after 12:00: {request_after_12} ", end='')
if request_after_12 < request_berfore_12:
    print('and less than before 12:00')
else:
    print('and more than before 12:00')
