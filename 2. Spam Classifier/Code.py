import os
import codecs
import random

#CREATING THE DATA STRUCTURES

def read_in(folder):
    files = os.listdir(folder)
    a_list = []
    for a_file in files:
        if not a_file.startswith("."):
            file_path = os.path.join(folder, a_file)  #there was a problem with the og. code, which was not joining the path and archive name correctly.
            f = codecs.open(file_path, "r", encoding="ISO-8859-1", errors="ignore")
            a_list.append(f.read())
            f.close()
    return a_list

spam_list = read_in("enron1/spam") 
print(len(spam_list))
print(spam_list[0])

ham_list = read_in("enron1/ham") 
print(len(ham_list))
print(ham_list[0])

#SHUFFLING THE DATA
all_emails = [(email_content, "spam") for email_content in spam_list]
all_emails += [(email_content, "ham") for email_content in ham_list]
random.seed(42)
random.shuffle(all_emails)
print (f"Dataset size = {str(len(all_emails))} emails")

#TOKENIZING THE DATA

import nltk
from nltk import word_tokenize

def get_features(text): 
    features = {}
    word_list = [word for word in word_tokenize(text.lower())]
    for word in word_list:
        features[word] = True
    return features

all_features = [(get_features(email), label) for (email, label) in all_emails]

print(get_features("Participate In Our New Lottery NOW!"))
print(len(all_features))
print(len(all_features[0][0]))
print(len(all_features[99][0]))

from nltk import NaiveBayesClassifier, classify

def train(features, proportion):
    train_size = int(len(features) * proportion)
    # initialise the training and test sets
    train_set, test_set = features[:train_size], features[train_size:]
    print (f"Training set size = {str(len(train_set))} emails")
    print (f"Test set size = {str(len(test_set))} emails")
    # train the classifier
    classifier = NaiveBayesClassifier.train(train_set)
    return train_set, test_set, classifier

train_set, test_set, classifier = train(all_features, 0.8)

def evaluate(train_set, test_set, classifier):
    # check how the classifier performs on the training and test sets
    print (f"Accuracy on the training set = {str(classify.accuracy(classifier, train_set))}")
    print (f"Accuracy on the test set = {str(classify.accuracy(classifier, test_set))}")    
    # check which words are most informative for the classifier
    classifier.show_most_informative_features(50)

# EXERCISE 2.7: CLASSIFY THE EMAILS IN ENRON2 WITH THE ALREADY TRAINED CLASSIFIER

test_spam_list = read_in("enron2/spam/")
print(len(test_spam_list))
print(test_spam_list[0])
test_ham_list = read_in("enron2/ham/")
print(len(test_ham_list))
print(test_ham_list[0])

test_emails = [(email_content, "spam") for email_content in test_spam_list]
test_emails += [(email_content, "ham") for email_content in test_ham_list]
random.shuffle(test_emails)

new_test_set = [(get_features(email), label) for (email, label) in test_emails]

evaluate(train_set, new_test_set, classifier)

# EXERCISE 2.7 B: CLASSIFYING THE COMBINED DATASET OF ENRON1 AND ENRON2

spam_list = read_in("enron1/spam/") + read_in("enron2/spam/")
print(len(spam_list))
ham_list = read_in("enron1/ham/") + read_in("enron2/ham/")
print(len(ham_list))

all_emails = [(email_content, "spam") for email_content in spam_list]
all_emails += [(email_content, "ham") for email_content in ham_list]
random.shuffle(test_emails)

all_features = [(get_features(email), label) for (email, label) in all_emails]
print(len(all_features))

train_set, test_set, classifier = train(all_features, 0.8) #it is training the classifier once again, but now with the complete data
evaluate(train_set, new_test_set, classifier) # we're classifying the emails from enron1 with the classifier trained with enron1 + enron2 data. confusing, i know.