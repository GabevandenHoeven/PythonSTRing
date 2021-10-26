import os
import subprocess


def processing_pipeline(d):
    """Processing results of vcf files while looping over a directory.
    """
    for filename in os.listdir(d):
        if filename.endswith(".vcf"):
            read_file(filename)


def read_file(filename):
    """Reads a file
    """
    lines = ["repeat_ID\treference\trepeats_length\tgenotype\n"]
    with open(filename) as file:
        for line in file:
            if not line.startswith("#"):
                rep_id = line.split("\t")[7].split(";")[5].removeprefix("REPID=")
                ref = line.split("\t")[7].split(";")[1].removeprefix("REF=")
                alt = line.split("\t")[4]
                if not alt == ".":
                    alt = alt.split(",")
                    for e in alt:
                        e = e.removeprefix("<STR").removesuffix(">")
                genotype = line.split("\t")[9].split(":")[0]
                if len(alt) == 1:
                    lines.append(rep_id+"\t"+ref+"\t"+str(alt[0])+"\t"+genotype+"\n")
                else:
                    lines.append(rep_id+"\t"+ref+"\t"+alt[0]+","+alt[1]+"\t"+genotype+"\n")
    new_filename = "/hpc/diaggen/users/Gabe/analysis/output_exhunt/" + filename.split("/")[-1].removesuffix(".vcf") \
                   + "output.tsv"
    with open(new_filename, "w") as file:
        for line in lines:
            file.write(line)


def analysis_pipeline(d):
    """Calls a shell script while looping over a directory.
    """
    for filename in os.listdir(d):
        if filename.endswith(".bam"):
            prefix = "/hpc/diaggen/users/Gabe/analysis/output_exhunt/" + filename.split("/")[-1].removesuffix(".bam")
            if "CM" in prefix:
                sex = "male"
            else:
                sex = "female"
            subprocess.call(["expansionhunter_script.sh", filename, prefix, sex])


if __name__ == "__main__":

    pipe = input()

    if pipe.upper() == "ANALYSE":
        # Analysis pipeline
        print("Starting analysis pipeline...")
        pc_dir = "/hpc/diaggen/users/Gabe/data/wes/Positive_controls/"
        giab_dir = "/hpc/diaggen/users/Gabe/data/wes/GIAB/"
        analysis_pipeline(pc_dir)
        analysis_pipeline(giab_dir)
    elif pipe.upper() == "PROCESS":
        # Processing pipeline
        print("Starting processing pipeline...")
        res_dir = "/hpc/diaggen/users/Gabe/analysis/output_exhunt/"
        processing_pipeline(res_dir)
    else:
        print("Error. Pipeline command not recognised.")
        print("Use \"ANALYSE\" to activate the analysis pipeline and process bam files using ExpansionHunter, "
              "or use \"PROCESS\" to activate the processing pipeline to process ExpansionHunter output vcf files.")
