n = int(input("Please enter a number: "))
sum = 0

#This code will print all the odd numbers from 0 to n and display the sum of each operation
for odd in range(n):
    if odd % 2 == 1:
        print("This is the odd number ", odd)
        sum += odd
        print("This is their sum", sum)