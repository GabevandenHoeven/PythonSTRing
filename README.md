# PythonSTRing

## This repository was used for a study towards the use of STR calling tools with whole exome sequencing data in a diagnostic environment. This study was commissioned by the genetic diagnostics department at the UMC Utrecht.
#### The bash script "sbatch_Pypeline.sh" was used to commit Python pipelines to the Slurm workload manager for automatic analyses of sample BAM files in a given directory.
#### For the tools ExpansionHunter and LobSTR separate bash scripts have been made that were customised for these tools and include implementation of an Rscript to plot and visualise results.
#### These bash scripts must be given the Python pipeline and full paths to the input and output directories as arguments.
#### Python pipelines for ExpansionHunter LobSTR and STRetch can be found in this repository, along with conversion scripts for output files into a CSV file for ExpansionHunter and LobSTR.
#### The Python script "Processing_LobSTR.py" was used in the study to filter results for genes AR, ATXN3, C9ORF72 and DMPK as these were the genes that were included in the study.
####
