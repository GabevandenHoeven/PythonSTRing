#!/bin/bash

# Script to run analysis with LobSTR for a BAM file.
# Parameters are:
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
