def read_file():
    """
    Asks the user for a filename, reads the file content, 
    and handles errors if the file doesn’t exist or can’t be read.
    """
    try:
        # Ask the user for a filename
        filename = input("Please enter the filename: ")
        
        # Try to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Print the content of the file
        print("\nFile content:")
        print(content)
    
    except FileNotFoundError:
        print(f"\nError: The file '{filename}' does not exist.")
    except PermissionError:
        print(f"\nError: You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")

# Call the function
read_file()