#!/bin/bash

# This script is meant to transform the bam files into fastq files for the tool STRetch

#SBATCH --time=02:00:00
#SBATCH --mem=16G
#SBATCH --cpus-per-task=15
#SBATCH --mail-type=ALL
#SBATCH --mail-user=g.c.w.vandenhoeven-2@umcutrecht.nl

FILES="/hpc/diaggen/users/Gabe/data/wes/GIAB/*"
OUTPUT="/hpc/diaggen/users/Gabe/data/wes/GIAB/FastQ/"

module load sambamcram/samtools/1.7

for f in $FILES
do
 if [ -f "$f" ]
 then
  if [ ${f: -4} == ".bam" ]
   then
    echo "Processing $f"
    FILE1=${f%.bam}_R1.fastq.gz
    FILE2=${f%.bam}_R2.fastq.gz
  
    samtools fastq -@ 15 $f -1 $FILE1 -2 $FILE2 -0 /dev/null -s /dev/null -n

    mv $FILE1 $OUTPUT
    mv $FILE2 $OUTPUT
  fi  
 else
  echo "Warning something went wrong with \"$f\""
 fi
done
