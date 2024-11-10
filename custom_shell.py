import os
import time

print("Welcome to The terminal")
print("Enter exit to Leave The terminal")
exit = 0

while exit != 1:

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

  if validated_input.find("exit", 0) == 0:
    exit = 1

  if validated_input.find("help", 0) == 0:
    print("create     Create file")
    print("rename     Renames a file")
    print("delete     deletes a file")
    print("modify     Modify file permissions")
    print("list -l    List file attributes")
    print("exit       Exit the terminal")

  
  # Modify file permissions

  #octal codes for the different permissions
    #octal code     Permission          Description
    #   0               ---             No premissions
    #   1               --x             Execute only
    #   2               -w-             Write only
    #   3               -wx             Write and execute
    #   4               r--             Read only
    #   5               r-x             Read and execute
    #   6               rw-             Read and write
    #   7               rwx             Read, write, and execute

    #common 3 digit octal permission codes
    #octal code       Description
    #  777            Read, write , and execute for owner, group, and others
    #  755            Read and exeute for everyone, write for owner
    #  644            Read and write for owner, read for group and others
    #  600            Read and write for owner, no access for group and others
    #  700            Read, write and execute for the owner only
    #  500            Read and execute for owner only
    #  400            Read only for owner

  elif validated_input.startswith("modify"):
    # Split input to get permissions and file name
    array_of_data = validated_input.split()
    if len(array_of_data) != 3:
      print("Usage: modify <permissions> <file_name>")
    else:
      permissions = int(array_of_data[1], 8)  # Convert permissions from octal
      file_name = array_of_data[2]
      current_dir = os.path.dirname(__file__)
      file_path = os.path.join(current_dir, file_name + ".txt")
      if os.path.exists(file_path):
          os.chmod(file_path, permissions)  # Modify permissions
          print(f"Permissions for {file_name} modified to {oct(permissions)}")
      else:
          print("Error: File does not exist")

  # List file attributes
  elif validated_input.startswith("list -l"):
    # Split input to get file name
    array_of_data = validated_input.split()
    if len(array_of_data) != 3:
        print("Usage: list -l <file_name>")
    else:
        file_name = array_of_data[2]
        current_dir = os.path.dirname(__file__)
        file_path = os.path.join(current_dir, file_name + ".txt")
        if os.path.exists(file_path):
            stat_info = os.stat(file_path)
            file_size = stat_info.st_size
            # Get the last modified time
            modification_time = time.ctime(stat_info.st_mtime)
            # Get permissions
            permissions = oct(stat_info.st_mode & 0o777)  # Get the last three digits of octal
            print(f"File: {file_name}.txt")
            print(f"Size: {file_size} bytes")
            print(f"Permissions: {permissions}")
            print(f"Last Modified: {modification_time}")
        else:
            print("Error: File does not exist")

  # Exit Command
  elif validated_input.startswith("exit"):
      exit = 1

  else:
        print("Error: Unrecognized command. Type 'help' for a list of available commands.")