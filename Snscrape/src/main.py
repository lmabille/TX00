#!/usr/bin/env python3
import json

candidats = ["EmmanuelMacron", "MLP_officiel", "PhilippePoutou", "ZemmourEric", "n_arthaud", "dupontaignan", "Anne_Hidalgo", "yjadot", "jeanlassalle", "JLMelenchon", "vpecresse", "Fabien_Roussel"]
tweets_list = []
old = 0
print()
for candidate in candidats:
    with open(f"/home/lumabill/Documents/TX00/Snscrape/Output/comptes/"+candidate+".json", "r") as json_file:
        # print("Fichier parsé: ", json_file.name)
        json_list = list(json_file)
    for json_str in json_list:
        tweet_json = json.loads(json_str)
        tweets_list.append(tweet_json["content"])
    total = len(tweets_list) - old
    old = len(tweets_list)
    print(f"Nombre de tweets écrits par {candidate}: {total}")
print(f'\nNombre de Tweets écrits par les candidats: {len(tweets_list)}')