import os
My_Directory = (os.listdir())

#Show my directory
print(os.listdir())

# Ask user to name a directory
choose_directory = input("\nChoose a directory name: ")

# Ask user to create a file name
file_name = input("Enter the file name: ")
os.makedirs(choose_directory)
fullName = os.path.join(choose_directory, file_name+".txt") 
fileObj= open(fullName, "w")
#Attributes

name = input("Write your contact name: ") 
telephone_number = input("Write your contact telephone number: ") 
full_adress = input("Type your contact full adress: ") 

file_name = f"{file_name}.txt"
file_object = open(fullName,"w")
while input != 'quit':
    with open (fullName, 'a') as file_object:
        file_object.write(f"{name}, {full_adress}, {telephone_number}.\n")

    prompt = input("\nWould you like to add another contact information? (Yes or NO): ").title() 
    if prompt == 'No':
        break
    else:
        name = input("\nWrite your contact name: ") 
        telephone_number = input("Write your contact phone number: ") 
        full_adress = input("Type your contact full adress: ")
        
file_object.close()   
file_object = open(fullName, "r")
print(file_object.read())