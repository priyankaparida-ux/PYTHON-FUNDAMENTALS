# write a function to return the count of the number of digitd in a number n
def count(n):
    c = 0
    while (n>0):
        d = n%10
        c+=1
        n = n//10
    print(c)
n = int(input("Enter a number: "))
count(n)