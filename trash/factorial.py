number = int(input("Type the integer: "))
factorial = 1

while number != 0:
    factorial *= number
    number -= 1

print(f"Factorial of you number is: {factorial}")

number = int(input("Type another integer: "))
def my_func (n):
    if n == 1:
        return 1
    return n*my_func(n-1)
print(f"Factorial of you number is: {my_func(number)}")
