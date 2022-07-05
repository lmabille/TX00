
import json
import nltk
#nltk.download('punkt')
from nltk.corpus import stopwords

#nltk.download('stopwords')
from nltk.stem.snowball import FrenchStemmer


def extract_tweets(candidate, filter):
    tweets_list = []
    with open("C:/Users/cesar/Desktop/UTC/GI04/TX00/TX00/Snscrape/Output/"+filter+"/"+candidate+".json", "r") as json_file:
        print("Fichier parsé: ", json_file.name)
        json_list = list(json_file)
    for json_str in json_list:
        tweet_json = json.loads(json_str)
        tweets_list.append((tweet_json["date"], tweet_json["content"]))
    return tweets_list

def process_tweets(tweets):
    processed_tweets = []
    for tweet in tweets:
        date = tweet[0]
        content = tweet[1]
        tokenizer = nltk.RegexpTokenizer(r'\w+') #enleve ponctuation
        content_new = nltk.word_tokenize(content)

        #stemmer = FrenchStemmer()
        #test = [stemmer.stem(w) for w in tweet_new] #enleve pluriels et genres
        clean = []
        test = content_new
        for w in test:
           clean+=tokenizer.tokenize(w)

        stopwords_fr = set(nltk.corpus.stopwords.words('french'))
        my_stopwords = ["a", "est"]
        begin_words = ["m'", "l'"]
        sw = list(stopwords_fr) + my_stopwords + begin_words
        final = [w.lower() for w in clean if w not in sw] #enleve mots liaison
        processed_tweets.append((date,final))
    return processed_tweets

def champ_lex_to_list(theme):
    champ_lex = []
    with open("C:/Users/cesar/Desktop/UTC/GI04/TX00/TX00/NLP/"+theme+".txt", "r", encoding="utf-8") as file:
        print("theme: ", file.name)
        lines = file.readlines()
    for line in lines:
        champ_lex.append(line.strip())
    return champ_lex

def tweets_to_theme(tweets):
    list_themes = ["ecologie", "economie", "education", "immigration", "sante", "securite_defense"]
    theme_list_words = {}
    for theme in list_themes:
        theme_list_words[theme] = champ_lex_to_list(theme)
        #print(theme_list_words[theme])
    tweet_and_count = []
    counts_per_theme = {} #{theme1: occurences,..., themen: occurences}
    for tweet in tweets:
        date = tweet[0]
        content = tweet[1]
        for theme in list_themes:
            tweet_count = 0
            for w in theme_list_words[theme]:
                tweet_count += content.count(w) #nombre d'occurences d'un mot du champ lex dans le tweet
            counts_per_theme[theme] = tweet_count
 #-------------------------on compare tous les themes et on affecte au tweet le theme le plus représentatif------------
        max_occ = -1
        max_theme = "init"
        #print("-----------tweet-------------")
        list_occ = list(counts_per_theme.values())
        if list_occ.count(list_occ[0]) == len(list_occ): #si égalité entre les thèmes
            #print("EGALITE")
            pass
        else:
            for theme, occ in counts_per_theme.items():
                #print(theme,":", occ)
                if occ > max_occ:
                    max_occ = occ
                    max_theme = theme
            #print("max",max_theme)
#-------------------------on ajoute le tweet avec son theme correspondant a la liste des tweets-----------------------
            tweet_and_count.append(((date,content), (max_theme, max_occ))) #tuples ( ( (date,content), (max_theme, max occ) ),... )
    return tweet_and_count

def tweets_by_themes(tweets_count):
    tweets_by_themes = {}
    list_themes = ["ecologie", "economie", "education", "immigration", "sante", "securite_defense"]
    for theme in list_themes:
        tweets_by_themes[theme] = []

    for tweet in tweets_count:
        theme = tweet[1][0]
        if theme in list_themes:
            tweets_by_themes[theme].append(tweet)
        else:
            print("error")
    return tweets_by_themes



#-------------------------------------TWEETS BY OFFICIAL ACCOUNT------------------------------------------------------------

def themes_by_candidate_compte(candidate):
    result_dict = {}
    tweets = extract_tweets(candidate, "comptes") #recupere data scrappée
    tweets_cleaned = process_tweets(tweets) #nettoie les tweets
    taux_tweets_lies = []
    nombre_tweets_lies = []

    tweets_occ = tweets_to_theme(tweets_cleaned)  # [(tweet, (champ lex, occ_max)),..,]

    tweets_list_by_theme = tweets_by_themes(tweets_occ) #dictionnaire de listes des tweets par theme

    for theme, list_tweets in tweets_list_by_theme.items():
        #print(theme, list_tweets)
        print("theme: ",theme)
        print(" Taux de tweets liés au thème: {:.2f} %".format((len(list_tweets) / len(tweets_occ)) * 100))
        print(" Nombre de tweets liés au thème: ", len(list_tweets))

        print("--------------------------------------------------------------------------------------------------")
        taux_tweets_lies.append(round(len(list_tweets) / len(tweets_occ) * 100, 4))
        nombre_tweets_lies.append(len(list_tweets))
    print("RATIO TWEETS TROUVES: ", len(tweets_occ),"/",len(tweets_cleaned))
    result_dict["tweets_lies"] = taux_tweets_lies
    result_dict["nombre_tweets_lies"] = nombre_tweets_lies
    return result_dict




