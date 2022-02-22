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
    # Set variables
    variables = get_variables()
    config = get_config()
    root = variables["root"]
    courses = variables["courses"]
    courses_list = courses.split(",")
    folders = list()
    current_directory = ""
    for course in courses_list:
        current_directory = f"{root}/{course}"
        os.mkdir(current_directory)
        # Build backbone
        for bone in config:
            # Mount bone
            if(">" in bone):
                # Mount last folder
                current_directory = f"{current_directory}/{folders[-1]}"
            # Unmount bone
            elif("<" in bone):
                # Unmount last folder
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
build_backbone()