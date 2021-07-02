#!/bin/bash
read -ep "ANN VCF: " a
read -ep "Prefix: " b
grep -v "#" $a | cut -f8 | cut -d ";" -f42 > $b'_Annotations.csv'
cat $b'_Annotations.csv' | cut -d "|" -f2,4,17,19,32,34,47,49,62,64,77,79 > $b'_Annotations_ModType-geneID.csv'
cat $b'_Annotations_ModType-geneID.csv' | cut -d "|" -f1,2 > $b'_Annotations_ModType-geneID2.csv'
cat $b'_Annotations_ModType-geneID.csv' | cut -d "|" -f3,4 >> $b'_Annotations_ModType-geneID2.csv'
cat $b'_Annotations_ModType-geneID.csv' | cut -d "|" -f5,6 >> $b'_Annotations_ModType-geneID2.csv'
cat $b'_Annotations_ModType-geneID.csv' | cut -d "|" -f7,8 >> $b'_Annotations_ModType-geneID2.csv'
cat $b'_Annotations_ModType-geneID.csv' | cut -d "|" -f9,10 >> $b'_Annotations_ModType-geneID2.csv'
cat $b'_Annotations_ModType-geneID.csv' | cut -d "|" -f11,12 >> $b'_Annotations_ModType-geneID2.csv'
sed -i '/^$/d' $b'_Annotations_ModType-geneID2.csv'
cat $b'_Annotations_ModType-geneID2.csv' | sed 's/&/_/g' | awk 'BEGIN{ FS="|" } { if ($1 !~ /^synonymous_variant/) print $0 }' > $b'_Annotations_ModType-geneID3.csv'
cat $b'_Annotations_ModType-geneID3.csv' | cut -d "|" -f2 | sort | uniq | sed  's/CHR_START-//g' | sed 's/-CHR_END//g' | sed 's/-/\n/g' | sort | uniq > $b'_GeneNames.txt'
