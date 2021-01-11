read -ep "VCF1: " a
read -ep "VCF2: " b
grep -v "#" $a | cut -f1,2 > SNPs1.txt
grep -v "#" $b | cut -f1,2 > SNPs2.txt
awk 'NR==FNR{a[$1,$2];next} ($1,$2) in a' SNPs1.txt SNPs2.txt > result.txt