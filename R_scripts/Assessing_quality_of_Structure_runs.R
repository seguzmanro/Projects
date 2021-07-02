### This is the path of the harvester output:
setwd('~/Desktop/harvester/')
a <- 26 ## Number of K
b <- 10 ## Number of runs per K

## ---The following command pulls the required info from the "summary.txt" file of 
# Harvester to a new file; The argument 'tail -' needs to be modified as the product 
# of K and the number of runs per K ---
system("cat summary.txt | awk '{if ($1 ~ /[0-9]/) print $0 }' | 
       tail -260  > quality_of_runs.txt")

qualruns<-read.table('quality_of_runs.txt', header = F, sep = '\t', row.names = 1)
qualruns<-qualruns[,-1]
qualruns<-qualruns[,-2:-3]

### Subdivide the main file into K dataframes inside a list:
corr<-list()
for (i in seq(1,(a*b),b)){
  for (j in 1:a){
    if( j==qualruns[i,1]){
      corr[[j]]<-subset(qualruns[i:(i+9),])
    }
  }
}

### Compute the mean and standard deviation for each set of runs of each K:
for (i in 1:a){
  for (j in 1:b){
    corr[[i]][j,3]<-mean(corr[[i]][,2])
    corr[[i]][j,4]<-sd(corr[[i]][,2])
  }
}

### Normalize the Variance of each run, using its mean and sd:
for (i in 1:a){
  for (j in 1:b){
    corr[[i]][j,5]<-((corr[[i]][j,2]-corr[[i]][j,3])/corr[[i]][j,4])
  }
}

### Testing for how many standard deviations the data stands 
## (1.96 = 2 standar deviations in a normal distrib) away from the mean:
for (i in 1:a){
  for (j in 1:b){
    if (corr[[i]][j,5]>1.96){
      corr[[i]][j,6]="out"}
    if (corr[[i]][j,5]<(-1.96)){
      corr[[i]][j,6]="out"}
  else {corr[[i]][j,6]="in"}
  }
}    

### Naming the columns:
for (i in 1:a){
  colnames(corr[[i]])<-c("K", "Variance of Ln likelihood", "Mean", "SD", "Normalized", "in/out")
}

### Printing the K with low quality runs: 
for (i in 1:a){
  for (j in 1:b){
    if (corr[[i]][j,6]=="out"){
      print(corr[[i]][j,1])
    }
  }
}

