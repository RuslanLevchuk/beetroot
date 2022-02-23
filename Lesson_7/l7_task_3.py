#this function makes operations
def make_operation(operation, *digits):
    #in case *args takes not a sequence as argument, but list or tuple↓
    if type(digits[0]) == tuple or type(digits[0]) == list:
        #→we get first elevent (list) of tuple/or list
        digits = list(digits[0])
    #initialize result as 0
    result = 0
    #use exception in case if at least one element of our sequence is not float
    #get first element and assign it to first operator result
    # resut will be inital for next arithmetical operations with other sequences
    try:
        result = float(digits[0])
        digits.pop(0)

    #return error if we can't convert in float
    except ValueError as err:
        return f"Data is incorrect: => {err}"

#analyze operation symbol
    if operation == '+':
        #cycle other remaining sequences
        for digit in digits:
            #tru to convert each of them into float
            try:
                digit = float(digit)
                #adding each value to result
                result += digit
            # return error if will be convertation error
            except ValueError as err:
                return f"Data is incorrect: => {err}"
#and other arithmetic oparations......
    elif operation == '-':
        for digit in digits:
            try:
                digit = float(digit)
                result -= digit
            except ValueError as err:
                return f"Data is incorrect: => {err}"

    elif operation == '*':
        for digit in digits:
            try:
                digit = float(digit)
                result *= digit
            except ValueError as err:
                return f"Data is incorrect: => {err}"
    #if operations symbol is another, function returns error
    else:
        return f"Incorrect operation \"{operation}\""
#conversion result in usability look
    if result%1 == 0:
        #if reminder equeal to 0, result converts and returns as integer
        return int(result)
    else:
        #else return in float
        return result

#just examples
print(make_operation('+', (5, 5, 5)))
print(make_operation('-', (5, 5, 5)))
print(make_operation('*', (5, 5, 5)))

#work with user input
while 1:
    #initialize symbol oparation
    symbol = None
    #get input from user
    value = input('Type operation and sequence of numbers (separated by comma or/and whitespaces): (+3.5,3.9,4.7):')
    #replace with whitespaces all commas
    value = value.replace(',', ' ')
    #split all values with whitespace between and assign elements in list
    value = value.split(' ')
    #delete all whitespaces in each element of list
    for n, val in enumerate(value):
        value[n] = val.strip()
    #dele all empty elements in list
    while '' in value:
        value.remove('')
    #in case user prompted operation symbol withot whitespace, first element may be longer that 1 symbol:
    #length of '+' will be 1
    if len(value[0]) == 1:
        #so we must to get operation symbol and delete its element from list
        symbol = value.pop(0)
    # else length of '+12' will be 3 etc
    else:
        #create temporary string
        temporary_first_str = ''
        #convert firs element of string into list
        first_str = list(value[0])
        #get and delete first element from its (one of opearion elements + - *)
        symbol = first_str.pop(0)
        #and push back other elements of list in temporary string
        for i in first_str:
            temporary_first_str += i
        #and push temporary string without operation symbol in our sequnece
        value[0] = temporary_first_str

    #all data are ready and we can pass them in our function make_operation
    # we can input variations of input:
    # with any number of spaces, commas
    # with/without(but with spaces) commas
    # with/without(but with commas) spaces
    # exampe: + 12,,,, 12   ,12 | result = 36
    # exampe: + 12,12 12 | result = 36
    # exampe: +12 12 12 | result = 36
    # etc..

    print(f"Result: {make_operation(symbol, value)}")


