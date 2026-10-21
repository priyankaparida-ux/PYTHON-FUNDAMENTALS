# write a function that prints the digits of a number n
# eg - n = 312 
# output = 3,1,2
def digit(n):
    while n>0:
        d = n%10
        print(d)
        n = n//10
n = int(input("Enter a digit : "))
digit(n)

'''
n = 312
312 % 10 = 2
312 // 10 = 31
31 % 10 = 1
31 // 10 = 3
'''