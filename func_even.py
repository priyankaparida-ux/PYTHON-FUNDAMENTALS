# write a function that takes two integers a and b and prints all even numbers between them (inclusive)
def even(a,b):
    for i in range(a,b+1):
        if(i%2 == 0):
            print(i)

a = int(input("Enter the starting number: "))
b = int(input("Enter the last number: "))
print(even(a,b))