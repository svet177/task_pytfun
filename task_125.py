import os
import shutil

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32

def process_temperature_file(file_path):
    """Process the temperature file, converting Celsius to Fahrenheit and saving to a new file."""
    try:
        # Check if the file has a .txt extension
        if not file_path.endswith('.txt'):
            raise ValueError("Unsupported file extension. Please provide a .txt file.")
        
        # Check if the file exists
        if not os.path.isfile(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")

        # Read the file and process each line
        with open(file_path, 'r') as file:
            lines = file.readlines()

        processed_lines = []
        for line in lines:
            line = line.strip()
            if line.endswith('C'):
                try:
                    temp_c = float(line[:-1])
                    temp_f = celsius_to_fahrenheit(temp_c)
                    processed_lines.append(f"{temp_f:.2f}F")
                except ValueError:
                    raise ValueError(f"Unexpected string format: '{line}'. Expected format is a numeric value followed by 'C'.")
            elif line.endswith('F'):
                # Keep the Fahrenheit value as it is
                processed_lines.append(line)
            else:
                raise ValueError(f"Unexpected string format: '{line}'. Expected format is a numeric value followed by 'C' or 'F'.")

        # Prepare the output file path
        directory, filename = os.path.split(file_path)
        file_root, file_ext = os.path.splitext(filename)
        output_file_path = os.path.join(directory, f"{file_root}_processed{file_ext}")

        # Check if there's enough disk space
        total, used, free = shutil.disk_usage(directory)  # Get disk space in bytes
        needed_space = len('\n'.join(processed_lines).encode('utf-8'))
        
        if needed_space > free:
            raise OSError("Not enough disk space to save the output file.")

        # Write the processed data to the output file
        with open(output_file_path, 'w') as output_file:
            output_file.write('\n'.join(processed_lines))
        
        print(f"Processed data has been saved to '{output_file_path}'.")

    except FileNotFoundError as fnf_error:
        print(fnf_error)
    except ValueError as val_error:
        print(val_error)
    except PermissionError:
        print("Permission denied: Unable to save the output file. Please check your permissions.")
    except OSError as os_error:
        print(os_error)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    # Ask the user for the path to the .txt file
    file_path = input("Please enter the path to the .txt file: ")
    process_temperature_file(file_path)

if __name__ == "__main__":
    main()
