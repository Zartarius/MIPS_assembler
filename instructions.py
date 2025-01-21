import sys

# Returns the line number of where main: starts
def find_main(lines) -> int:
    line_number = 0
    # Search for main
    for line in lines:
        if "main:" in line:
            return line_number
        else:
            line_number += 1
    # No main label found, exit the program
    print("Error: No main label found in the file.", file=sys.stderr)
    sys.exit(1)