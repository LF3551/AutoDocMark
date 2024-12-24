import sys
from markitdown import MarkItDown

def main():
    if len(sys.argv) != 2:
        print("Usage: python convert_to_markdown.py <file_path>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = input_file.rsplit(".", 1)[0] + ".md"

    try:
        md = MarkItDown()
        result = md.convert(input_file)

        with open(output_file, "w") as f:
            f.write(result.text_content)

        print(f"File '{input_file}' successfully converted to '{output_file}'")
    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred while converting '{input_file}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
