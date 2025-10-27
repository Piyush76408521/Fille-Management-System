"""Simple file management CLI.

This module provides a tiny command-line file manager with operations to
create, list, delete, read and append to files in the current working
directory. It's intentionally small and educational.

Usage:
    Run the script and follow the menu prompts.

Notes:
    - Functions print status messages rather than returning values because
      the script is interactive and intended for direct user use.
    - Errors are caught and reported to keep the REPL loop running.
"""

import os


def create_file(filename):
    """Create a new file using exclusive creation mode ('x').

    Args:
        filename (str): Path or name of the file to create.

    Behavior:
        - If the file already exists, a FileExistsError is handled and the
          user is informed instead of raising.
        - On success a confirmation message is printed.
    """
    try:
        # 'x' mode ensures we don't overwrite existing files by accident
        with open(filename, 'x') as f:
            print(f"File '{filename}' created successfully!")
    except FileExistsError:
        # A common expected condition; inform the user
        print(f"File '{filename}' already exists!")
    except Exception as E:
        # Catch-all to avoid crashing the interactive loop on unexpected errors
        print(f'An unexpected error occurred during file creation: {E}')


def view_all_files():
    """List files and directories in the current working directory.

    This uses os.listdir() and prints results line-by-line. If the
    directory is empty, the user is informed.
    """
    files = os.listdir()
    if not files:
        print('No files found in the current directory!')
    else:
        print('Files and Directories in Current Directory:')
        for file in files:
            # Print each entry so the user can see what's available
            print(f"- {file}")


def delete_file(filename):
    """Delete the named file from the filesystem.

    Args:
        filename (str): The file to remove. If the file does not exist,
                        the user is notified.
    """
    try:
        os.remove(filename)
        print(f"'{filename}' has been deleted successfully!")
    except FileNotFoundError:
        # User attempted to delete a non-existent file
        print(f"File '{filename}' not found!")
    except Exception as e:
        # Report unexpected errors (permissions, etc.) without crashing
        print(f'An unexpected error occurred during file deletion: {e}')


def read_file(filename):
    """Read and print the entire contents of a text file.

    Args:
        filename (str): The file to open for reading.

    Notes:
        - Reads the whole file into memory; acceptable here because the
          tool is simple. For very large files consider streaming.
    """
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of '{filename}':\n{content}")
    except FileNotFoundError:
        print(f"File '{filename}' doesn't exist!")
    except Exception as e:
        print(f'An unexpected error occurred during file reading: {e}')


def edit_file(filename):
    """Append a single line (user input) to the given file.

    The function opens the file in append mode so existing data is preserved.
    If the file doesn't exist, the user is informed.
    """
    try:
        with open(filename, 'a') as f:
            # Use input() to collect data to append. Append a newline for readability.
            content = input('Enter data to add (will be added on a new line) = ')
            f.write(content + "\n")
            print(f"Content added to '{filename}' successfully! ")
    except FileNotFoundError:
        print(f"File '{filename}' doesn't exist!")
    except Exception as e:
        print(f'An unexpected error occurred during file editing: {e}')


def main():
    """Interactive menu loop for the small file manager.

    The loop continues until the user selects the Exit option. Input is
    stripped to reduce accidental whitespace errors.
    """
    while True:
        # Display a simple textual menu each iteration
        print('\n' + '='*20)
        print('FILE MANAGEMENT APP')
        print('='*20)
        print('1: Create file')
        print('2: View all files')
        print('3: Delete file')
        print('4: Read file')
        print('5: Edit file')
        print('6: Exit')

        choice = input('Enter your choice (1-6) = ').strip()
        print('-'*20)

        # Route the user's choice to the appropriate helper
        if choice == '1':
            filename = input("Enter the file name to create = ").strip()
            create_file(filename)
        elif choice == '2':
            view_all_files()
        elif choice == '3':
            filename = input('Enter the name of file to delete = ').strip()
            delete_file(filename)
        elif choice == '4':
            filename = input('Enter the file name to read = ').strip()
            read_file(filename)
        elif choice == '5':
            filename = input('Enter the name of file to edit/append = ').strip()
            edit_file(filename)
        elif choice == '6':
            print('Closing the app.... Goodbye! 👋')
            break
        else:
            # Handle unexpected input gracefully and continue the loop
            print('Invalid choice. Please enter a number between 1 and 6.')

5
if __name__ == "__main__":
    main()
