import os
import subprocess


def analysis_pipeline(d):
    """
    """
    for filename in os.listdir(d):
        if filename.endswith(".bam"):
            prefix = "/hpc/diaggen/users/Gabe/analysis/output_lobstr/allelotype/" + \
                     filename.split("/")[-1].removesuffix(".bam")
            subprocess.call(["/home/cog/gvandenhoeven/repos/PythonSTRing/lobSTR_script.sh", filename, prefix])


def processing_pipeline(d):
    """Processing results of vcf files while looping over a directory.
    """
    for filename in os.listdir(d):
        if filename.endswith(".vcf"):
            read_file(filename)


def read_file(filename):
    """"""

    with open(filename) as file:
        for line in file:
            print("finish pipeline")


if __name__ == "__main_":
    print("Starting pipeline...")


