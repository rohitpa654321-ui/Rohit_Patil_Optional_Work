import os

def list_directory_contents(path='.'):
    """
    List and print the contents of the specified directory.
    Defaults to the current working directory if no path is given.
    """
    try:
        contents = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"Error: The directory '{path}' was not found.")
    except PermissionError:
        print(f"Error: Permission denied to access '{path}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
if __name__ == "__main__":
    directory_path = input("Enter the path to the directory (leave blank for current directory): ").strip()
    if not directory_path:
        directory_path = '.'  # Default to current directory
    list_directory_contents(directory_path)
