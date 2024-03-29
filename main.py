import os
import subprocess

def display_tree_structure():
    cwd = os.getcwd()
    result = subprocess.run(['tree', cwd], capture_output=True, text=True)
    if result.returncode == 0:
        print("This is my project structure:\n")
        print(result.stdout)
    else:
        print("Error executing 'tree' command:", result.stderr)

def display_contents(start_path):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            file_path = os.path.join(root, file)
            print(f"{file_path}:")
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    print(f.read())
            except Exception as e:
                print(f"Error reading file {file_path}: {e}")
            print("\n" + "-"*20 + "\n")  # Separator between files

def main():
    display_tree_structure()
    print("Displaying contents of each file:\n")
    cwd = os.getcwd()
    display_contents(cwd)

if __name__ == "__main__":
    main()
