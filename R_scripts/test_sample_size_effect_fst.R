#!/usr/bin/env Rscript
## Load or install and load libraries
ver_load_packages<-function(...) {
  libs<-unlist(list(...))
  req<-unlist(lapply(libs,require,character.only=TRUE))
  need<-libs[req==FALSE]
  if(length(need)>0){ 
    install.packages(need)
    lapply(need,require,character.only=TRUE)
  }
}
list.of.packages <- c("vcfR", "rlang", "devtools", "hierfstat", "dplyr", "poppr")
ver_load_packages(list.of.packages)

## Load Funcitons:
# Function to randomly sample inds_per_sample-1 individuals per npops populations from an x hierfstat-dataframe object
random_sample<- function(x, inds_per_sample, npops){
  pop_lim = inds_per_sample
  data<-data.frame()
  current_pop = 1
  for (pop in (1:npops)){
    pop_size = 0
    data_tmp <- data.frame()
    for (indv in (1:nrow(x))){
      if (x$pop[indv] == current_pop){
        data_tmp <- rbind(x[indv,], data_tmp)
        pop_size = pop_size+1
      }
    }
    if (pop_size >= pop_lim){
      data <- rbind(data_tmp[sample(1:nrow(data_tmp), (pop_lim-1)),], data)
    } 
    else {
      data <- rbind(data_tmp[(1:nrow(data_tmp)),], data)
    }
    current_pop = current_pop + 1
  }
  return(data)
}

## Set working directory:
cat("Set working directory: ") 
work_dir <- readLines(con="stdin", 1)
setwd(work_dir)
## Enter the PREFIX used throughout the script:
cat("Enter VCF prefix: ")
vcf_prefix <- readLines(con="stdin", 1)
## We use a mapfile as the one used in the program Stacks to define populations. One individual and population per line, separated by \t
cat("Enter mapfile: ")
mapfile <- readLines(con = "stdin", 1)
## load VCF:
Pdepint2 = read.vcfR(paste0(vcf_prefix,".recode.vcf"))
## Convert VCF to genind object:
GI_Pdepint2 = vcfR2genind(Pdepint2)
## Define and assign individuals to populations:
pop_def <- read.table(mapfile, sep = '\t')
GI_Pdepint2@pop <- as.factor(pop_def[,2])
## Convert genind to hierfstat-dataframe object:
hPdepint <- genind2hierfstat(dat=GI_Pdepint2, pop = as.numeric(GI_Pdepint2$pop))
rownames(hPdepint) <- rownames(GI_Pdepint2@tab)
hPdepint_2 <- genind2hierfstat(dat=GI_Pdepint2, pop = GI_Pdepint2$pop)
rownames(hPdepint_2) <- rownames(GI_Pdepint2@tab)

## Getting the number of samples and number of populations:
pop_count <- hPdepint%>%count(pop)
sampl_size <- min(pop_count[,2])
npopus <- length(pop_count[,2])

## Start main routine:
total <- list()
for (iteration in (1:50)){
  total[[iteration]]<-matrix(ncol = 4, nrow = 4)
  row_res = 1
  for (k in (3:6)){
    data<-random_sample(hPdepint, k, npopus)
    data<-dplyr::arrange(data, pop)
    pwfboots<-boot.ppfst(data, nboot=100, quant = c(0.025,0.975), diploid = TRUE)
    print(pwfboots)
    total[[iteration]][row_res, 1] <- k-1
    total[[iteration]][row_res, 2] <- sum(pwfboots$ll, na.rm = T)/(((npopus*npopus)-npopus)/2)
    total[[iteration]][row_res, 3] <- sum(pwfboots$ul, na.rm = T)/(((npopus*npopus)-npopus)/2)
    fstmedi<- matrix(nrow = nrow(pwfboots$ul), ncol = ncol(pwfboots$ul))
    for (i in seq(2,ncol(pwfboots$ll))){
      for (j in seq(1,nrow(pwfboots$ll))){
        fstmedi[j,i]<-(pwfboots$ll[j,i]+pwfboots$ul[j,i])/2
      }
    }
    total[[iteration]][row_res, 4] <- sum(fstmedi, na.rm = T)/(((npopus*npopus)-npopus)/2)
    row_res = row_res + 1
    print(paste('bootstap', k, 'run done'))
  }
  print(paste('Total iteration', iteration,'DONE'))
}
save(total, file = "total_runs_sample_effect")

results <- matrix(nrow = 4, ncol = 4)
colnames(results) <- c('n', 'low_lim', 'up_lim', 'avg')
for (k in (1:50)){
  for (j in (1:4)){
    for (i in (1:4)){
      results[j,i] <- (sum(total[[k]][j,i])/50)*10
    }
  }  
}
for (j in (2:4)){
  for (i in (1:4)){
    results[i,j]<-round(results[i,j],4)
  }
}
write.csv(results, file = paste0(vcf_prefix, '_random_sample_effect.csv'), row.names = F, quote = F)

