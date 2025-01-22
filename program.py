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


def syscall() -> None:
    syscall_num = registers["$v0"]
    arg = registers["$a0"]

    if syscall_num == 1 or syscall_num == 4:
        print(arg, end="")
    elif syscall_num == 5:
        registers["$v0"] = int(input())
    elif syscall_num == 11:
        print(arg, end="")
    else:
        print("Invalid syscall number.", file=sys.stderr)
        sys.exit(1)


def load_immediate(register, value, constants) -> None:
    if constants.get(value) is not None:
        registers[register] = constants.get(value)
    elif all(c.isdigit() for c in value):
        registers[register] = int(value)
    else:
        esc_seq_string = value.strip("'")
        char = esc_seq_string.encode("utf-8").decode("unicode_escape")
        registers[register] = char
        

class Program:
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

    def fetch_decode_execute(self) -> None:
        global constants, labels, globals
        delimeters = r"[ ,]+"
        instruction = re.split(delimeters, self.lines[self.prog_counter])
        op = instruction[0]
        
        if op == "syscall":
            syscall()
            self.prog_counter += 1
        elif op == "li" or op == "la":
            load_immediate(instruction[1], instruction[2], constants)
            print(registers[instruction[1]])
            self.prog_counter += 1
        else:
            self.prog_counter += 1

    
        

