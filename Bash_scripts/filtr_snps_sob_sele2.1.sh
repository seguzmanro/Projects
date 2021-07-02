read -ep "VCF: " a
read -p "PCAdapt or BayeScan? " e
grep -v "#" $a | cut -f1,2 > positions.txt
sn=$( grep -v "#" $a | wc -l | sed 's/   //')
seq 1 $sn > numbers.txt
paste numbers.txt positions.txt > fullpositions.txt
rm numbers.txt positions.txt
read -ep "Positions: " b
c=$(cat $b | head -1 | sed 's/"//g' | sed 's/ //')
if [ $c = x ]
then 
cat $b | awk '{ print $2}' | sed "s/$'\n/'$'\t'$'\t'$'\t'$'\t'$'\t'$'\n'/g" > pos2.txt
awk 'NR==FNR{a[$1];next} ($1) in a' pos2.txt fullpositions.txt > result.txt
rm fullpositions.txt pos2.txt
else
awk 'NR==FNR{a[$1];next} ($1) in a' $b fullpositions.txt > result.txt
rm fullpositions.txt
fi
d=$(echo $a | sed 's/.recode.vcf//') 
cat result.txt | cut -f2,3 > $d'_list_snp_sob_sele_'$e'.txt'
rm result.txt
RED='\033[0;31m'
NC='\033[0m'
echo " Your file is ready at $d _list_snp_sob_sele_$e.txt" 
