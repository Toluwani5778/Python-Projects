#Diwash Bhattarai
#CS 142 A
# Assignment 4: Final Assignmnet
# Course: Intro to Python Programming
# Scope: Python Dictionary Data Structures, Files, Text
# Description: Taking a word in English, converting it to Morse code, and Vice Versa
# Resources: https://www.onlinewebtoolkit.com/morse-code
#Input file: https://math.hws.edu/eck/cs225/s03/code.txt
#Due date: Wednesay December 8th, at 23:55
#Submission Instruction: delivery includes python source code, and screenshots of all output
# TOTAL POINTS: 40 POINTTS
# NO LATE SUBMISSIONS WILL BE ACCEPTED -- NO EXCEPTIONS!

# [5 POINTS]
#You are given the input file above, which contains the Alphabets and its equivalence
# your task is to read the file one line at a time as we did (English-Czech) in class on Monday
# write a function called read_mc_file()
# the function takes the file name, and the path if you downloaded it in another directory
#The function should return a list of the lines
def read_mc_file(file_name):
    read_handle = open (file_name)
    lines = read_handle.readlines( )
    return lines

# [5 POINTS]
# using the list of the lines, you will process the lines one line at a time
# you will split each line to the two components: the English Letter and the Mores code equivalent symbol
# write a function that takes the list of lines called is eg_to_mc()
# the function will take the list of lines created from the previous function above
# the function will construct a dictionary eg_mc_dict,
### the key will be the Englsih letters and the values are the MC symboles# the function will return a fully populated dictionary that you can look up for englsih letters
def eg_to_mc(lines):
    eg_mc_dict={}
    temp_set = {}
    for line in lines:
        e_m_word = line.split(" ")
        temp_set [e_m_word[0]] = e_m_word[1]
    for word, morse in temp_set.items():
        mc= morse.rstrip("\n")
        eg_mc_dict[word] = mc
    return eg_mc_dict

                 
# [5 POINTS]
#using the list of the lines, you will process the lines one line at a time
# you will split each line to the two components: the English Letter and the Mores code equivalent symbol
# write a function that takes the list of lines called is mc_to_eg()                                                                          
# the function will take the list of lines created from the previous function above
# the function will construct a dictionary mc_eg_dict,
### the key will be the MC symbols and the values are the English letters
# the function will return a fully populated dictionary that you can look up for MC symbols
def mc_to_eg(lines ):
    mc_eg_dict = {}
    temp_set = {}
    for line in lines:
        e_m_word = line.split(" ")
        temp_set [e_m_word[1]] = e_m_word[0]
    for word, english in temp_set.items():
        eg= english.rstrip("\n")
        mc_eg_dict[word] = eg
    return mc_eg_dict
       

# [5 POINTS]
# write a funtion called word_MC_translator)
# the function takes a word in English and returns the equivalent symbols
def word_MC_translator(eg_mc_dict):
    Ques = input("Enter a English word in Upper Case: ")
    temp_list = []
    for letter in Ques:
        print (letter)
        for key,value in eg_mc_dict.items():
            print ("key:",key,"value:",value)
            if key == letter:
                print (letter)
                temp_list.append(value)
    return " ".join(temp_list)

# [5 POINTS]
# write a funtion called MC_word_translator()
# the function takes a set of MC symbols and returns the equivalent word in English
def MC_word_translator(mc_eg_dict):
    Ques = input("Enter a Morse code: ")
    temp_list = []
    for letter in Ques:
        print (letter)
        for key,value in mc_eg_dict.items():
            print ("key:",key,"value:",value)
            if key == letter:
                print (letter)
                temp_list.append(value)
    return " ".join(temp_list)

# 15 POINTS]
# write a main function that prompt for a type of input (English or MC)
# write another input that asks for the actual English/MC input accordingly
#if the input is a set of MC inputs, called the MC_word_translator()
# if the input is an English word, call the word_MC_translator()
def main( ):
    lines = read_mc_file("morse code.txt")
    eg_mc_dict = eg_to_mc(lines )
    mc_eg_dict = mc_to_eg(lines )
    word_MC_translator(eg_mc_dict)
    MC_word_translator(mc_eg_dict)
main( )

# [10 POINTS]
# for each type, provide 2 input types
### 20 English words (eg carrot, planet, fish, desert, trees, biodiversity, data science)
### and 20 set of symbols
