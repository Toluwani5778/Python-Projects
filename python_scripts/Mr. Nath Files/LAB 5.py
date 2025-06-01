def tweet_data(file_name):
    read_handle = open(file_name, encoding="utf8")
    lines = read_handle.readlines()
    return lines

def tweet_sender(lines):
    list_senders = []
    for line in lines:
        splits = line.split("|")
        list_senders.append(splits[1])
    return list_senders

def tweets(lines):
    list_tweets = []
    for line in lines:
        splits = line.split("|")
        list_tweets.append(splits[2])
    return list_tweets

def get_hashtags(tweet):
    hashtags = []
    words = tweet.split()
    for word in words:
        if word.startswith("#"):
            hashtags.append(word)
    return hashtags

def get_mentions(tweet):
    mentions = []
    words = tweet.split()
    for word in words:
        if word.startswith("@"):
            mentions.append(word.rstrip(":"))
    return mentions
#_________________________________________________________________________________________________________________________________________________________________________

def main():
    lines  =  tweet_data("twenty-tweets.txt")
    text_list = tweets(lines)
    for twt in text_list:
        list_hashtags = get_hashtags(twt)
        print("Current hashtag Count:", len(list_hashtags))
        print("-----------------------------------------------------------------")
        
        mentions_list = get_mentions(twt)
        print("Current mention Count:", len(mentions_list))
        print("_________________________________________________________________\n")
    
main()
