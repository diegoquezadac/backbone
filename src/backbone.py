import os
from typing import Optional


def get_variables():
    # Set variables
    file = open("../config/.conf", 'r')
    lines = file.readlines()
    parse = False
    variables = dict()
    # Read lines
    for line in lines:
        # Remove whitespaces
        line = line.strip()
        # Start variable parsing
        if(line == "VARIABLES"):
            parse = True
            continue
        # Parse variables
        if(parse and "=" in line):
            name,value = line.split("=")
            variables[name] = value
        # Stop parsing
        if(parse and "=" not in line):
            break
    return variables


def get_backbone_config():
    # Set variables
    file = open("../config/.conf", 'r')
    lines = file.readlines()
    # Set state variable
    parse = False
    # Set variable that will hold the configuration
    config = list()
    # Read lines
    for line in lines:
        # Remove \n
        line = line.strip("\n")
        # Start variable parsing
        if(line == "BACKBONE"):
            parse = True
            continue
        # Parse config file
        if(parse and ":" in line):
            config.append(line)
        if(">" in line or "<" in line):
            config.append(line)

    return config


def build_backbone(root: Optional[str] = None):
    # Get .conf data
    variables = get_variables()
    config = get_backbone_config()
    # Unpack variables
    if(root is None):
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