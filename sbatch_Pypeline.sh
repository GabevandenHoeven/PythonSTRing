#!/bin/bash
#SBATCH --time=1:00:00
#SBATCH --c=2
#SBATCH --mem 5G
#SBATCH --mail-user g.c.w.vandenhoeven-2@umcutrecht.nl
#SBATCH --mail-type ALL

module load python/3.6.1
python /home/cog/gvandenhoeven/repos/PythonSTRing/$1