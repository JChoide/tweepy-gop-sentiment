# Author: Jason Chang
clc <- function() cat(rep("\n",50))
# clc() function to add space
rm(list=ls()) # clears environment
cat("\014")   # clears console
search()      # displays attached variables

# Table of word frequency per valence rating
sentiment<-data.frame("-5"=c(6,0,0,1,0),"-4"=c(46,8,1,2,0), "-3"=c(94,0,4,6,0), "-2"=c(210,19,10,6,6), "-1"=c(136,37,8,69,2), 
                      "1"=c(106,19,1,8,14), "2"=c(137,11,2,66,7), "3"=c(54,9,1,6,9), "4"=c(49,1,1,0,4), "5"=c(0,0,0,0,0))
rownames(sentiment)<-c("Donald Trump", "Jeb Bush", "Marco Rubio", "Ben Carson", "Ted Cruz")   # changes row names

# Adds columns to the table: Negative (total number of negative words), Positive (total number of positive words),
# Negative Proportion (propotion of rated words that are negative), and Positive Proportion (vice versa)
sentiment=transform(sentiment, Negative=rowSums(sentiment[,1:5]), Positive=rowSums(sentiment[,6:10]), 
                    NegativeProportion=rowSums(sentiment[,1:5])/rowSums(sentiment), 
                    PositiveProportion=rowSums(sentiment[,6:10])/rowSums(sentiment))
colnames(sentiment)[1:10]<-c(-5:-1,1:5)   # changes column names

# Prints sentiment table
print(sentiment)  
