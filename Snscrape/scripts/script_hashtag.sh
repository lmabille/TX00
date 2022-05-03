#!/bin/bash

rm ./Snscrape/Output/*.json
for i in Macron Lepen Poutou Zemmour Arthaud Dupont-Aignan Hidalgo Jadot Lassalle Mélenchon Pécresse Roussel
#date jusque jour -1 pour le until
do
 snscrape -n 1000 --jsonl --with-entity --progress twitter-search "since:2022-01-01 until:2022-04-11 #$i" >./Snscrape/Output/$i.json
done