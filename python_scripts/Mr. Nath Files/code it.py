def main():
    handle = open("Electoral_College.csv")
    handle.readline()
    records = handle.readlines()

    max_year = 0
    current_state = ""
    
    for record in records:
        
        current_max = max_year
        splits = record.split(",")
        current_state = splits[1]
        
        if int(splits[0]) > max_year:
            max_year = splits[0]

