#!/bin/bash
read -ep "GFF File: " b
read -ep "Prefix: " c
awk '{ if ($3 ~ /mRNA/ || /tRNA/) print $9}' $b | gsed 's/;/\t/g' | gsed 's/ /\t/g' | awk '{ print $2,$13}' | sed 's/Parent=//' | sed 's/Ontology_term=//' |sed 's/\"//g'| awk '{ if ($2 ~/GO:/) print $0 }' > $c'_allGO.txt'
# if Petunia inflata genome is being used, then the column is $13;
# if Petunia axillaris genome is being used, the the column is $14.