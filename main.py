import sys
import os
import ctypes
from commands.help import *
from commands.about import *
from commands.test.anim import *
from commands.file_ops import *

# Load the shared library
cpp_commands = ctypes.CDLL(os.path.join(os.path.dirname(__file__), 'cpp_commands.so'))

# Define the argument and return types for the writefile function
cpp_commands.writefile.argtypes = [ctypes.c_char_p, ctypes.c_char_p]
cpp_commands.writefile.restype = None

def main():

    # INTRO
    print("Welcome to the DuckOS!")
    print("Type 'help' for a list of commands.")

    print("-------------------")
    
    while True:
        command = input("DUCK@DUCKOS: ").strip().lower()
        
        if command == "help":
            show_help()

        elif command == "about":
            show_about()

        elif command == "exit":
            print("Exiting the application...")
            sys.exit(0)

        elif command == "test":
            print("Jokes/Tests, currently subcmds: anim")

        elif command == "test/anim":
            test_anim()

        elif command == "ls" or command == "dir":
            cpp_commands.cpp_list_files()

        elif command.startswith("cat"):
            filename = command[3:].strip()
            cpp_commands.cpp_show_file_content(filename.encode('utf-8'))

        elif command.startswith("write"):
            parts = command[5:].strip().split(' ', 1)
            if len(parts) == 2:
                filename, content = parts
                cpp_commands.writefile(filename.encode('utf-8'), content.encode('utf-8'))
            else:
                print("Usage: write <filename> <content>")

        else:
            print(f"'{command}' is not a valid command. Type 'help' for a list of commands.")

if __name__ == "__main__":
    main()