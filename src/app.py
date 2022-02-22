##### BACKBONE,
##### A
##### MINIMAL
##### BATCH
##### FOLDER
##### MAKER
##### <>

import os
from parser import get_variables, get_config

def build_backbone():
    # Get .conf data
    variables = get_variables()
    config = get_config()
    # Unpack variables
    root = variables["root"]
    courses = variables["courses"]
    # Map from string to list
    courses_list = courses.split(",")
    # Define state variables
    folders = list()
    current_directory = ""
    for course in courses_list:
        # Create course folder
        current_directory = f"{root}/{course}"
        os.mkdir(current_directory)
        # Build course backbone
        for bone in config:
            # Move down one directory
            if(">" in bone):
                # Mount last bone
                current_directory = f"{current_directory}/{folders[-1]}"
            # Move up one directory)
            elif("<" in bone):
                # Unmount last bone
                current_directory = "/".join(current_directory.split("/")[:-1])
            # Execute command
            else:
                command,argument = bone.split(":")
                command,argument = command.strip(),argument.strip()
                # Parse command
                if(command == "f"):
                    # Save folder
                    folders.append(argument)
                    # Create folder
                    os.mkdir(f"{current_directory}/{argument}")
                elif(command == "m" or command == "t"):
                    # Create file
                    new_file = open(f"{current_directory}/{argument}", "w")
                    new_file.close()
                else:
                    raise Exception(f"{command} is an unknown command. Only f,m and t commands are available.")

# LET'S BUILD THAT THING
build_backbone()