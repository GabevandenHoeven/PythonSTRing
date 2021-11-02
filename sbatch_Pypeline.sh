#!/bin/bash
#SBATCH --time=4:00:00
#SBATCH --cpus-per-task=4
#SBATCH --mem 16G
#SBATCH --mail-user g.c.w.vandenhoeven-2@umcutrecht.nl
#SBATCH --mail-type ALL

module load python/3.6.1
python /home/cog/gvandenhoeven/repos/PythonSTRing/$1 $2 $3
