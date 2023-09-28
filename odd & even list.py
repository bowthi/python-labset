a=[]
n=int(input("Enter the number of elements :"))
for b in range (1,n+1):
    b=int(input("Enter th element :"))
    a.append(b)
even=[]
odd=[]
for b in a:
    if (b%2==0):
        even.append(b)
    else:
        odd.append(b)
print("The odd list is :",odd)
print("The even list is :",even)