# file_processor.py

def create_input_file():
    """Creates a file named input.txt with sample content."""
    try:
        # Define the content to be written to the file
        content = """This is the first line of the input file.
Python file handling is a fundamental concept.
We will read this content, process it, and write to a new file.
Counting words and converting to uppercase are the main tasks.
Let's see the final result in output.txt."""
        
        # Open input.txt in write mode ('w') and write the content
        with open('input.txt', 'w') as f:
            f.write(content)
        print("Successfully created 'input.txt'.")
    except IOError as e:
        print(f"Error creating input file: {e}")
        return False
    return True

def process_file():
    """Reads input.txt, processes its content, and writes to output.txt."""
    try:
        # Step 1: Read the contents of input.txt
        with open('input.txt', 'r') as f:
            content = f.read()
            
        # Step 2: Count the number of words
        # Split the content by whitespace to get a list of words
        words = content.split()
        word_count = len(words)
        
        # Step 3: Convert all text to uppercase
        processed_text = content.upper()
        
        # Step 4: Write the processed text and word count to output.txt
        with open('output.txt', 'w') as f:
            f.write("--- PROCESSED CONTENT ---\n")
            f.write(processed_text)
            f.write("\n\n--- STATISTICS ---\n")
            f.write(f"Word Count: {word_count}\n")
            
        # Step 5: Print a success message
        print("✅ Success! 'output.txt' has been created with the processed content and word count.")
        
    except FileNotFoundError:
        print("Error: 'input.txt' not found. Please create it first.")
    except IOError as e:
        print(f"An error occurred during file processing: {e}")

# Main execution block
if __name__ == "__main__":
    # First, create the necessary input file
    if create_input_file():
        # If the input file was created successfully, process it
        process_file()
