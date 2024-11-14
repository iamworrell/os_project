#authors: worrel seville, tian mcfarlane, demario scott, javan james
import os
import time

print("Welcome to The terminal")
print("Enter exit to Leave The terminal")


#Environment Variables
current_dir = os.path.dirname(__file__)

#output current directory
print(current_dir)
exit = 0
index = 0
skip = False
validated_input = ""
pipe_validated_input = ""
temp_validated_input = ""

def initialize():
  #Wait for user input
  global initial_input
  initial_input = input("")
  global pipe_validated_input
  pipe_validated_input = ""

  #Convert all input to string
  global user_input
  user_input = str(initial_input)

  #format input
  #convert input to lowercase
  global validated_input
  validated_input = user_input.lower()

  global from_pipe
  global skip
  if validated_input.find("|") != -1:
    from_pipe = True
  else:
    from_pipe = False
  


#Keep looping until exit command
while exit != 1:
  if skip == False:
    pipe_validated_input = ""
    validated_input = ""
    initialize()
    end = False

  #Logic for piping
  if validated_input.find("|") != -1:
    skip = True
    if index == 0:
      #split input up
      array_of_commands = validated_input.split("|")
      unvalidated_input = array_of_commands[index]
      pipe_validated_input = unvalidated_input.lstrip()

      #store input to temp initially
      temp_validated_input = validated_input
      repeat = False
    else:
      if index < len(array_of_commands):
        array_of_commands = validated_input.split("|")
        unvalidated_input = array_of_commands[index]
        pipe_validated_input = unvalidated_input.lstrip()

        #clear validated input for pipe
        validated_input = ""
      else:
        pipe_validated_input = ""
        validated_input = ""
        end = True
        repeat = True
        skip = False
        #reset index
        index = 0

    #Increment Index based on Criteria
    if from_pipe == True and repeat == False:
      index = index + 1
    if from_pipe == True and repeat == True:
      index = 0


  if end == False:
    #Error Handling
    if from_pipe == True:
      if temp_validated_input.find("cd..", 0) != 0 and temp_validated_input.find("exit", 0) != 0 and temp_validated_input.find("help", 0) != 0 and temp_validated_input.find("create", 0) != 0 and temp_validated_input.find("rename", 0) != 0 and temp_validated_input.find("delete", 0) != 0 and temp_validated_input.find("make", 0) != 0 and temp_validated_input.find("remove", 0) != 0 and temp_validated_input.find("change", 0) != 0 and temp_validated_input.find("modify", 0) != 0 and temp_validated_input.find("list -l", 0) != 0:
        print("unrecognized command, please use the \"help\" command for assistance")
    else:
      if validated_input.find("cd..", 0) != 0 and validated_input.find("exit", 0) != 0 and validated_input.find("help", 0) != 0 and validated_input.find("create", 0) != 0 and validated_input.find("rename", 0) != 0 and validated_input.find("delete", 0) != 0 and validated_input.find("make", 0) != 0 and validated_input.find("remove", 0) != 0 and validated_input.find("change", 0) != 0 and validated_input.find("modify", 0) != 0 and validated_input.find("list -l", 0) != 0:
        print("unrecognized command, please use the \"help\" command for assistance")
        
    #check if input includes the keyword create
    if validated_input.find("create", 0) == 0 or pipe_validated_input.find("create", 0) == 0:

      #Exceptioan Handling
      try:
        if from_pipe == True:
          single_command_validated_input = pipe_validated_input
          #remove all blank space
          noBlankSpace = single_command_validated_input.replace(" ", "")
          #remove create from input and only get name of file we wish to create
          textFileName = noBlankSpace[6:]
        if from_pipe == False:
          #remove all blank space
          noBlankSpace = validated_input.replace(" ", "")
          #remove create from input and only get name of file we wish to create
          textFileName = noBlankSpace[6:]

        #create file in same directory
        file_path = os.path.join(current_dir, textFileName + ".txt")
        open(file_path, 'w')
        print("File Created")
        
      except Exception:
        print("Something went wrong")
      
      finally:
        #output current directory
        print(current_dir)
        validated_input = temp_validated_input
      


        
    #Delete File Command
    #Check if input includes the keyword 'delete' at the start of the input
    elif validated_input.find("delete", 0) == 0 or pipe_validated_input.find("delete", 0) == 0:
      print(pipe_validated_input)
      try:
        if from_pipe == True:
          single_command_validated_input = pipe_validated_input
          #remove all blank space
          noBlankSpace = single_command_validated_input.replace(" ", "")

          #Remove 'delete' from input to get the name of the file to delete
          text_file_name = noBlankSpace[6:]
          
          #Get the path of the file to delete in the current directory
          file_path = os.path.join(current_dir, text_file_name + ".txt")
        if from_pipe == False:
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
      finally:
        #output current directory
        print(current_dir)
        #re-initialize validated_input with user original data
        validated_input = temp_validated_input

    #rename file feature
    command = ''
    original_file_name = ''
    new_file_name = ''
    if validated_input.find("rename", 0) == 0 or pipe_validated_input.find("rename", 0) == 0:
      try:
        if from_pipe == True:
          single_command_validated_input = pipe_validated_input
          
          #split input up
          array_of_data = single_command_validated_input.split()

          #assign the appropirate parts of input to the variable
          command = array_of_data[0]
          original_file_name = array_of_data[1]
          new_file_name = array_of_data[2]

          original_file_name_path = os.path.join(current_dir, original_file_name + ".txt")
          new_file_name_path = os.path.join(current_dir, new_file_name + ".txt")
          os.rename(original_file_name_path, new_file_name_path)
          print(original_file_name + " changed to the name" + new_file_name)

        if from_pipe == False:
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
      finally:
        #output current directory
        print(current_dir)
        #re-initialize validated_input with user original data
        validated_input = temp_validated_input

    #Exit Feature
    if validated_input.find("exit", 0) == 0:
      exit = 1

    if validated_input.find("help", 0) == 0 or pipe_validated_input.find("help", 0) == 0:
      print("create     Create file")
      print("rename     Renames a file")
      print("delete     deletes a file")
      print("modify     Modify file permissions")
      print("list -l    List file attributes")
      print("cd..       Move back one directory")
      print("exit       Exit the terminal")
      validated_input = temp_validated_input
    
    #Demario Scott Directory Code
    #Make Directory
    if validated_input.startswith("make") or pipe_validated_input.startswith("make"):
      try:
        if from_pipe == True:
          dir_name = pipe_validated_input.split(" ")[1]
          if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            print(f"Directory '{dir_name}' created")
            #output current directory
            print(current_dir)
          else:
            print(f"Error: Directory '{dir_name}' already exists")
        if from_pipe == False:
          dir_name = validated_input.split(" ")[1]
          if not os.path.exists(dir_name):
            os.mkdir(dir_name)
            print(f"Directory '{dir_name}' created")
            
          else:
            print(f"Error: Directory '{dir_name}' already exists")
      except:
        print("Something Went Wrong")
      finally:
        #output current directory
        print(current_dir)
        validated_input = temp_validated_input

    #Remove a Directory
    elif validated_input.startswith("remove") or pipe_validated_input.startswith("remove"):
      try:
        if from_pipe == True:
          dir_name = pipe_validated_input.split(" ")[1]
          if os.path.exists(dir_name) and os.path.isdir(dir_name):
              os.rmdir(dir_name)
              print(f"Directory '{dir_name}' removed")
          else:
              print(f"Error: Directory '{dir_name}' does not exist or is not empty")
        if from_pipe == False:
          dir_name = validated_input.split(" ")[1]
          if os.path.exists(dir_name) and os.path.isdir(dir_name):
              os.rmdir(dir_name)
              print(f"Directory '{dir_name}' removed")
              
          else:
              print(f"Error: Directory '{dir_name}' does not exist or is not empty")
      except:
        print("Soemthing Went Wrong")
      finally:
        #output current directory
        print(current_dir)
        validated_input = temp_validated_input

  # Change to a Directory location
    elif validated_input.startswith("change") or pipe_validated_input.startswith("change"):
      try:
        if from_pipe == True:
          dir_name = pipe_validated_input.split(" ")[1]
          if os.path.exists(dir_name) and os.path.isdir(dir_name):
            os.chdir(dir_name)
            print(f"Changed directory to '{dir_name}'")

            testing = dir_name
            #change path when we change directory
            folder_name = str(testing)

            #each time we change directory we add to the directory we were before
            #update current_dir variable
            current_dir = current_dir + "\\" + folder_name
          else:
            print(f"Error: Directory '{dir_name}' does not exist")
        if from_pipe == False:
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
            
          else:
            print(f"Error: Directory '{dir_name}' does not exist")
      except:
        print("Something Went Wrong")
      finally:
        #output current directory
        print(current_dir)
        validated_input = temp_validated_input

  #Remove last folder from path and go back to previous folder
    if validated_input.startswith("cd..") or pipe_validated_input.startswith("cd.."):

      try:
        #split input up
        array_of_folders = current_dir.split("\\")

        #remove last folder from path,
        new_dir = current_dir.replace("\\" + array_of_folders[-1], '')

        #update current working directory
        current_dir = new_dir
        #output current directory
        print(current_dir)

        #update directory to create folders as well
        os.chdir('../')
      except:
        print("Something Went Wrong")
      finally:
        validated_input = temp_validated_input
  
    

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

    elif validated_input.startswith("modify") or pipe_validated_input.startswith("modify"):
      try:
        if from_pipe == True:
          # Split input to get permissions and file name
          array_of_data = pipe_validated_input.split()
          if len(array_of_data) != 3:
            print("Usage: modify <permissions> <file_name>")
          else:
            permissions = int(array_of_data[1], 8)  # Convert permissions from octal
            file_name = array_of_data[2]
            file_path = os.path.join(current_dir, file_name + ".txt")
            if os.path.exists(file_path):
                os.chmod(file_path, permissions)  # Modify permissions
                print(f"Permissions for {file_name} modified to {oct(permissions)}")
                #output current directory
                print(current_dir)
            else:
                print("Error: File does not exist")
        if from_pipe == False:
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
                #output current directory
                print(current_dir)
            else:
                print("Error: File does not exist")
      except:
        print("Something went wrong")
      finally:
        validated_input = temp_validated_input

    # List file attributes
    elif validated_input.startswith("list -l") or pipe_validated_input.startswith("list -l"):
      try:
        if from_pipe == True:
          # Split input to get file name
          array_of_data = pipe_validated_input.split()
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
                  #output current directory
                  print(current_dir)
              else:
                  print("Error: File does not exist")
        if from_pipe == False:
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
                  #output current directory
                  print(current_dir)
              else:
                  print("Error: File does not exist")
      except:
        print("Something went wrong")
      finally:
        validated_input = temp_validated_input
      
    # Exit Command
    elif validated_input.startswith("exit") or pipe_validated_input.startswith("exit"):
      exit = 1
      validated_input = temp_validated_input