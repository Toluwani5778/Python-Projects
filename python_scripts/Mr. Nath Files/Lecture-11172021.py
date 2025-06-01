def read_dictionary_from_file(file_name):
    file_handle = open(file_name)
    words_equv_lines = file_handle.readlines()
    return words_equv_lines


def load_dictionary(dictionary):
    
    ligno_dictinary = {}
    for line in dictionary:
        eng_czech = line.rstrip('\n').split(",")        
        ligno_dictinary[eng_czech[0]] = eng_czech[1]
    
    return ligno_dictinary
    
    
    
    
    
def word_equivelance(english_word, dictionary):
    for line in dictionary:

        eng_czech = line.rstrip('\n').split(",")
        # print("Curent word: ", eng_czech[0])
        if english_word == eng_czech[0]:
            return eng_czech[1]

    return None 
            
    
def main():
    dictionary_file_name = "english-czech-dictionary.txt"
    
    eng_czch_words = read_dictionary_from_file(dictionary_file_name)
    
    word_meaning = load_dictionary(eng_czch_words)
    
    # print(word_meaning["beetroot"])
    
    
    print("The equivalent word for beetroot: ", word_meaning["beetroot"])

    # print("The equivalent word for roastbeef: ", word_meaning["roastbeef"])

    print("The equivalent word for salmon: ", word_meaning["salmon"])
    
    print("The equivalent word for tomatoes: ", word_meaning["tomato"])    
        
    
    
    
    
    # for line in eng_czch_words:
    #     eng_czech = line.rstrip('\n').split(",")
    #     print("The English Word: ", eng_czech[0])
    #     print("The Czech Word: ", eng_czech[1])
    #     print("---------------------------------")
        
    
    
main()        