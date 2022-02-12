"""3. Write a Python program to sum of two given integers. However,
if the sum is between 15 to 20 it will return 20."""

while True:
    int_1 = int(input("Int 1:"))
    int_2 = int(input("Int 2:"))
    if (int_1+int_2) > 15 and (int_1+int_2) < 20:
        print("20")
    else:
        print("<====>")
