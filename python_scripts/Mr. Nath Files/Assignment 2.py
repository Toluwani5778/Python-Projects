### Name: Amarnath No_Lname
### Section: A
### course: CS142
### Assignment: 2
### total points: 20
### submissions must include the .py file and the screenshot
### submissions without code will resule in 0 score
### submissions without screenshots will immediately be penalized by [-5 points]
### No late submissions will be accepted: only those with accomodations
### Not placing these comments above each question will lead to a penality of [-2 point]



#Defining a dotted line seperation function, so that I dont have to write them again and again.

def space():
  print()
  print("---------------------------------------------------------------------")
  print()

### [2 points]
### create an empty list
### name it list_of_numbers
### define a function that doesn't take an input but return an empty list
### call it create_empty_list()

  
def create_empty_list():
  list_of_numbers = []
  return list_of_numbers

### [3 points]
### using the input() to populate the list with numbers of type (int)
### add immediately to the list
### create a function and call it add_element()
### the function takes a list
### the function returns the list with the number added

def add_element(list_of_numbers):
  num = int(input("Please enter a number: "))
  list_of_numbers.append(num)
  return list_of_numbers

### [2 points]
### now print the elements of the list using a for loop
### your for loop should NOT use an index
### print a meaningful message (ex: "Current Int is:")
### create a function called dump_list()
### the function will take a list as an input
### the function will NOT return but ONLY print the values

def dump_list(list_of_numbers):

  for i in list_of_numbers:
      print("The current number in the list is:", i)

### [3 points]
### now create a new function similar to the find_minimum() from Lab-3
### this time you will use a for loop with an index
### The function will take the list as input and return the minimum of the elements

def find_min(list_of_numbers):
   temp_min = list_of_numbers[0]
   print("My baseline minimum is:", temp_min)
   for i in range(0, len(list_of_numbers)):
      if list_of_numbers[i] < temp_min:
         temp_min = list_of_numbers[i]
   return temp_min

### [3 points]
### yet to be disussed this Friday
### create a function called it flex_size()
### the function will start with an empty list (no need for an input)
### you function will keep asking for int input() until you you say "done"
### the function will call the find_minimum() (that you defined above)
### your function will return the mimimum number()

    
def flex_size():
   flex_list = create_empty_list()
   done = "no"
   while done == "no":
      add_num = add_element(flex_list)
      done = input("Are you done? (done/no): ")
      print()
      if done == "done":
         min = find_min(flex_list)
   return min   

### [1 point]
### create a main() that will be used for testing in the way we demonstrated in class today
### no loose code anywhere in the file, everything goes into the main()


def main():

   ### [2 points]
   ### repeat the two steps above process 2 more times
   ### don't use a for loop
   ### use just one variable name for accepting the input()
      ### here you would simply call the add_element() function twice but passing the new values from the input()

   
   new_list = create_empty_list()
   num = add_element(new_list)
   num = add_element(new_list)
   num = add_element(new_list)
   space()
   
   dump_list(new_list)
   space()
   
   mini = find_min(new_list)
   print("The lowest integer on the given list is:", mini)
   space()
   
   flex_list = flex_size()
   space()
   print("The minimum number on the given list is:", flex_list)
   
main()


### [4 points]
### you will test all the functions with three different meaningful cases

# Since all the functions requires us to enter a number/word, I have attached screenshots of 3 different meaningful cases. 
