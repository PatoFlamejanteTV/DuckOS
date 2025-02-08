import os

def list_files():
    for file in os.listdir('.'):
        print(file)

def show_file_content(filename):
    try:
        with open(filename, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print(f"File '{filename}' not found.")
    except Exception as e:
        print(f"An error occurred: {e}")