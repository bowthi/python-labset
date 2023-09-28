input_str=input("Enter the list elements seprated by spaces :")
input_list=input_str.split()
my_list=[int(element) for element in input_list]
print("List elements :",my_list)
print("First element :",my_list[0])
print("Last element :",my_list[-1])
print("Sliced element",my_list[1:4])

index=input("Enter the index of  the element to modify :")
value=input("Enter the new value :")
my_list[int(index)]=int(value)
print("Modified List :",my_list)
value=input("Enter the element to append :")
my_list.append(int(value))
print("List after appending :",my_list)

index=input("Enter the index of the element to delete :")
del my_list[int(index)]
print("List after deleting :",my_list)
print("Length of the list :",len(my_list))
my_list.sort()
print("Sorted list :",my_list)
my_list.reverse()
print("Reversed List :",my_list)

copy_list=my_list[:]
print("Copied list :",my_list)

new_list_str=input("Enter additional list elements separated by spaces :")
new_list=[int(element) for element in new_list_str.split()]
concatenated_list=my_list + new_list
print("Concatenated list :",concatenated_list)