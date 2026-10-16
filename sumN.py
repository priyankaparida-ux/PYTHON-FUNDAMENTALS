# sum of n natural numbers
# my way
n = int(input("enter a number"))
for i in range(n):
    n = n + i
print (n)

# apnacollege way
n = int(input("enter a number"))
sum = 0
for i in range(1,n+1):
    sum += i
print(sum)