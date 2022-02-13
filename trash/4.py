#Task_1
while 1:
    str = input("Input your string (type 'q' to quit): ")
    if str == 'q':
        print("Good luck!")
        break
    elif len(str) < 2:
        print("Empty string")
    else:
        print(str[:2] + str[-2:])


#Task_2
while 1:
    nmbr = input("Type phone number to analyse (type 'q' to quit): ")
    if nmbr == 'q':
        print("Good luck!")
        break
    elif nmbr.isdigit():
        if len(nmbr) == 10:
            print('Phone number is valid')
        else:
            if len(nmbr) > 10:
                print('Phone number is too long, type again')
            else:
                print('Phone number is too short, type again')
    else:
        print("Must be only digits! Type again!")

        
#Task_3
name = 'ruslan'
while 1:
    nm = input("Input my name (type 'q' to quit): ")
    if nm == 'q':
        print("Good luck!")
        break
    elif nm.lower() == name:
        print("True")
    else:
        print("False")