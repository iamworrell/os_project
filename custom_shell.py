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