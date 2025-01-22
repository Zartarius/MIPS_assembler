import sys
import init #type: ignore
from program import Program #type: ignore


lines = init.read_file(sys.argv)
prog_counter = init.find_main(lines)
variables = init.variables(lines) # Parse all labels and const and static variables

program = Program(lines, prog_counter, variables)

while program.halt() is False:
    program.fetch_decode_execute()
