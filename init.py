import sys


def read_file(cl_args) -> list[str]:
    # Exit if there any issues with the cl args or file
    if len(cl_args) != 2:
        print("Error: Invalid number of arguments. Add a file name.", file=sys.stderr)
        sys.exit(1)
    elif not cl_args[1].endswith(".s"):
        print("Error: Invalid file extension. Only .s files are supported.", file=sys.stderr)
        sys.exit(1)

    # Read the file and save in a list, after cleaning it up
    with open(cl_args[1], "r") as file:
        lines = file.readlines()
        lines = [line.split("#", maxsplit=1)[0] for line in lines] # Remove comments
        lines = [line.strip() for line in lines] # Remove extra whitespace
        lines = [line for line in lines if line != ""]  # Remove empty lines
    
    return lines


# Exits the program if a variable name is invalid
def _check_valid_name(constants:dict, name) -> None:
    valid_chars = all(c.isalpha() or c == "_" or c.isdigit() for c in name)
    valid_name = valid_chars and not name[0].isdigit() # Check if name starts with digit
    
    if not valid_name:
        print(f"Error: Invalid name '{name}'. Failed to parse.", file=sys.stderr)
        sys.exit(1)
    elif constants.get(name) is not None:
        print(f"Error: Name '{name}' defined multiple times.", file=sys.stderr)
        sys.exit(1)


def _parse_constants(lines) -> dict:
    constants = {}
    for line in lines:
        if "=" in line:
            key, value = line.split("=")
            _check_valid_name(constants, key.strip())
            constants[key.strip()] = int(value)
    return constants


def _parse_globals(lines) -> dict:
    return None


def _parse_labels(lines) -> dict:
    return None


# Find all constants, labels and statics (globals), and return as key value pairs
def variables(lines) -> tuple[dict, dict]:
    return (_parse_constants(lines), _parse_labels(lines), _parse_globals(lines))


# Returns the line number of where main: starts
def find_main(lines) -> int:
    line_number = 0
    # Search for main
    for line in lines:
        if "main:" in line:
            return line_number + 1
        else:
            line_number += 1
    # No main label found, exit the program
    print("Error: No main label found in the file.", file=sys.stderr)
    sys.exit(1)
