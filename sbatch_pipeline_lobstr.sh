#!/bin/bash
##SBATCH --time=08:00:00
##SBATCH --cpus-per-task=8
##SBATCH --mem 32G
##SBATCH --mail-user g.c.w.vandenhoeven-2@umcutrecht.nl
##SBATCH --mail-type ALL

module load python/3.6.1
# $1 - LobSTR_pipeline.py
# $2 - Directory with input BAM files
# $3 - Directory used for output files

python $1 $2 $3

singularity exec -B /hpc/diaggen/:/hpc/diaggen/ /hpc/diaggen/software/singularity_cache/rocker-tidyverse-3.5.1.img
Rscript plot_results_lobstr.R