def find_hashtags(tweet):
    list_hashtags = []
    words = tweet.split()
    for word in words:
        if word.startswith("#"):
            list_hashtags.append(word)
    return list_hashtags


def find_mentions(tweet):
    list_mentions = []
    words = tweet.split()
    for word in words:
        if word.startswith("@"):
            list_mentions.append(word)
    return list_mentions


def word_count(tweet):
    words = tweet.split()
    return len(words)


def main():
    
    list_tweets = []
    for index in range(0,5):
        tweet = input("Enter your tweet here: ")
        list_tweets.append(tweet)
        
    for twt in list_tweets:
        print("\nReading current tweet...\n")
        print(twt)
        
        print("\nThe length of the current tweet is:", len(twt), "Characters")

        count = word_count(twt)
        print("The word count of the current tweet is:", count)
        print("\n---------------------------Hashtag Statistics---------------------------\n")

        list_hashtags = find_hashtags(twt)
        print("The Hashtag count is:", len(list_hashtags))

        for ht in list_hashtags:
            print("Cuurent hashtag:", ht)
        print("\n---------------------------Mention Statistics---------------------------\n")
        
        list_mentions = find_mentions(twt)
        print("The mention count is:", len(list_mentions))

        for men in list_mentions:
            print("The current mention is:", men)
            
        print("__________________________________________________________________________\n")
main()

#Python is one of the easiest and best #programming_language i've ever learned @python @ahamed @python_learners
# professor @ahamed is an good #programmer and #Best_professor
# we will be the future #coding #masters @python @ash_garo @mangtoya @diwash @dane @raymond @bryce
# thanks to professor @ahamed for #teaching us to be an #independent_coder
#Norwich_University is really #amazing @Nu @NorwichUniversity #vermont #northfield
