import sys    

# Check if file and file contents are valid, and free
# of syntax errors
def check_file_syntax(cl_args: list[str]) -> bool:
    # Check if command line argument is provided
    if len(cl_args) != 2:
        print("Error: Invalid number of arguments. Add a file name.", file=sys.stderr)
        return False

    # Check for valid file extension
    if cl_args[1].endswith(".s") == False:
        print("Error: Invalid file extension. Only .s files are supported.", file=sys.stderr)
        return False
    
    retval = True
    with open(cl_args[1], "r") as file:
        contents = file.read()

        # Check for main label
        if "main:" not in contents:
            print("Error: Provide a 'main' label.", file=sys.stderr)
            retval = False


