#make infinity loop
while 1:
    amount = input("Type your number: ")
    #try to make value we get from user into integer
    try:
        amount = int(amount)
        #if input data >0 we raise value error to inform user that program needs only positive integer
        if amount < 0:
            raise ValueError
        print([(i, i*i) for i in range(1, amount)])
    #make exception if data is not integer to avoid error
    except ValueError:
        print("Type only integer >0!")
        pass
