#!/bin/bash
snscrape -n 100 --jsonl --with-entity --progress twitter-user JLMelenchon >JLMelenchon.json
snscrape -n 100 --jsonl --with-entity --progress twitter-user JLMelenchon >JLMelenchon.json

for i in Macron Lepen Poutou Zemmour Arthaud Dupont-Aignan Hidalgo Jadot Lassalle Mélenchon Pécresse Roussel
do

 snscrape -n 100 --jsonl --with-entity --progress twitter-hashtag $i >./Output/${i}_hashtags.json
done