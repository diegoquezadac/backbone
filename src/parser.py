import os

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


def get_config():
    # Set variables
    file = open("../config/.conf", 'r')
    lines = file.readlines()
    parse = False
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