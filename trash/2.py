i = 0
multiple = int(input("Input you number: "))
multi_number = int(input("Input the number oo multiples to show: "))

while 1:
    i += 1
    if i % multiple == 0:
        print (i)
    if i/multiple == multi_number:
            break
