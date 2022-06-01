#!/bin/bash

rm ./Snscrape/Output/comptes/*.json
for i in EmmanuelMacron MLP_officiel PhilippePoutou ZemmourEric n_arthaud dupontaignan Anne_Hidalgo yjadot jeanlassalle JLMelenchon vpecresse Fabien_Roussel
#date jusque jour -1 pour le until
do
 snscrape --jsonl --with-entity --progress twitter-search "from:$i since:2022-01-01 until:2022-04-11" >./Snscrape/Output/comptes/$i.json
done