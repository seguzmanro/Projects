#!/bin/bash
read -ep "Gene Names File: " a
read -ep "GFF File: " b
read -ep "Prefix: " c
awk '{ if ($3 ~ /mRNA/ || /tRNA/) print $1,$4,$5,$9}' $b | sed 's/;/\t/g' | sed 's/ /\t/g' > $c'_temp1.txt'
awk '{ print $1,$2,$3,$5,$13,$14,$15,$16,$17}' $c'_temp1.txt' | sed 's/Parent=//g' > $c'_temp2.txt'
rm $c'_temp1.txt'
echo "#CHR Start End GeneID Functional_ahrd_qcode Functional_annotation Functional_blast_hit Functional_ipr_hit Ontology_term" | sed 's/ /\t/g' > $c'_GeneList.txt'
awk 'NR==FNR{a[$1];next} ($4) in a' $a $c'_temp2.txt' | sed 's/Functional_ahrd_qcode=//g' | sed 's/Functional_annotation="//g' | sed 's/Functional_blast_hit="//g' | sed 's/Functional_ipr_hit=//g' | sed 's/Ontology_term=//g' | sed 's/\"//g'  >> $c'_GeneList.txt'
awk 'NR==FNR{a[$4];next}!($1 in a)' $c'_temp2.txt' $a > $c'_NOGeneList.txt'
rm $c'_temp2.txt'
