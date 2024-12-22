import re

def add_blank_line_before_badges(filepath):
    """Adds a blank line between the description and badge line in a Markdown file."""
    try:
        with open(filepath, 'r') as file:
            content = file.read()
    except FileNotFoundError:
        print(f"Error: File not found at path: {filepath}")
        return

    # Regex pattern to find description followed by the badge
    pattern = re.compile(r"([^\n])\n\[!", re.MULTILINE)
    
    # Replace with description, two newlines, and the badge line
    modified_content = pattern.sub(r"\1\n\n[!", content)

    try:
        with open(filepath, 'w') as file:
            file.write(modified_content)
        print(f"Successfully modified: {filepath}")
    except IOError:
        print(f"Error: Could not write to file: {filepath}")

if __name__ == "__main__":
    file_path_input = input("Please enter the path to your markdown file: ")
    add_blank_line_before_badges(file_path_input)