# File Read & Write Challenge + Error Handling Lab (Custom Message Version)

def read_and_modify_file(input_filename, output_filename, custom_message):
    try:
        # Open and read the original file
        with open(input_filename, "r") as infile:
            content = infile.read()

        # Modify content by appending a custom message
        modified_content = content + "\n\n" + custom_message

        # Write modified content to a new file
        with open(output_filename, "w") as outfile:
            outfile.write(modified_content)

        print(f"Modified content successfully written to '{output_filename}'.")

    except FileNotFoundError:
        print(f"Error: The file '{input_filename}' does not exist.")
    except PermissionError:
        print(f"Error: You do not have permission to read/write the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Ask user for file names
input_file = input("Enter the filename to read: ")
output_file = input("Enter the new filename to save modified content: ")
message = input("Enter a custom message to append: ")

# Call function
read_and_modify_file(input_file, output_file, message)
