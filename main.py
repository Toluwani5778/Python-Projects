from stats import get_book_text, get_num_words, get_num_characters, get_sorted_list
import sys

def main():
    """
    Main function to execute the book reading functionality.
    """
    filepath = sys.argv[1]  # Replace with the path to your book file
    text = get_book_text(filepath)
    num_words = get_num_words(text)
    num_characters = get_num_characters(text)
    sorted_char = get_sorted_list(num_characters)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for char in sorted_char:
        for key, value in char.items():
            if key.isalpha():
                print(f"{key}: {value}")
    print("============= END ===============")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    main()