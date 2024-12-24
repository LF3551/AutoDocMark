# AutoDocMark: Streamline Document-to-Markdown Workflows

**AutoDocMark** leverages the **MarkItDown** library to convert documents into Markdown files. Use it effectively within your virtual environment.

## Installation

To use MarkItDown in a virtual environment, follow these steps:

1. Create a virtual environment:

   ```bash
   python3 -m venv my_markitdown_env
   source my_markitdown_env/bin/activate
```

2. Install MarkItDown directly from the repository:

   ```bash
   pip install git+https://github.com/microsoft/markitdown.git
```

## Usage

### Single File Conversion
Convert a document file into Markdown using the provided convert_to_markdown.py script. Specify the input file as an argument:

```bash
python convert_to_markdown.py <file_path>
```

For example:
```bash
python convert_to_markdown.py example.docx
```

After execution, a Markdown file (e.g., example.md) will be created in the same directory as the input file.

## Features
1. Flexible Input: Specify any supported document format (PDF, DOCX, XLSX, etc.).
2. Simple Interface: Easy command-line usage for converting files.
3. Customizable Output: Automatically saves the converted Markdown file in the same directory.

## Supported Formats

MarkItDown supports the following file types:

- PDF
- Word (DOCX)
- Excel (XLSX)
- PowerPoint (PPTX)
- Images (with OCR capabilities)
- Audio files (with speech transcription)
- HTML
- CSV, JSON, XML
- ZIP files (processes contents)
