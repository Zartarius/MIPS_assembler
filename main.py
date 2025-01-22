import sys
import init #type: ignore
from instructions import Instructions


lines = init.read_file(sys.argv)
prog_counter = init.find_main(lines)
variables = init.variables(lines) # Parse all labels and const and static variables

instructions = Instructions(lines, prog_counter, variables)

while not instructions.halt():
    instructions.execute()
