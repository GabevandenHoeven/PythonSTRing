#!/bin/bash
#SBATCH --time=1:00:00
#SBATCH --nodes=2
#SBATCH --mem 5G
#SBATCH --gres=tmpspace:10G
#SBATCH --mail-user g.c.w.vandenhoeven-2@umcutrecht.nl
#SBATCH --mail-type ALL
#SBATCH --export=NONE
#SBATCH --account=diaggen
#
# This is a script that will call ExpansionHunter to perform an analysis using variable input
#
# "reads" need to be in a BAM file
# "output-prefix" is the name you want the output files to have
# "sex" is either "female" -default- or "male"

/hpc/diaggen/users/Gabe/tools/ExpansionHunter-v5.0.0-linux_x86_64/bin/ExpansionHunter \
--reads $1 \
--reference /hpc/diaggen/data/databases/ref_genomes/Homo_sapiens.GRCh37.GATK.illumina/Homo_sapiens.GRCh37.GATK.illumina.fasta \
--variant-catalog /hpc/diaggen/users/Gabe/tools/ExpansionHunter-v5.0.0-linux_x86_64/variant_catalog/hg19/variant_catalog.json \
--output-prefix /hpc/diaggen/users/Gabe/analysis/output_exhunt/$2 \
--region-extension-length 1000 \
--sex $3 \
