import os

print("Welcome to The terminal")
#Wait for user input
initial_input = input("")

#Convert all input to string
user_input = str(initial_input)

#format input
#convert input to lowercase
validated_input = user_input.lower()

#check if input includes the keyword create
if validated_input.find("create", 0) == 0:
    #remove all blank space
    noBlankSpace = validated_input.replace(" ", "")
    #remove create from input and only get name of file we wish to create
    textFileName = noBlankSpace[6:]
    #create file in same directory
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, textFileName + ".txt")
    open(file_path, 'w')
    print("File Create")


    
#Delete File Command
#Check if input includes the keyword 'delete' at the start of the input
elif validated_input.find("delete", 0) == 0:
    #Delete File Command
    #Check if input includes the keyword 'delete' at the start of the input
    elif validated_input.find("delete", 0) == 0:
    #remove all blank space
    noBlankSpace = validated_input.replace(" ", "")

    #Remove 'delete' from input to get the name of the file to delete
    text_file_name = noBlankSpace[6:]
    
    #Get the path of the file to delete in the current directory
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, text_file_name + ".txt")
    
    #Check if the file exists before trying to delete it
    if os.path.exists(file_path):
        os.remove(file_path) #Delete the file
        print("File Deleted") #Confirm that the file has been deleted
    else:
        print("Error: File does not exist") #Display an error if file is not found

#rename file feature
command = ''
original_file_name = ''
new_file_name = ''
if validated_input.find("rename", 0) == 0:
  #split input up
  array_of_data = validated_input.split()

  #assign the appropirate parts of input to the variable
  command = array_of_data[0]
  original_file_name = array_of_data[1]
  new_file_name = array_of_data[2]

  current_dir = os.path.dirname(__file__)
  original_file_name_path = os.path.join(current_dir, original_file_name + ".txt")
  new_file_name_path = os.path.join(current_dir, new_file_name + ".txt")
  os.rename(original_file_name_path, new_file_name_path)
  print(original_file_name + " changed to the name" + new_file_name)