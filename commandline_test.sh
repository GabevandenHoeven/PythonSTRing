#!/bin/bash
#SBATCH --time=0:05:00
#SBATCH --c=2
#SBATCH --mem 5G
#SBATCH --mail-user g.c.w.vandenhoeven-2@umcutrecht.nl
#SBATCH --mail-type ALL

echo "$1"
echo "$2"