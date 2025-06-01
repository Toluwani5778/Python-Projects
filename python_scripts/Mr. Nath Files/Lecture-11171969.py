def read_dictionary(file_name):
    file_handle = open(file_name)
    words_equv_lines = file_handle.readlines()
    return words_equv_lines
    
def main():
    dictionary_file_name = "english-czech-dicttionary.txt"
    
    eng_czch_words = read_dictionary(dictionary_file_name)
    for line in eng_czch_words:
        print(line)
    
    
main()        