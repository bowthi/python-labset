def count_char_vowel_spaces(text):
     num_character=len(text)
     vowels="aeiouAEIOU"
     num_vowels=sum(1 for char in text if char in vowels)
     num_spaces=sum(1 for char in text if char==" ")
     return num_character,num_vowels,num_spaces
text=input("Enter a line of text :")
char_count,vowel_count,space_count=count_char_vowel_spaces(text)
text=input("Enter a line of text :")
print("Number of Characters :",char_count-space_count)
print("Number of Vowels :",vowel_count)
print("Number of Spaces :",space_count)