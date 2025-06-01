# Name: Amarnath
# Assignment 4: Final Assignment
# Course: Intro to Python Programming
# Scope: Python Dictionary Data Structures, Files, Text
# Description: Taking a word in English, converting it to Morse code, and Vice Versa
# Resources: https://www.onlinewebtoolkit.com/morse-code
# Input file: https://math.hws.edu/eck/cs225/s03/code.txt
# Due date: Wednesay December 8th, at 23:55
# Submission Instruction: delivery includes python source code, and screenshots of all output

# TOTAL POINTS: 40 POINTTS
# NO LATE SUBMISSIONS WILL BE ACCEPTED -- NO EXCEPTIONS!
#______________________________________________________________________________________________________________________________________

# [5 POINTS]
# You are given the input file above, which contains the Alphabets and its equivalence
# your task is to read the file one line at a time as we did (English-Czech)in class on Monday
# write a function called read mc file()
# the function takes the file name, and the path if you downloaded it in another directory
# The function should return a list of the lines

def read_mc_file(file_name):
    read_file = open(file_name)
    lines = read_file.readlines()
    return lines 
#______________________________________________________________________________________________________________________________________

# [5 POINTS]
# using the list of the lines, you will process the lines one line at a time
# you will split each line to the two components: the English Letter and the Mores code equivalent symbol
# write a function that takes the list of lines called is eg to mc()
# the function will take the list of lines created from the previous function above
# the function will construct a dictionary eg mc dict,
### the key will be the Englsih letters and the values are the MC symboles
# the function will return a fully populated dictionary that you can look up for englsih letters

def eg_to_mc(lines):
    eg_mc_dict = {}
    temp = {}
    for line in lines:
        cons = line.split(" ")
        temp[cons[0]] = cons[1]
    for key, value in temp.items():
        new_value = value.rstrip("\n")
        eg_mc_dict[key] = new_value
    return eg_mc_dict
             

#______________________________________________________________________________________________________________________________________

# [5 POINTS]
# using the list of the lines, you will process the lines one line at a time
# you will split each line to the two components: the English Letter and the Mores code equivalent symbol
# write a function that takes the list of lines called is mc to eg()
# the function will take the list of lines created from the previous function above
# the function will construct a dictionary mc eg dict,
### the key will be the MC symbols and the values are the English letters
# the function will return a fully populated dictionary that you can look up for MC symbols

def mc_to_eg(lines):
    mc_eg_dict = {}
    temp = {}
    for line in lines:
        cons = line.split(" ")
        temp[cons[1]] = cons[0]
    for value,key in temp.items():
        new_value = value.rstrip("\n")
        mc_eg_dict[key] = new_value
    return mc_eg_dict


#______________________________________________________________________________________________________________________________________

# [5 POINTS]
# write a funtion called word MC translator)
# the function takes a word in English and returns the equivalent symbols

def get_word():
    get = input("Enter word/s to convert to morse code: ")
    word = get.upper()
    return word

def word_MC_translator(dictionary):
    word = get_word()
    
    t_word = []
    for letter in word:
        for key, value in dictionary.items():
            if key == letter:
                t_word.append(value)

    return " ".join(t_word)


#______________________________________________________________________________________________________________________________________

# [5 POINTS]
# write a funtion called MC word translator()
# the function takes a set of MC symbols and returns the equivalent word in English

def get_morse():
    code = input("Enter morse code/s to convert to word: ")
    morse = code.split(" ")
    return morse

def MC_word_translator(dictionary):
    word = get_morse()
    
    t_word = []
    for letter in word:
        for key, value in dictionary.items():
            if value == letter:
                t_word.append(key)

    return "".join(t_word)

#______________________________________________________________________________________________________________________________________
def line():
    print("________________________________________________________________________")
    
def process(lines):
    ask = "y"
    while ask == "y":
        
        ques = input("Select an option (1 or 2) below\n\t(1) Convert Word to Morse Code\n\t(2) Convert Morse Code to Word\nPlease enter your response here: ")    

        if ques == "1":
            translation_1 = eg_to_mc(lines)
            work_1 = word_MC_translator(translation_1)
            print("\t\tTranslated Morse Code:",work_1)
            line()
            
        elif ques == "2":
            translation_2 = mc_to_eg(lines)
            work_2 = MC_word_translator(translation_2)
            print("\t\tTranslated Word:",work_2)
            line()
            
        else:
            print("\nSorry, the number you entered is invalid!")
            
        ask = input("Would you like to try again? (y/n) ")
        print()
    return ask

#______________________________________________________________________________________________________________________________________

# [15 POINTS]
# write a main function that prompt for a type of input (English or MC)
# write another input that asks for the actual English/MC input accordingly
# if the input is a set of MC inputs, called the MC word translator()
# if the input is an English word, call the word MC translator()

# Answer: I created a seperate function called process to do all the work in this section so that the code looks so neat and readable.

def main():
    
    lines = read_mc_file("morse code.txt")
    process(lines)
    
main()


#______________________________________________________________________________________________________________________________________

# [10 POINTS]
# for each type, provide 2 input types
### 20 English words (eg carrot, planet, fish, desert, trees, biodiversity, data science)
### and 20 set of symbols

# Answer: 20 word translation takes too much screenshots so as you said i tranlsated 5 from each respectfully.
### and i apologize that i didn't submit my coding screenshots because that would be about 4-5 screenshots.

### Thanks for this assignment, professor.
