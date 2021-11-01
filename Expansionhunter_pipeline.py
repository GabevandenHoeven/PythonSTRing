import os
import subprocess


def processing_pipeline(d):
    """Calls process_file() to process vcf files in a given directory.

    :param d: str - path to the directory with the vcf files that need to be processed.
    :return new_file: str - path to the new file containing the simplified output.
    """
    new_file = ""
    for filename in os.listdir(d):
        if filename.endswith(".vcf"):
            new_file = process_file(filename)
    return new_file


def process_file(filename):
    """Processes a vcf file by ExpansionHunter and writes output to a tsv file.

    :param filename: str - path to the file that is being processed.
    :return new_filename: str - path to the new file containing the simplified output.
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
                    lines.append(rep_id+"\t"+ref+"\t"+alt[0]+", "+alt[1]+"\t"+genotype+"\n")
    new_filename = "/hpc/diaggen/users/Gabe/analysis/output_exhunt/" + filename.split("/")[-1].removesuffix(".vcf") \
                   + "output.tsv"
    with open(new_filename, "w") as file:
        for line in lines:
            file.write(line)
    return new_filename


def analysis_pipeline(d):
    """Calls a shell script while looping over a directory.

    :param d: str - path to the directory with the BAM files that need to be analysed.
    """
    for filename in os.listdir(d):
        if filename.endswith(".bam"):
            prefix = "/hpc/diaggen/users/Gabe/analysis/output_exhunt/" + filename.split("/")[-1].removesuffix(".bam")
            if "CM" in prefix:
                sex = "male"
            else:
                sex = "female"
            subprocess.call(["/home/cog/gvandenhoeven/repos/PythonSTRing/expansionhunter_script.sh",
                             filename, prefix, sex])


if __name__ == "__main__":
    # Analysis pipeline
    print("Starting analysis pipeline...")
    pc_dir = "/hpc/diaggen/users/Gabe/data/wes/Positive_controls/"
    giab_dir = "/hpc/diaggen/users/Gabe/data/wes/GIAB/"
    analysis_pipeline(pc_dir)
    analysis_pipeline(giab_dir)
    print("Analysis complete.")

    # Processing pipeline
    print("Starting processing pipeline...")
    res_dir = "/hpc/diaggen/users/Gabe/analysis/output_exhunt/"
    output = processing_pipeline(res_dir)
    print("processing complete.\nNew output in " + output)
