# string and string mainpulation

item_name = 'Biriyani'
print("Type of the Item_name:",type(item_name))

test1 = (item_name.startswith('B'))
test2= (item_name.startswith('b'))

print("The item name '",item_name, "' starts with 'B' ?", test1 )
print("The item name '",item_name, "' starts with 'b' ?", test2 )
print()
print("____________________________________________GAME STARTS____________________________________________")
print()
print("Game: Guess the word")
answer = "false"
while answer == "false":
    print()
    word_name = input("Please enter a word: ")

    if item_name == word_name:
        print("It's correct. You won!!")
        answer = "true"
    else:
        print("Not exactly, try again.")
        answer = "false"
print("______________________________________________GAME END______________________________________________")
print()

item_name_2 = 'Biriyani'

print("Item name in LOWERCASE letters:", item_name.lower())

print("Item name in UPPERCASE letters:",item_name_2.upper())

print("The length of the word is:", len(item_name))


print()
print("----------------------------------------------------------------------------------------------------")
print()
if item_name.lower() == item_name_2.lower():
    print("Is the item",item_name.lower(), "same as the item",item_name_2.lower(), ": YES, it is")
else:
    print("Is the item",item_name.lower(), "same as the item",item_name_2.lower(), ": NO, it is not")
print()
print("----------------------------------------------------------------------------------------------------")
print()
number = input("Please enter a number: ")
print("Type of your entered value without 'int()' is:", type(number))
print()
print("Type of your entered value with 'int()' is:", type(int(number)))
print()
print("The entered number is a digit ('.isdigit()'): ", number.isdigit())
print()
print("The entered number is an alphanumeric number ('.isalnum()') :", number.isalnum())

print()
print("__________________________________________________________________________________________________")
print()

sentence = (input("Enter a sentence: "))
##sentence = "Today I was HAPPY. I did sand art and mask dye, it was so fun and exciting."
print()
print("Type of your entered sentence:",type(sentence))
print()
words = sentence.split()
print("Words: ",words)
print()
print("Type of the words:",type(words))

print()

for word in words:
    if word.lower().startswith('s'):
        print("The word starting with 's' -",word.strip(".").strip(","))
        print()
    elif word.lower().endswith('d'):
        print("The word ending with 'd' - ",word.strip(".").strip(","))
        print()
    elif word.isupper():
        print("The word with Uppercase letters: ",word.strip(".").strip(","))
        print()
print()
print("The words with more than 3 letters are printed below")
words = sentence.split()
print()
for word in words:
    if len(word) > 3:
        print("Word:", word.strip(".").strip(","))
