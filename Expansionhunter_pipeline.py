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
            prefix = out_d + filename.split("/")[-1].removesuffix(".bam")
            if "CM" in prefix:
                sex = "male"
            else:
                sex = "female"
            subprocess.run(f"/hpc/diaggen/users/Gabe/tools/ExpansionHunter-v5.0.0-linux_x86_64/bin/ExpansionHunter "
                           f"--reads {filename} "
                           f"--reference /hpc/diaggen/data/databases/ref_genomes/"
                           f"Homo_sapiens.GRCh37.GATK.illumina/Homo_sapiens.GRCh37.GATK.illumina.fasta "
                           f"--variant_catalog /hpc/diaggen/users/Gabe/tools/ExpansionHunter-v5.0.0-linux_x86_64/"
                           f"variant_catalog/hg19/variant_catalog.json --output-prefix {prefix} --sex {sex}")


if __name__ == "__main__":
    print("Starting analysis pipeline...")
    in_dir, out_dir = sys.argv[1], sys.argv[2]
    # pc_dir = "/hpc/diaggen/users/Gabe/data/wes/Positive_controls/"
    # giab_dir = "/hpc/diaggen/users/Gabe/data/wes/GIAB/"
    print("element 0: " + str(sys.argv[0]))
    print("element 1 " + in_dir)
    print("element 2: " + out_dir)
    # analysis_pipeline(in_dir, out_dir)
    print("Analysis complete.")


