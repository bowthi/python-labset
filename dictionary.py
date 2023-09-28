print("Creating a new dictionary :")
this_dict={
    "Brand Name":"Lakme",
    "Founder":"J.R.D",
    "Product":"Sun Screen"
}
print(this_dict)

print("\n Adding a new key-value pairs :")
new_key=input("Enter a key :")
new_value=input("Enter a value :")
this_dict[new_key]=[new_value]
print(this_dict)

print("\n Changing the value based on the key :")
change_key=input("Enter the key :")
change_value=input("Enter the value :")
this_dict.update({change_key:change_value})
print(this_dict)

print("\n Retrieving the value based on the key :")
retrieve_key=input("Enter a key :")
retrieve_value=this_dict[retrieve_key]
print(retrieve_value)