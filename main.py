import sys
import static_and_const #type: ignore
import instructions #type: ignore

# Exit if there any issues with the cl args or file
if len(sys.argv) != 2:
    print("Error: Invalid number of arguments. Add a file name.", file=sys.stderr)
    sys.exit(1)
elif not sys.argv[1].endswith(".s"):
    print("Error: Invalid file extension. Only .s files are supported.", file=sys.stderr)
    sys.exit(1)

# Read the file and save in a list, after cleaning it up
with open(sys.argv[1], "r") as file:
    lines = file.readlines()
    lines = [line.split("#", maxsplit=1)[0] for line in lines] # Remove comments
    lines = [line.strip() for line in lines] # Remove extra whitespace
    lines = [line for line in lines if line != ""]  # Remove empty lines

constants, statics = static_and_const.ret_static_and_const(lines) # Parse all const and static variables

prog_counter = instructions.find_main(lines)

while prog_counter < len(lines):
    pass
