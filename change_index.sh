#!/bin/bash

# This script changes the name of the index so that ExpansionHunter can use them

#SBATCH --time=00:05:00
#SBATCH --mem=5G
#SBATCH --cpus-per-task=2
#SBATCH --mail-type=ALL
#SBATCH --mail-user=g.c.w.vandenhoeven-2@umcutrecht.nl

FILES="/hpc/diaggen/users/Gabe/data/wes/GIAB/*"
for f in $FILES
do
 if [ -f "$f" ]
  then
   if [ ${f: -4} == ".bai" ]
    then
     FILE1=${f%.bai}.bam.bai
     mv $f $FILE1
   fi 
 fi 
done
