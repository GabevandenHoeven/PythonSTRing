#!/bin/bash
#SBATCH --time=01:30:00
#SBATCH --cpus-per-task=2
#SBATCH --mem 8G
#SBATCH --mail-user g.c.w.vandenhoeven-2@umcutrecht.nl
#SBATCH --mail-type ALL

module load python/3.6.1
python $1 $2 $3
