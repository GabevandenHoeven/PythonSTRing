import os
import subprocess
import sys


def analysis_pipeline(in_d, out_d):
    """Calls a shell script while looping over a directory.

    :param in_d: str - path to the directory with the BAM files that need to be analysed.
    :param out_d: str - path to the output directory.
    """
    for filename in os.listdir(in_d):
        if filename.endswith(".bam"):
            print(filename)
            prefix = out_d + filename.split("/")[-1].replace(".bam", "")
            sb = False
            sex = ""
            if "CM" or "PM" in filename:
                sex = "male"
                sb = True
            elif "CF" or "PF" in filename:
                sex = "female"
                sb = True
            if sb:
                subprocess.run(
                    [f"/hpc/diaggen/users/Gabe/tools/ExpansionHunter-v5.0.0-linux_x86_64/bin/ExpansionHunter",
                     f"--reads", f"{in_d}{filename}",
                     f"--reference", f"/hpc/diaggen/data/databases/ref_genomes/"
                                     f"Homo_sapiens.GRCh37.GATK.illumina/Homo_sapiens.GRCh37.GATK.illumina.fasta",
                     f"--variant-catalog", f"/hpc/diaggen/users/Gabe/tools/ExpansionHunter-v5.0.0-linux_x86_64/"
                                           f"variant_catalog/hg19/variant_catalog.json",
                     f"--output-prefix", f"{prefix}", f"--sex", f"{sex}"])
            else:
                print("Error.\nCould not determine gender")


if __name__ == "__main__":
    print("Starting analysis pipeline...")
    analysis_pipeline(sys.argv[1], sys.argv[2])
    print("Analysis complete.")
