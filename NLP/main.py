
import json
import nltk
#nltk.download('punkt')
from nltk.corpus import stopwords

#nltk.download('stopwords')
from nltk.stem.snowball import FrenchStemmer

tweets_list = []

def extract_tweets():
    with open("C:/Users/cesar/Desktop/UTC/GI04/TX00/TX00/Snscrape/Output/Zemmour.json", "r") as json_file:
        print(json_file.name)
        json_list = list(json_file)
    for json_str in json_list:
        tweet_json = json.loads(json_str)
        tweets_list.append(tweet_json["content"])



#tweets_list = ["Bonjour, il y a de nombreuses maisons bleues et vive l'écologie #manu", "je m'appelle Lucien nature important #environement", "Ma voiture est noire #melanchon"]
processed_tweets = []

def process_tweets(tweets):
    for tweet in tweets:
        tokenizer = nltk.RegexpTokenizer(r'\w+') #enleve ponctuation
        tweet_new = nltk.word_tokenize(tweet)

        #stemmer = FrenchStemmer()
        #test = [stemmer.stem(w) for w in tweet_new] #enleve pluriels et genres
        clean = []
        test = tweet_new
        for w in test:
           clean+=tokenizer.tokenize(w)

        stopwords_fr = set(nltk.corpus.stopwords.words('french'))
        my_stopwords = ["a", "est"]
        begin_words = ["m'", "l'"]
        sw = list(stopwords_fr) + my_stopwords + begin_words
        final = [w.lower() for w in clean if w not in sw] #enleve mots liaison
        processed_tweets.append(final)

def champ_lex_to_list():
    champ_lex = []
    with open ("./NLP/economie.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
    for line in lines:
        champ_lex.append(line.strip())
    return champ_lex

def tweets_to_theme(tweets, champ_lex):
    tweet_and_count = []
    for tweet in tweets:
        tweet_count = 0
        for w in champ_lex:
                tweet_count += tweet.count(w)
        tweet_and_count.append((tweet, tweet_count))
    return tweet_and_count

extract_tweets()
champ_eco = champ_lex_to_list()
process_tweets(tweets_list)
count = 0
max_c=0
for tweet in tweets_to_theme(processed_tweets, champ_eco):
    if tweet[1] >0:
        if tweet[1] > max_c:
            max_c = tweet[1]
        count+=1
print((count/len(tweets_to_theme(processed_tweets, champ_eco)))*100)
print(max_c)

