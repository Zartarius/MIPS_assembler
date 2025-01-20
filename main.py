import sys
from syntax_checker import check_file_syntax #type: ignore

if check_file_syntax(sys.argv) == False:
    sys.exit(1)