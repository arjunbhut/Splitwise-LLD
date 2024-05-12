from sys import argv
from input_handler import *
def main():
    
    """
    Sample code to read inputs from the file
    """
    if len(argv) != 2:
        raise Exception("File path not entered")
    file_path = argv[1]
    f = open(file_path, 'r')
    lines = f.readlines()
    input_manager(lines)
    
if __name__ == "__main__":
    main()