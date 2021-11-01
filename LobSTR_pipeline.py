import os
import subprocess
import sys


def analysis_pipeline(d):
    """Calls a shell script while looping over a given directory.

    :param d: str - path to the directory with the BAM files that need to be analysed.
    """
    for filename in os.listdir(d):
        if filename.endswith(".bam"):
            prefix = "/hpc/diaggen/users/Gabe/analysis/output_lobstr/allelotype/" + \
                     filename.split("/")[-1].removesuffix(".bam")
            subprocess.call(["/home/cog/gvandenhoeven/repos/PythonSTRing/lobSTR_script.sh", filename, prefix])
            subprocess.run(f"singularity shell -B /hpc/diaggen:/hpc/diaggen "
                           f"/hpc/diaggen/software/singularity_cache/lobster_v4.0.0.img")
            subprocess.run(f"allelotype --command classify --bam {filename} "
                           f"--noise_model /hpc/diaggen/users/Gabe/tools/lobSTR/models/illumina_v3.pcrfree "
                           f"--strinfo /hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/lobstr_v3.0.2_hg19_strinfo.tab "
                           f"--index-prefix /hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/lobstr_hg19_ref/lobSTR_ "
                           f"--out {prefix}")


if __name__ == "__main_":
    print("Staring analysis pipeline...")
    pc_dir, giab_dir = sys.argv[1], sys.argv[2]
    # pc_dir = "/hpc/diaggen/users/Gabe/data/wes/Positive_controls/"
    # giab_dir = "/hpc/diaggen/users/Gabe/data/wes/GIAB/"
    analysis_pipeline(pc_dir)
    analysis_pipeline(giab_dir)
    print("Analysis complete.")



