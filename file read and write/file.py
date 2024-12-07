def read_and_write_file(input_file, output_file):
    """
    Reads a file, modifies its content, and writes to a new file.

    Parameters:
    - input_file: str, the name of the input file
    - output_file: str, the name of the output file
    """
    try:
        # Open the input file and read its content
        with open(input_file, 'r') as infile:
            content = infile.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()
        
        # Open the output file and write the modified content
        with open(output_file, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to '{output_file}'.")
    
    except FileNotFoundError:
        print(f"The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'input.txt'  # Replace with the name of your input file
output_file = 'output.txt'  # Replace with the name of your output file

# Example: Writing sample content to the input file
with open(input_file, 'w') as f:
    f.write("This is a sample file content.")

# Call the function
read_and_write_file(input_file, output_file)

# Verify the output by reading the new file
with open(output_file, 'r') as f:
    print("Content in the output file:", f.read())
