def read_tweets_from_file(file_name):
    
    reader_handle   = open(file_name)
    actual_lines    = reader_handle.readlines()
    
    return actual_lines


def tweets_processing(tweet_lines):
    count = 0
    for line in tweet_lines:
        count += 1
        
        print("Line number: ", count)
        
        
        
        
        
        if len(splits) == 2:
        
            # print("Sent at: ", splits[0])
            print("The handle of the person tweeted: ", splits[0])  
            print("Tweet: ", splits[1])      
        # print("My current line is: ", line)
        
        print("\n-------------------------------\n")
   
   
def extract_tweeters(tweet_lines):
    tweet_handles = []

    for line in tweet_lines:
        splits = line.split("|")
        
        if len(splits) == 2:
            splits = line.split("|")
            tweet_handles.append(splits[0])

    return tweet_handles 
            
def extract_tweets(tweet_lines):
    tweet_extracted = []

    for line in tweet_lines:
        splits = line.split("|")
        
        if len(splits) == 2:
            splits = line.split("|")
            tweet_extracted.append(splits[1])

    return tweet_extracted
   
        
def find_hashtags(tweet):
    hashtags_found = []
    words = tweet.split()
    for word in words:
        if word.startswith("#"):
            hashtags_found.append(word)
    return hashtags_found
    
def find_mentions(tweet):
    mentions_found = []
    words = tweet.split()
    for word in words:
        if word.startswith("@"):
            mentions_found.append(word)
    return mentions_found    
    
    
def main():
    
    ### call the read_tweets_from_file()
    tweet_lines = read_tweets_from_file("tweet-dataset.txt")
    
    print("The number of lines: ", len(tweet_lines))
    
    # for tweet in tweet_lines:
    #     print(tweet)
    
        
    ## calling all other functions
    # tweets_processing(tweet_lines)
    
    ### calling extract_tweets()
    list_tweeters = extract_tweeters(tweet_lines)
    
    
    list_tweets = extract_tweets(tweet_lines)
    
    for tweet in list_tweets:
                
        hashtags_found = find_hashtags(tweet)
        print("Tweet contains hashtags: ", tweet)        
        if len(hashtags_found) > 0:             
            print("Number of hashtags found: ", len(hashtags_found))
    
        mentions_found = find_mentions(tweet)
        if len(mentions_found) > 0: 
            print("Number of mentions found: ", len(mentions_found))
        
    

    # for handle in list_tweeters:
    #
    #     print("Current Tweet without handle: ", handle)
        

                

        # hashtags = find_hashtag(tweet)
        # for hashtag in hashtags:
        #     print("\tHashtag: ", hashtag)
        print("\n------------------------------\n")
    

main()    
