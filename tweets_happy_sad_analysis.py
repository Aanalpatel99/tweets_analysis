tweets = [
    "Wow, what a great day today!! #sunshine",
    "I feel sad about the things going on around us. #covid19",
    "I'm really excited to learn Python with @JovianML #zerotopandas",
    "This is a really nice song. #linkinpark",
    "The python programming language is useful for data science",
    "Why do bad things happen to me?",
    "Apple announces the release of the new iPhone 12. Fans are excited.",
    "Spent my day with family!! #happy",
    "Check out my blog post on common string operations in Python. #zerotopandas",
    "Freecodecamp has great coding tutorials. #skillup"
]

number_of_tweets = 10
happy_words = ['great', 'excited', 'happy', 'nice', 'wonderful', 'amazing', 'good', 'best']
sad_words = ['sad', 'bad', 'tragic', 'unhappy', 'worst']
sample_tweet = tweets[0]
print(sample_tweet)

is_tweet_happy = False

# Get a word from happy_words
for word in happy_words:# Check if the tweet contains the word
    if word in sample_tweet:# Word found! Mark the tweet as happy
        is_tweet_happy = True
print(is_tweet_happy)

# store the final answer in this variable
number_of_happy_tweets = 0
i=0

# perform the calculations here
for i in happy_words:
    for j in tweets:
        if i in j:
            number_of_happy_tweets+=1
print("Number of happy tweets:", number_of_happy_tweets)
happy_fraction =number_of_happy_tweets/number_of_tweets
print("The fraction of happy tweets is:", happy_fraction)


# store the final answer in this variable
number_of_sad_tweets = 0

# perform the calculations here
for i in sad_words:
    for j in tweets:
        if i in j:
            number_of_sad_tweets+=1
print("Number of sad tweets:", number_of_sad_tweets)
sad_fraction = number_of_sad_tweets/number_of_tweets
print("The fraction of sad tweets is:", sad_fraction)

# Calculate the sentiment score, which is defined as the difference betweek the fraction of happy tweets and the fraction of sad tweets.
sentiment_score = happy_fraction - sad_fraction
print("The sentiment score for the given tweets is", sentiment_score)

if happy_fraction > sad_fraction:
    print("The overall sentiment is happy")
else:
    print("The overall sentiment is sad")

# store the final answer in this variable
number_of_neutral_tweets = 0

# perform the calculation here
number_of_neutral_tweets= number_of_tweets-(number_of_happy_tweets+number_of_sad_tweets)
print(number_of_neutral_tweets)
neutral_fraction = number_of_neutral_tweets/number_of_tweets
print('The fraction of neutral tweets is', neutral_fraction)
