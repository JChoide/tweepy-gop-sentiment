# Author: Jason Chang

# Libraries needed
from pandas import *
import numpy as np
import matplotlib.pyplot as plt
import re
import collections
import operator

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
# AFINN file location
file_name = 'C:\Users\changj7\Dropbox\Coursera_DataSci\\assignment1\AFINN-111.txt'
afinn_file = open(file_name)                # loads/opens AFINN sentiment file
scores = {}                                 # initialize an empty dictionary of sentiment scores
for line in afinn_file:                     # for loop to load data into dictionary (format)
    term, score = line.split("\t")          # The file is tab-delimited; "\t" means "tab character"; sets term variable to first value separated by tab and score variable to second value
    scores[term] = int(score)               # Convert the score to an integer and stores the value associated to the term key

index = np.array(range(5))
ranking = DataFrame(columns=('Name', 'Sentiment Score', 'Number of Tweets'), index = index)

# Determines sentiment score of each candidate
# Counts number of tweets per candidate
for candidate in tweets:                                        # loop through each tweet in tweet data
    sentiments = []                                             # empty list to store sentiment scores
    count = 0
    for row in tweets[candidate]:
        if row is False:
            pass
        else:
            count += 1
            final_string = str.split(row)                       # splits words up into a list
            for term in final_string:                           # assigns score to words
                if term in scores.keys():                       # if it is a scored word, add to sentiments list
                    sentiments.append(scores[term])
                else:                                           # otherwise it gets a score of 0
                    pass
    print candidate
    print "Sentiment Score:", sum(sentiments)
    print "Number of Tweets:", count
    print "Average Rating:", sum(sentiments) / len(sentiments)
    if candidate == "Donald Trump":                               
        counter1 = collections.Counter(sentiments)                                  # Dictionary of word frequency per valence rating
        print counter1
        sorted_counter1 = sorted(counter1.items(), key=operator.itemgetter(0))      # Sorts above dictionary by key
        print sorted_counter1
    elif candidate == "Jeb Bush":
        counter2 = collections.Counter(sentiments)
        print counter2
        sorted_counter2 = sorted(counter2.items(), key=operator.itemgetter(0))
        print sorted_counter2
    elif candidate == "Marco Rubio":
        counter3 = collections.Counter(sentiments)
        print counter3
        sorted_counter3 = sorted(counter3.items(), key=operator.itemgetter(0))
        print sorted_counter3
    elif candidate == "Ben Carson":
        counter4 = collections.Counter(sentiments)
        print counter4
        sorted_counter4 = sorted(counter4.items(), key=operator.itemgetter(0))
        print sorted_counter4
    else:
        counter5 = collections.Counter(sentiments)
        print counter5
        sorted_counter5 = sorted(counter5.items(), key=operator.itemgetter(0))
        print sorted_counter5
    print

# Plot settings
index = np.arange(-5, 6)
bar_width = 0.8
opacity = 0.8

# Donald Trump Valence Spread
plt.subplot(211)
plt.bar(counter1.keys(), counter1.values(), bar_width, alpha=opacity, color='g')
plt.xticks(index + bar_width/2, index)
plt.xlabel("Valence Rating")
plt.ylabel("Number of Words")
plt.title("Donald Trump")

# Jeb Bush Valence Spread
plt.subplot(245)
plt.bar(counter2.keys(), counter2.values(), bar_width, alpha=opacity, color='r')
plt.xticks(index + bar_width/2, index, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Valence Rating", fontsize=10)
plt.ylabel("Number of Words", fontsize=10)
plt.title("Jeb Bush", fontsize=10)

# Marco Rubio Valence Spread Plot
plt.subplot(246)
plt.bar(counter3.keys(), counter3.values(), bar_width, alpha=opacity, color='orange')
plt.xticks(index + bar_width/2, index, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Valence Rating", fontsize=10)
plt.ylabel("Number of Words", fontsize=10)
plt.title("Marco Rubio", fontsize=10)

# Ben Carson Valence Spread Plot
plt.subplot(247)
plt.bar(counter4.keys(), counter4.values(), bar_width, alpha=opacity, color='y')
plt.xticks(index + bar_width/2, index, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Valence Rating", fontsize=10)
plt.ylabel("Number of Words", fontsize=10)
plt.title("Ben Carson", fontsize=10)

# Ted Cruz Valence Spread Plot
plt.subplot(248)
plt.bar(counter5.keys(), counter5.values(), bar_width, alpha=opacity, color='b')
plt.xticks(index + bar_width/2, index, fontsize=10)
plt.yticks(fontsize=10)
plt.xlabel("Valence Rating", fontsize=10)
plt.ylabel("Number of Words", fontsize=10)
plt.title("Ted Cruz", fontsize=10)
plt.subplots_adjust(hspace=.4)
plt.subplots_adjust(wspace=.5)

plt.show()
