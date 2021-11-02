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
            prefix = out_d + filename.split("/")[-1].replace(".bam", "")
            # subprocess.run([f"singularity", f"shell", f"-B", f"/hpc/diaggen:/hpc/diaggen",
            #                f"/hpc/diaggen/software/singularity_cache/lobster_v4.0.0.img"])
            # subprocess.run([f"allelotype", f"--command", f"classify", f"--bam", f"{in_d}{filename}", f"--noise_model",
            #                 f"/hpc/diaggen/users/Gabe/tools/lobSTR/models/illumina_v3.pcrfree",
            #                 f"--strinfo", f"/hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/"
            #                               f"lobstr_v3.0.2_hg19_strinfo.tab", f"--index-prefix",
            #                 f"/hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/lobstr_hg19_ref/lobSTR_",
            #                 f"--out", f"{prefix}"])
            singularity_img = "/hpc/diaggen:/hpc/diaggen /hpc/diaggen/software/singularity_cache/lobster_v4.0.0.img"
            lobstr_command = f"allelotype --command classify --bam {in_d}{filename} --noise_model " \
                             f"/hpc/diaggen/users/Gabe/tools/lobSTR/models/illumina_v3.pcrfree --strinfo " \
                             f"/hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/lobstr_v3.0.2_hg19_strinfo.tab " \
                             f"--index-prefix " \
                             f"/hpc/diaggen/users/Gabe/tools/lobSTR/lobstr_new/lobstr_hg19_ref/lobSTR_ " \
                             f"--out {prefix}"
            subprocess.run(["singularity", "shell", "-B", singularity_img, lobstr_command])


if __name__ == "__main__":
    print("Staring analysis pipeline...")
    print("arg1: " + sys.argv[1])
    print("arg2: " + sys.argv[2])
    analysis_pipeline(sys.argv[1], sys.argv[2])
    print("Analysis complete.")
