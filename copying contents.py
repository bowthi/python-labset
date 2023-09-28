def copy_file(source_file,destinaton_file):
    try:
        with open(source_file,'r') as source:
            content=source.read()
            print("Content of the source file :")
            print(content)
        with open(destination_file,'w') as destination:
            destination.write(content)
            print("File Content copied successfully in :",destination_file)

    except:
        print("One or the  both the files does not exist")
source_file="Source.txt"
destination_file="destination.txt"
copy_file(source_file,destination_file)