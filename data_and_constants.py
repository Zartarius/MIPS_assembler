'''
This file parses the assembly file,
looking for all static variables and constants, 
returning them a key value pairs.
'''

# Find all constants, and return as key value pairs
def parse_for_constants(file) -> dict:
    constants = {}
    for line in file:
        if "=" in line:
            key, value = line.split("=")
            constants[key.strip()] = int(value)
    print(constants)