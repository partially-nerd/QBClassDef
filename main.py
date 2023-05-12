from BP import Transpiler
from sys import argv

if len(argv) != 3:
    print("ERROR: I/O files not defined. Pass them in as positional arguments")
    exit()

transpiler = Transpiler(file=argv[1])
transpiler.transpile()
transpiler.write_to_file(file=argv[2])
