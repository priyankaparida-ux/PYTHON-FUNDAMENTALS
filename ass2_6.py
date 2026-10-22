# WAP to print all numbers from 1 to 100 that are divisible by both 3 and 5
def divisible(a,b):
    for i in range(a,b+1):
        if (i%3 == 0 and i%5 == 0):
            print(i)
a = int(input("Enter the starting number: "))
b = int(input("Enter the last number: "))
divisible(a,b)