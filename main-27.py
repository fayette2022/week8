import os

My_Directory = (os.listdir())

#Show my directory
print(os.listdir())

# Ask user to name a directory
choose_directory = input("\nChoose a directory name: ")

# Ask user to create a file na,me
file_name = input("Enter the file name: ")
os.makedirs(choose_directory)
fullName = os.path.join(choose_directory, file_name+".txt") 

#Attributes
name = input("Write your contact name: ") 
telephone_number = input("Write your contact telephone number: ") 
full_adress = input("Type your contact full adress: ") 

file_name = f"{file_name}.txt"
while input != 'quit':
    with open (fullName, 'a') as file_object:
        file_object.write(f"Name: {name}.\n")
        file_object.write(f"Phone number: {telephone_number}.\n")
        file_object.write(f"Adress: {full_adress}.\n")
    prompt = input("\nWould you like to add another contact information? (Yes or NO): ").title() 
    if prompt == 'No':
        break
    else:
        name = input("\nWrite your contact name: ") 
        telephone_number = input("Write your contact phone number: ") 
        full_adress = input("Type your contact full adress: ")