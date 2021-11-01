#!/bin/bash

# Dit is een script wat met twee input velden een lobSTR analyse draait voor een bam file.
# parameters zijn:
# $1 : absolute/path/bam_file.bam
# $2 : absolute/path/output_prefix

singularity shell -B /hpc/diaggen:/hpc/diaggen /hpc/diaggen/software/singularity_cache/lobster_v4.0.0.img

allelotype \
--command classify \
--bam $1 \
--noise_model /hpc/diaggen/users/Gabe/tools/lobSTR/models/illumina_v3.pcrfree \
--strinfo /hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/lobstr_v3.0.2_hg19_strinfo.tab \
--index-prefix /hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/lobstr_hg19_ref/lobSTR_ \
--out $2
