import os
from typing import List
import easyocr
import argparse

reader = easyocr.Reader(['en', 'es'], gpu=False)


def scan(path_name: str) -> str:
    read_text = reader.readtext(str(path_name))
    recognized_text = " ".join(elem[1] for elem in read_text)

    return recognized_text


def keyword_match(directory: str, keyword: str) -> List[str]:
    matching_files = []
    for root, dir, files in os.walk(directory):
        for file in files:
            if files.endswith('.jpg', '.pdf', '.png', '.jpeg'):
                image_path = os.path.join(root, file)
                read_text = scan(image_path)
                if keyword.lower() in read_text.lower():
                    matching_files.append(image_path)

    return matching_files


def convert_files(directory: str, target_dir: str):
    for root, dir, files in os.walk(directory):
        for file in files:
            if files.endswith('.jpg', '.pdf', '.png', '.jpeg'):
                image_path = os.path.join(root, file)
                read_text = scan(image_path)
                file_dest = os.path.join(target_dir, file)
                f = open(f"{file_dest}.txt", "w")
                f.write(read_text)


def main():
    parser = argparse.ArgumentParser(description="OCR Parser over images")
    parser.add_argument("-sd", "--source_directory", type: str, help="Directory to read from")
    parser.add_argument("-td", "--target_directory", type: str, help="Directory to output text files to")
    parser.add_argument("-i", "--image", type: str, help="Single file to process")
    parser.add_argument("-k", "--keyword", type: str, help="Keyword to search for")

    args = parser.parse_args()

    if args.source_directory and args.target_directory:
        convert_files(args.source_directory, args.target_directory)
    elif args.source_directory and args.keyword:
        paths = keyword_match(args.source_directory, args.keyword)
        print(f"Images containing {keyword}")
        for path in paths:
            print(path)
        user_input = input("Would you like to convert these to text files? (y/n) ")
        if user_input.lower() is "y":
            new_dir = input("Please specify a directory: ")
            convert_files(args.source_directory, new_dir)
    elif args.image and args.keyword:
        text = scan(args.image)
        if args.keyword.lower() in text.lower():
            print(f"{args.keyword} found in {args.image}")
            print(f"Text: {text}")
        else:
            print(f"{args.keyword} not found.")

if __name__ == "__main__":
    main()
