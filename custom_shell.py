import os

print("Welcome to The terminal")
#Wait for user input
initial_input = input("")

#Convert all input to string
user_input = str(initial_input)

#format input
#remove all blank space
noBlankSpace = user_input.replace(" ", "")
#convert input to lowercase
validated_input = noBlankSpace.lower()

#check if input includes the keyword create
if validated_input.find("create", 0) == 0:
    #remove touch from input and only get name of file we wish to create
    textFileName = validated_input[6:]
    #create file in same directory
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, textFileName + ".txt")
    open(file_path, 'w')
    print("File Create")
    
#Delete File Command
#Check if input includes the keyword 'delete' at the start of the input
elif validated_input.find("delete", 0) == 0:
    #Remove 'delete' from input to get the name of the file to delete
    text_file_name = validated_input[6:]
    
    #Get the path of the file to delete in the current directory
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, text_file_name + ".txt")
    
    #Check if the file exists before trying to delete it
    if os.path.exists(file_path):
        os.remove(file_path) #Delete the file
        print("File Deleted") #Confirm that the file has been deleted
    else:
        print("Error: File does not exist") #Display an error if file is not found