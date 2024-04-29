# PDF OCR Tool

## Overview

This tool is designed to perform Optical Character Recognition (OCR) on .pdf, .jpg, .jpeg, and .png files. It allows users to extract text from documents, making the content searchable and editable.

## Features

- **PDF Text Extraction**: Extract text content from files.
- **Searchable Content**: Convert scanned documents or image-based files into searchable text.
- **File Conversion**: Converts files to .txt for easy of editing or further processing. 

## Installation

1. Clone this repository:

   ```
   git clone https://github.com/LogPRose/NoteConverter.git
   ```

2. Navigate to the project directory:

   ```
   cd NoteConverter 
   ```

3. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the tool and provide the path to the PDF file you want to process:

   ```
   python NoteConverter.py -i example.pdf 
   ```
2. Run the tool with the help flag to see all options:

   ```
   python NoteConverter.py --help 
   ```



## Examples

- Extract text from a PDF file and save it as plain text:

  ```
  python NoteConverter.py --sd /user/Logan/482slides -td /user/Logan/482Notes 
  ```

