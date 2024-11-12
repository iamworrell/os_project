#authors: worrel seville, tian mcfarlane, demario scott, javan james
import os
import time

print("Welcome to The terminal")
print("Enter exit to Leave The terminal")

print(os.path.dirname(__file__))
print(os.getcwd())

#Environment Variables
current_dir = os.path.dirname(__file__)
exit = 0

#Keep looping until exit command
while exit != 1:

  #Wait for user input
  initial_input = input("")

  #Convert all input to string
  user_input = str(initial_input)
  
  #format input
  #convert input to lowercase
  validated_input = user_input.lower()

  #Error Handling
  if validated_input.find("cd..", 0) != 0 and validated_input.find("exit", 0) != 0 and validated_input.find("help", 0) != 0 and validated_input.find("create", 0) != 0 and validated_input.find("rename", 0) != 0 and validated_input.find("delete", 0) != 0 and validated_input.find("make", 0) != 0 and validated_input.find("remove", 0) != 0 and validated_input.find("change", 0) != 0 and validated_input.find("modify", 0) != 0 and validated_input.find("list -l", 0) != 0:
    print("unrecognized command, please use the \"help\" command for assistance")

  #check if input includes the keyword create
  if validated_input.find("create", 0) == 0:

    #Exceptioan Handling
    try:
      #remove all blank space
      noBlankSpace = validated_input.replace(" ", "")
      #remove create from input and only get name of file we wish to create
      textFileName = noBlankSpace[6:]
      
      
      #create file in same directory
      file_path = os.path.join(current_dir, textFileName + ".txt")
      open(file_path, 'w')
      print("File Create")
    except Exception:
      print("Something went wrong")
    


      
  #Delete File Command
  #Check if input includes the keyword 'delete' at the start of the input
  elif validated_input.find("delete", 0) == 0:
    try:
      #remove all blank space
      noBlankSpace = validated_input.replace(" ", "")

      #Remove 'delete' from input to get the name of the file to delete
      text_file_name = noBlankSpace[6:]
      
      #Get the path of the file to delete in the current directory
      file_path = os.path.join(current_dir, text_file_name + ".txt")
      
      #Check if the file exists before trying to delete it
      if os.path.exists(file_path):
        os.remove(file_path) #Delete the file
        print("File Deleted") #Confirm that the file has been deleted
      else:
        print("Error: File does not exist") #Display an error if file is not found
    except:
      print("Something Went Wrong")

  #rename file feature
  command = ''
  original_file_name = ''
  new_file_name = ''
  if validated_input.find("rename", 0) == 0:
    try:
      #split input up
      array_of_data = validated_input.split()

      #assign the appropirate parts of input to the variable
      command = array_of_data[0]
      original_file_name = array_of_data[1]
      new_file_name = array_of_data[2]

      original_file_name_path = os.path.join(current_dir, original_file_name + ".txt")
      new_file_name_path = os.path.join(current_dir, new_file_name + ".txt")
      os.rename(original_file_name_path, new_file_name_path)
      print(original_file_name + " changed to the name" + new_file_name)
    except:
      print("Something went wrong")

  #Exit Feature
  if validated_input.find("exit", 0) == 0:
    exit = 1

  if validated_input.find("help", 0) == 0:
    print("create     Create file")
    print("rename     Renames a file")
    print("delete     deletes a file")
    print("modify     Modify file permissions")
    print("list -l    List file attributes")
    print("exit       Exit the terminal")

# Demario Scott Directory Code
# Make Directory
  elif validated_input.startswith("make"):
    try:
      dir_name = validated_input.split(" ")[1]
      if not os.path.exists(dir_name):
          os.mkdir(dir_name)
          print(f"Directory '{dir_name}' created")
      else:
          print(f"Error: Directory '{dir_name}' already exists")
    except:
      print("Something Went Wrong")

# Remove a Directory
  elif validated_input.startswith("remove"):
    try:
      dir_name = validated_input.split(" ")[1]
      if os.path.exists(dir_name) and os.path.isdir(dir_name):
          os.rmdir(dir_name)
          print(f"Directory '{dir_name}' removed")
      else:
          print(f"Error: Directory '{dir_name}' does not exist or is not empty")
    except:
      print("Soemthing Went Wrong")

# Change to a Directory location
  elif validated_input.startswith("change"):
    try:
      
      
      dir_name = validated_input.split(" ")[1]
      print(dir_name)
      if os.path.exists(dir_name) and os.path.isdir(dir_name):
        os.chdir(dir_name)
        print(f"Changed directory to '{dir_name}'")

        testing = dir_name
        #change path when we change directory
        folder_name = str(testing)

        #each time we change directory we add to the directory we were before
        #update current_dir variable
        current_dir = current_dir + "\\" + folder_name
        print(current_dir)
      else:
        print(f"Error: Directory '{dir_name}' does not exist")
    except:
      print("Something Went Wrong")

#Remove last folder from path and go back to previous folder
  if validated_input.startswith("cd.."):

    #split input up
    array_of_folders = current_dir.split("\\")

    #remove last folder from path,
    new_dir = current_dir.replace("\\" + array_of_folders[-1], '')

    #update current working directory
    current_dir = new_dir
    print(current_dir)

    #update directory to create folders as well
    os.chdir('../')

# End of Demario Scott Directory Code

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
    try:
      # Split input to get permissions and file name
      array_of_data = validated_input.split()
      if len(array_of_data) != 3:
        print("Usage: modify <permissions> <file_name>")
      else:
        permissions = int(array_of_data[1], 8)  # Convert permissions from octal
        file_name = array_of_data[2]
        file_path = os.path.join(current_dir, file_name + ".txt")
        if os.path.exists(file_path):
            os.chmod(file_path, permissions)  # Modify permissions
            print(f"Permissions for {file_name} modified to {oct(permissions)}")
        else:
            print("Error: File does not exist")
    except:
      print("Something went wrong")

  # List file attributes
  elif validated_input.startswith("list -l"):
    try:
      # Split input to get file name
      array_of_data = validated_input.split()
      if len(array_of_data) != 3:
          print("Usage: list -l <file_name>")
      else:
          file_name = array_of_data[2]
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
          else:
              print("Error: File does not exist")
    except:
      print("Something went wrong")
    
  # Exit Command
  elif validated_input.startswith("exit"):
      exit = 1