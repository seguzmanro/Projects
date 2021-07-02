#!/bin/bash -i
read -ep "Gene List: " a
read -ep "BLAST Data Base: " b
read -ep "Prefix: " c
read -p "DB Type: " d
grep -v "#" $a | awk '{print $1,$2,"-",$3}' | sed 's/ - /-/g' > $c'_temp1.txt'
blastdbcmd -db $b -dbtype $d -entry_batch $c'_temp1.txt' -out $c'_sequences.fasta'
rm $c'_temp1.txt'
