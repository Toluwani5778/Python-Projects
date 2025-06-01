def get_book_text(filepath):
    """
    Reads the content of a book from a file and returns it as a string.
    
    :param filepath: Path to the book file.
    :return: Content of the book as a string.
    """
    with open(filepath, 'r', encoding='utf-8') as file:
        return file.read()
    
def get_num_words(text):
    """
    Counts the number of words in a given text.
    
    :param text: The text to count words in.
    :return: Number of words in the text.
    """
    return len(text.split())

def get_num_characters(text):
    """
    Counts the number of characters in a given text.
    
    :param text: The text to count characters in.
    :return: Number of characters in the text.
    """
    text = text.lower()
    return {x: text.count(x) for x in set(text) if x.isalpha() or x.isspace()}    

def get_sorted_list(dictionary):
    """
    Sorts a dictionary by its values in descending order and returns a list of tuples.
    
    :param dict: The dictionary to sort.
    :return: A list of tuples sorted by the dictionary's values in descending order.
    """
    dict_pairs = [{"char": x, "num": y} for x, y in dictionary.items()]
    dict_pairs.sort(key=lambda x: x["num"], reverse=True)
    return [{dict_pair["char"]: dict_pair["num"]} for dict_pair in dict_pairs]