#-------------------------------------TWEETS BY HASHTAGS------------------------------------------------------------


def themes_by_candidate_hashtag(candidate):
    result_dict = {}
    tweets = extract_tweets(candidate, "hashtags") #recupere data scrappée
    tweets_cleaned = process_tweets(tweets) #nettoie les tweets
    taux_tweets_lies = []
    nombre_tweets_lies = []

    tweets_occ = tweets_to_theme(tweets_cleaned)  # [(tweet, (champ lex, occ_max)),..,]

    tweets_list_by_theme = tweets_by_themes(tweets_occ) #dictionnaire de listes des tweets par theme

    for theme, list_tweets in tweets_list_by_theme.items():
        #print(theme, list_tweets)
        print("theme: ",theme)
        #print(" Occurence moyenne par tweet: {:.2f}".format(sum_count / len(tweets_occ)))
        print(" Taux de tweets liés au thème: {:.2f} %".format((len(list_tweets) / len(tweets_occ)) * 100))
        #print(" Nombre d'occurence max dans un tweet: ", occ)
        print(" Nombre de tweets liés au thème: ", len(list_tweets))

        print("--------------------------------------------------------------------------------------------------")
        taux_tweets_lies.append(round(len(list_tweets) / len(tweets_occ) * 100, 4))
        nombre_tweets_lies.append(len(list_tweets))
    print("RATIO TWEETS TROUVES: ", len(tweets_occ),"/",len(tweets_cleaned))
    result_dict["tweets_lies"] = taux_tweets_lies
    result_dict["nombre_tweets_lies"] = nombre_tweets_lies
    return result_dict



#-------------------------------------TWEETS BY TIME AND HASHTAGS------------------------------------------------------------



def tweet_by_time_hashtag(candidate):
    count_by_theme = {}
    list_themes = ["ecologie", "economie", "education", "immigration", "sante", "securite_defense"]
    for theme in list_themes:
        count_by_theme[theme] = []
    tweets = extract_tweets(candidate, "hashtags")  # recupere data scrappée
    tweets_cleaned = process_tweets(tweets)  # nettoie les tweets
    tweets_occ = tweets_to_theme(tweets_cleaned)  # [(tweet, (champ lex, occ_max)),..,]
    dates = []

    for tweet in tweets_occ:
        date = tweet[0][0]
        theme = tweet[1][0]
        dates.append(date)
        """
        for curr_theme in list_themes:
            if curr_theme == theme:
                if len(count_by_theme[curr_theme]) == 0: #si 1er parcour, liste vide, alors on append juste
                    new_count = 1
                else: # si pas vide on peut incrémenter
                    new_count = count_by_theme[theme][-1] + 1 #dernier compteur +1
                count_by_theme[theme].append(new_count)
            else:
                if len(count_by_theme[curr_theme]) == 0: #si 1er parcour, liste vide, alors on append juste
                    new_count = 0
                else: # si pas vide on peut incrémenter
                    new_count = count_by_theme[curr_theme][-1] #dernier compteur +1
                count_by_theme[curr_theme].append(new_count)"""
        for curr_theme in list_themes:
            if curr_theme == theme:
                count_by_theme[curr_theme].append(1)
            else:
                count_by_theme[curr_theme].append(0)

    print(len(count_by_theme['ecologie']), len(count_by_theme['economie']), len(tweets_occ), len(tweets_cleaned))
    count_by_theme["date"] = dates
    print(count_by_theme.keys())

    for theme in list_themes: #met dans le sens janvier -> Avril
        count_by_theme[theme].reverse()

    return count_by_theme



#-------------------------------------TWEETS BY TIME AND ACCOUNTS------------------------------------------------------------


def tweet_by_time_account(candidate):
    count_by_theme = {}
    list_themes = ["ecologie", "economie", "education", "immigration", "sante", "securite_defense"]
    for theme in list_themes:
        count_by_theme[theme] = []
    tweets = extract_tweets(candidate, "comptes")  # recupere data scrappée
    tweets_cleaned = process_tweets(tweets)  # nettoie les tweets
    tweets_occ = tweets_to_theme(tweets_cleaned)  # [(tweet, (champ lex, occ_max)),..,]
    dates = []

    for tweet in tweets_occ:
        date = tweet[0][0]
        theme = tweet[1][0]
        dates.append(date)

        for curr_theme in list_themes:
            if curr_theme == theme:
                count_by_theme[curr_theme].append(1)
            else:
                count_by_theme[curr_theme].append(0)

    print(len(count_by_theme['ecologie']), len(count_by_theme['economie']), len(tweets_occ), len(tweets_cleaned))
    count_by_theme["date"] = dates
    print(count_by_theme.keys())

    for theme in list_themes: #met dans le sens janvier -> Avril
        count_by_theme[theme].reverse()

    return count_by_theme





#themes_by_candidate_compte("Fabien_Roussel")
#themes_by_candidate_hashtag()
#tweet_by_time_hashtag("Roussel")