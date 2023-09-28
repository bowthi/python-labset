def  compute_gcd(x,y):
    while(y):
        temp=y
        y=x%y
        x=temp
    return x
def compute_lcm(x,y):
    lcm=(x*y)//compute_gcd(x,y)
    return lcm
num1=int(input("Enter the first number :"))
num2=int(input("Enter the second number :"))
gcd=compute_gcd(num1,num2)
lcm=compute_lcm(num1,num2)
print("The GCD of",num1,"and",num2,"is :",gcd)
print("The LCM of",num1,"and",num2,"is :",lcm)