my_tuple=((1,2,3,4,5),6,7,8,9,10,['a','e','i','o','u'],"red","green","blue",'l','@','$')
print("Original tuple :",my_tuple)
slice1=my_tuple[2:5]
print("Slice 1 [2:5] :",slice1)

slice2=my_tuple[:5]
print("\n Slice 2 [:5] :",slice2)

slice3=my_tuple[5:]
print("\n Slice 3 [5:] :",slice3)

slice4=my_tuple[2:9:2]
print("\n Slice 4 [2:9:4] :",slice4)

slice5=my_tuple[:]
print("\n Slice 5 [:] :",slice5)

slice6=my_tuple[-3:1]
print("\n Slice 1 [-3:1] :",slice6)

slice7=my_tuple[: :4]
print("\n Slice 7 [: :4] :",slice7)

slice8=my_tuple[-2:-4:-2]
print("\n Slice 8 [-2:-4:-2] :",slice8)

slice9=my_tuple[9:2:-4]
print("\n Slice 9 [9:2:-4] :",slice9)

slice10=my_tuple[0]
print("\n Slice 10 :",slice10)

reverse_tuple=my_tuple[: :-1]
print("\n Reverse tuple :",reverse_tuple)