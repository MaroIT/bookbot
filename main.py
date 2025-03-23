from stats import get_num_words, count_characters
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
    
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filepath = sys.argv[1]
        text = get_book_text(filepath)
        num_words = get_num_words(text)
        characters = count_characters(text)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {filepath}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")
        for k, v in characters.items():
            print(f"{k}: {v}")
        print("============= END ===============")
        
main()