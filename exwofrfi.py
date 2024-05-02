import re
import argparse

def extract_words(file_path):
    try:
        with open(file_path, 'r') as file:
            text = file.read()
            words = re.findall(r'\b\w+\b', text)
            unique_words = set(words)
            return unique_words
    except FileNotFoundError:
        print("Error: File not found.")
        return set()

def main():
    parser = argparse.ArgumentParser(description="Extract unique words from a file.")
    parser.add_argument("file", help="Path to the input file")
    args = parser.parse_args()

    file_path = args.file
    unique_words = extract_words(file_path)

    print("Unique words extracted from '{}':".format(file_path))
    for word in sorted(unique_words):
        print(word)

if __name__ == "__main__":
    main()
