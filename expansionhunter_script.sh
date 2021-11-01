#!/bin/bash

# This is a script that will call ExpansionHunter to perform an analysis using variable input
#
# "reads" need to be in a BAM file
# "output-prefix" is the name you want the output files to have
# "sex" is either "female" -default- or "male"
# Additional parameters
#--region-extension-length int \


/hpc/diaggen/users/Gabe/tools/ExpansionHunter-v5.0.0-linux_x86_64/bin/ExpansionHunter \
--reads $1 \
--reference /hpc/diaggen/data/databases/ref_genomes/Homo_sapiens.GRCh37.GATK.illumina/Homo_sapiens.GRCh37.GATK.illumina.fasta \
--variant_catalog /hpc/diaggen/users/Gabe/tools/ExpansionHunter-v5.0.0-linux_x86_64/variant_catalog/hg19/variant_catalog.json \
--output-prefix $2 \
--sex $3
