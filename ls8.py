"""Main."""

from cpu import *
import sys

argv_err_msg = """Error: You must specify a file name as a command line argument."""

if len(sys.argv) != 2:
    print(argv_err_msg)
    sys.exit(1)

else:
    file_name = sys.argv[1]

cpu = CPU()
cpu.load(file_name)
cpu.run()