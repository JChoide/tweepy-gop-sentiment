# Author: Jason Chang

# Libraries needed
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import re

# Location of file that contains all the tweets
file_path = "C:\Users\changj7\Dropbox\Projects\GOPSentiment\output.txt"
tweet_file = open(file_path)

# Loads tweets into a list
tweets_data = []
for line in tweet_file:
    tweets_data.append(line)
print 'Total Number of Tweets:', len(tweets_data), '\n'


# Finds if a phrase is in a line of text
def word_in_text(word, text):             # determines if word is in tweet
    word = word.lower()                   # converts word to lowercase
    text = text.lower()                   # converts full tweet to lowercase
    matches = re.search(word, text)       # searches for word in tweet
    if matches:                           # if it matches, print true, else print false
        return text
    else:
        return False

# Data frame of all tweets associated with each candidate
tweets = DataFrame()                                                                            # creates tweet data frame
tweets['Donald Trump'] = map(lambda tweet: word_in_text("Donald Trump", tweet), tweets_data)    # Donald Trump tweet column (returns false if no DT text)
tweets['Jeb Bush'] = map(lambda tweet: word_in_text("Jeb Bush", tweet), tweets_data)            # Jeb Bush tweet column
tweets['Marco Rubio'] = map(lambda tweet: word_in_text("Marco Rubio", tweet), tweets_data)      # Marco Rubio tweet column
tweets['Ben Carson'] = map(lambda tweet: word_in_text("Ben Carson", tweet), tweets_data)        # Ben Carson tweet column
tweets['Ted Cruz'] = map(lambda tweet: word_in_text("Ted Cruz", tweet), tweets_data)            # Ted Cruz tweet column

# Creates AFINN dictionary (word sentiment dictionary)
afinn_file = open("AFINN-111.txt")          # loads/opens AFINN sentiment file
scores = {}                                 # initialize an empty dictionary of sentiment scores
for line in afinn_file:                     # for loop to load data into dictionary (format)
    term, score = line.split("\t")          # The file is tab-delimited; "\t" means "tab character"; sets term variable to first value separated by tab and score variable to second value
    scores[term] = int(score)               # Convert the score to an integer and stores the value associated to the term key


# Creates data frame for sentiment data to be loaded into
index = np.array(range(5))
ranking = DataFrame(columns=('Name', 'Sentiment Score', 'Number of Tweets'), index = index)

# Determines sentiment score of each candidate
# Counts number of tweets per candidate
index = 0                                   # initializes index variable
for candidate in tweets:                    # loop through each tweet in tweet data
    sentiments = []                         # empty list to store sentiment scores
    count = 0                               # initializes counting variable for tweets
    for row in tweets[candidate]:
        if row is False:
            pass
        else:
            count += 1                                          # increments counting variable (number of tweets)
            final_string = str.split(row)                       # splits words up into a list
            for term in final_string:                           # assigns score to words
                if term in scores.keys():                       # if it is a scored word, add to sentiments list
                    sentiments.append(scores[term])
                else:                                           # otherwise, continue loop
                    pass
    ranking.loc[index] = np.array([candidate, sum(sentiments), count])  # stores information in row index of data frame
    index += 1                                                          # increments index variable
    print candidate                                                     # candidate name
    print "Sentiment Score:", sum(sentiments)                           # total of sentiment scores
    print "Number of Tweets:", count                                    # number of tweets
    print                                                               # new line

print ranking
ranking = ranking.convert_objects(convert_numeric=True)         # converts values to numeric

# Plot for Sentiment Total per Candidate
f, ax = plt.subplots()                                        
ax.set_xlabel("Candidate", fontsize=12)
ax.set_ylabel("Sentiment Score", fontsize=12)
ax.set_title("GOP Presidential Candidate Sentiment Rating", fontsize=16)
colors = ['r', 'r', 'r', 'g', 'g']
ranking.plot(x='Name', y='Sentiment Score', ax=ax, kind='bar', color=colors)
plt.plot([-7, 7], [0, 0], lw=3, color='black')
plt.xticks(rotation=0)
plt.grid()
ax.legend_.remove()

# Plot for Number of Tweets per Candidate
f, ax = plt.subplots()                                           
ax.set_xlabel("Candidate", fontsize=12)
ax.set_ylabel("No. of Tweets", fontsize=12)
ax.set_title("GOP Presidential Candidate Tweet Count", fontsize=16)
ranking.plot(x='Name', y='Number of Tweets', ax=ax, kind='bar', color='blue')
plt.xticks(rotation=0)
plt.grid()
ax.legend().set_visible(False)

plt.show()  # shows plots
