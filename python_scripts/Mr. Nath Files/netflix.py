def read_file(file_name):
    read_handle = open(file_name)
    read_handle.readline()
    lines = read_handle.readlines()
    return lines

def netflix(lines):
    movie_dict = {}
    excluded = [0,4,6]
    for line in lines:
        metadata = []
        attribute = line.strip("\n").split(",")
        time_attribute = (attribute[4],attribute[6])

        for index in range(0,len(attribute)):
            if index not in excluded:
                metadata.append(attribute[index])

        key = attribute[0]
        movie_dict[key] = [time_attribute, metadata]
        
        for element in movie_dict:
            print("Key:", element)
            print("Values:", movie_dict[element],"\n")

            for value in movie_dict[element]:
                print(type(value))
                print(value)
                print("========================================\n")
              
        my_keys = movie_dict.keys()
        print(type(my_keys))
        print(my_keys)
        print("========================================\n")

        key_set = set(my_keys)
        print(type(key_set))
        print(key_set)
        print("=========================================\n")

        key_list = list(key_set)
        print(type(key_list))
        print(key_list)
        print("=========================================\n")

        my_values = movie_dict.values()
        movie_types = []

        for element in my_values:
            movie_types.append(element[1][0])

        movie_type_set = set(movie_types)                                             
        print("There are", len(movie_type_set), "unique movie types in this dictionary.\n They are:")

        for movie_type in movie_type_set:
            print(movie_type)
                  
def main():
    file = read_file("netflix_titles.csv")
    netflix(file)
if __name__ == "__main__":
    main()
