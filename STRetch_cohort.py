import os
import subprocess
import sys


def analysis_pipeline(in_d, out_d):
    """Runs an analysis while looping over a directory.

    :param in_d: str - path to the directory with the fastq.gz files that need to be analysed.
    :param out_d: str - path to the output directory.
    """
    os.chdir(out_d)
    action = ["/hpc/diaggen/users/Gabe/tools/STRetch/tools/bin/bpipe", "run", "-p",
              "EXOME_TARGET=/hpc/diaggen/users/Gabe/tools/STRetch/reference-data/"
              "hg19.simpleRepeat_period1-6_dedup.sorted.bed",
              "/hpc/diaggen/users/Gabe/tools/STRetch/pipelines/STRetch_exome_pipeline.groovy"]
    for filename in os.listdir(in_d):
        if filename.endswith("R1.fastq.gz"):
            reads1 = in_d + filename
            reads2 = in_d + filename.replace("R1.fastq.gz", "R2.fastq.gz")
            action.append(reads1)
            action.append(reads2)
    subprocess.run(action)


if __name__ == "__main__":
    print("Starting analysis pipeline...")
    analysis_pipeline(sys.argv[1], sys.argv[2])
    print("Analysis complete.")
