import sys
import re

registers = {
    "$zero":0, "$v0":0, "$v1":0, "$a0":0, "$a1":0, "$a2":0, "$a3":0,
    "$t0":0, "$t1":0, "$t2":0, "$t3":0, "$t4":0, "$t5":0, "$t6":0, "$t7":0,
    "$gp":0, "$sp":0, "$fp":0, "$ra":0
}

constants = None
labels = None
globals = None
stack = [0] * 32000

def load_immediate(register, value, constants):
    if constants.get(value) is not None:
        registers[register] = constants.get(value)
    else:
        try:
            int(value)
            registers[register] = int(value)
        except ValueError:
            print(f"Error: Invalid immediate value: {value}.")
            sys.exit(1)


class Instructions:
    def __init__(self, lines=None, prog_counter=0, variables=None):
        self.lines = lines
        self.prog_counter = prog_counter
        
        global constants, labels, globals
        constants = variables[0]
        labels = variables[1]
        globals = variables[2]

    def halt(self):
        if self.prog_counter >= len(self.lines):
            return True
        else:
            return False

    def execute(self) -> None:
        global constants, labels, globals
        delimeters = r"[ ,]+"
        instruction = re.split(delimeters, self.lines[self.prog_counter])
        op = instruction[0]
        
        if op == "li" or op == "la":
            load_immediate(instruction[1], instruction[2], constants)
            print(registers[instruction[1]])
            self.prog_counter += 1

    
        

