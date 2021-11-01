import os
import subprocess
from Expansionhunter_pipeline import processing_pipeline


def analysis_pipeline(d):
    """Calls a shell script while looping over a given directory.

    :param d: str - path to the directory with the BAM files that need to be analysed.
    """
    for filename in os.listdir(d):
        if filename.endswith(".bam"):
            prefix = "/hpc/diaggen/users/Gabe/analysis/output_lobstr/allelotype/" + \
                     filename.split("/")[-1].removesuffix(".bam")
            subprocess.call(["/home/cog/gvandenhoeven/repos/PythonSTRing/lobSTR_script.sh", filename, prefix])


def process_file(filename):
    """Processes a vcf file by lobSTR and writes output to a tsv file.

    :param filename: str - path to the file that is being processed.
    :return new_filename: str - path to the new file containing the simplified output.
    """
    lines = ["repeat_ID\treference\trepeats_length\tgenotype\n"]
    with open(filename) as file:
        for line in file:
            print("")

    new_filename = "/hpc/diaggen/users/Gabe/analysis/output_lobstr/allelotype/" + \
                   filename.split("/")[-1].removesuffix(".vcf") + "output.tsv"
    with open(new_filename, "w") as file:
        for line in lines:
            file.write(line)
    return new_filename


if __name__ == "__main_":
    print("Starting pipeline...")
    print("Staring analysis...")
    pc_dir = "/hpc/diaggen/users/Gabe/data/wes/Positive_controls/"
    giab_dir = "/hpc/diaggen/users/Gabe/data/wes/GIAB/"
    analysis_pipeline(pc_dir)
    analysis_pipeline(giab_dir)
    print("Analysis complete.")

    print("Starting processing output...")
    res_dir = "/hpc/diaggen/users/Gabe/analysis/output_lobstr/allelotype/"
    output = processing_pipeline(res_dir)
    print("Processing complete.\nNew file in " + output)



