import csv

import re

import matplotlib.pyplot as plt

import pandas as pd

from nltk.corpus import stopwords

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.model_selection import train_test_split

from sklearn.naive_bayes import MultinomialNB

class CleanAndTest:

    def filter_data(self):

        with open("out.csv") as csvfile:
            reader = csv.reader(csvfile)

            for row in reader:

                for string in row:
                    string = re.sub('[^ ]+\.[^ ]+', '', string)  # regex to remove URL and substitute with a space

                    emoji_pattern = re.compile("["
        
                                               u"\U0001F600-\U0001F64F"  # emoticons
        
                                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
        
                                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
        
                                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
        
                                               u"\U00002702-\U000027B0"
        
                                               u"\U000024C2-\U0001F251"
        
                                               "]+", flags=re.UNICODE)  # removing emoticons

                    string = emoji_pattern.sub(r'', string)

                    string = string.strip()

                    string = re.sub(" \d+", " ", string)

        comments = pd.read_csv("out.csv", sep='\t', names=['comment'])

        import string


        def clean_text(cstring):
            nopunc = [char for char in cstring if char not in string.punctuation]

            nopunc = "".join(nopunc)

            return ([word for word in nopunc.split() if word.lower() not in stopwords.words("english")])


        df = comments['comment'].head(500).apply(clean_text)

        df.replace('\n', 'NaN')

        df.replace(' ', 'NaN')

        df.dropna(axis=0, how='any', inplace=True)

        i = 0

        with open("out111.csv", "a") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')

            for i in range(0, 450):

                str1 = ' '.join(str(e) for e in df[i])

                if (str1 != '\n' and str1 != ''):

                    csv_file.write(str1 + "\n")

                else:

                    continue

        data_train = pd.read_csv("DataSet.csv", encoding="latin-1")

        data_testing = pd.read_csv("out111.csv", encoding="latin-1", names=["Comment"])

        labels = data_train.Sentiment

        data_train = data_train.drop('ItemID', 1)

        X = data_train.SentimentText

        y = data_train.Sentiment

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.66, random_state=61)

        X_test = data_testing.Comment

        Mn = MultinomialNB()

        # label=data_train

        vectorizer = CountVectorizer(stop_words='english')

        vectorizer.fit(X_train)

        # print(vectorizer.get_feature_names())

        X_train_dtm = vectorizer.transform(X_train)

        X_test_dtm = vectorizer.transform(X_test)

        # print(X_test_dtm)


        nb = MultinomialNB()

        nb.fit(X_train_dtm, y_train)

        y_predict_class = nb.predict(X_test_dtm)

        print(y_predict_class)

        count0 = 0

        count1 = 0

        for i in y_predict_class:

            if (i == 1):

                count1 += 1

            else:

                count0 += 1

        perc1 = (count1 / (count1 + count0)) * 100

        perc0 = (count0 / (count1 + count0)) * 100

        print("Percentage of positive comments:", perc1, "\nPercentage of negative comments:" , perc0)

        print("Number of positive comments", count1, "\nNumber of Negative comments", count0)

        labels = 'Positive', 'Negative'

        sizes = [perc1, perc0]

        fig1, ax1 = plt.subplots()

        ax1.pie(sizes, labels=labels, autopct='%1.1f%%',

                shadow=True, startangle=90)

        ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

        plt.title('Sentiment Analysis')

        plt.show()

        fig2, ax2 = plt.subplots()

        ax2.bar(("Positive", "Negative"), (perc1, perc0))

        plt.show()

        fig3, ax3 = plt.subplots()

        ax3.bar(("Positive Comments", "Negative Comments"), (count1, count0))

        plt.show()

