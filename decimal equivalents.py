def print_decimal_equivalents(n):
    for i in range(2,n+1):
        decimal=1.0/i
        print("The decimal equivalent of 1/{0} is {1:4f}".format(i,decimal))
n=int(input("Enter the value of 'n' :"))
print_decimal_equivalents(n)