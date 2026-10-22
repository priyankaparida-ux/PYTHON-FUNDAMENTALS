# write a function to return the sum of digits of a number n
def sum(n):
    sum = 0
    while (n>0):
        d = n%10
        sum += d
        n = n//10
    return sum
n = int(input("Enter the number: "))
print(sum(n))