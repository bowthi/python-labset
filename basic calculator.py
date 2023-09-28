def add(p,q):
    return p+q
def sub(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
print("1.To Add..\n 2.To Subtract...\n3.To Multiply....\n 4.To Divide.....")
select=int(input("Please select the operation in 1/2/3/4 :"))
num1=float(input("Please enter the first number :"))
num2=float(input("Please enter the Second number :"))
if select==1:
    print(num1,"+",num2,"=",add(num1,num2))
elif select==2:
    print(num1,"-",num2,"=",sub(num1,num2))
elif select==3:
    print(num1,"*",num2,"=",multiply(num1,num2))
elif select==4:
    print(num1,"/",num2,"=",divide(num1,num2))
else:
    print("This is an Invalid input")