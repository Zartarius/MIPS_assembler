def _valid_var_name(name) -> bool:
    valid_chars = all(c.isalpha() or c == "_" or c.isdigit() for c in name)
    return valid_chars and not name[0].isdigit()

def _parse_for_constants(lines) -> dict:
    constants = {}
    for line in lines:
        if "=" in line:
            key, value = line.split("=")
            constants[key.strip()] = int(value)

def _parse_for_globals(file) -> dict:
    return None

# Find all constants and statics (globals), and return as key value pairs
def ret_static_and_const(lines) -> tuple[dict, dict]:
    return (_parse_for_constants(lines), _parse_for_globals(lines))
