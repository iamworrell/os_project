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