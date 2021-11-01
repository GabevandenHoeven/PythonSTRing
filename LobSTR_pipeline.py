import os
import subprocess
import sys


def analysis_pipeline(in_d, out_d):
    """Calls a shell script while looping over a given directory.

    :param in_d: str - path to the directory with the BAM files that need to be analysed.
    :param out_d: str - path to the output directory.
    """
    for filename in os.listdir(in_d):
        if filename.endswith(".bam"):
            # prefix = out_d + filename.split("/")[-1].removesuffix(".bam")
            prefix = out_d + filename.split("/")[-1].replace(".bam", "")
            subprocess.run(f"singularity shell -B /hpc/diaggen:/hpc/diaggen "
                           f"/hpc/diaggen/software/singularity_cache/lobster_v4.0.0.img")
            subprocess.run(f"allelotype --command classify --bam {filename} "
                           f"--noise_model /hpc/diaggen/users/Gabe/tools/lobSTR/models/illumina_v3.pcrfree "
                           f"--strinfo /hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/lobstr_v3.0.2_hg19_strinfo.tab "
                           f"--index-prefix /hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/lobstr_hg19_ref/lobSTR_ "
                           f"--out {prefix}")


if __name__ == "__main_":
    print("Staring analysis pipeline...")
    # pc_dir = "/hpc/diaggen/users/Gabe/data/wes/Positive_controls/"
    # giab_dir = "/hpc/diaggen/users/Gabe/data/wes/GIAB/"
    analysis_pipeline(sys.argv[1], sys.argv[2])
    print("Analysis complete.")



