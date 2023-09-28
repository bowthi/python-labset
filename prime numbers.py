start=int(input("Enter the lower bound :"))
stop=int(input("Enter the upper bound :"))
print("Prime numbers betweeen the ",start,"and",stop,"are :")
for val in range(start,stop+1):
    for i in range(2,val):
        if val%i==0:
            break
    else:
        print(val)1
