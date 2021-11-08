import os
import subprocess
import sys
import pathlib


def process_files(in_d, new_dir):
    """Loops through a directory and creates a new output file for vcf files.
    These contain STR information of AR, SCA3, C9ORF72, DM1

    :param in_d: str - path to the directory with the vcf files that need to be processed.
    :param new_dir: str - path to the output directory.
    """
    db = pathlib.Path(new_dir)
    if not db.exists():
        print("Given output directory does not exist.\nMaking directory now.")
        subprocess.run(["mkdir", new_dir])
    for filename in os.listdir(in_d):
        if filename.endswith(".vcf"):
            print("Working on file: " + filename)
            lines = ["#FORMAT=<ID=ALLREADS,Number=1,Type=String,Description=<All reads aligned to locus>\n",
                     "#FORMAT=<ID=AML,Number=1,Type=String,Description=<Allele marginal likelihood ratio scores>\n",
                     "#FORMAT=<ID=DISTENDS,Number=1,Type=Float,Description=<Average difference between distance of "
                     "STR to read ends>\n",
                     "#FORMAT=<ID=DP,Number=1,Type=Integer,Description=<Read Depth>\n",
                     "#FORMAT=<ID=GB,Number=1,Type=String,Description=<Genotype given in bp difference from "
                     "reference>\n",
                     "#FORMAT=<ID=PL,Number=G,Type=Integer,Description=<Normalized, Phred-scaled likelihoods for "
                     "genotypes as defined in the VCF specification>\n",
                     "#FORMAT=<ID=Q,Number=1,Type=Float,Description=<Likelihood ratio score of allelotype call>\n",
                     "#FORMAT=<ID=GT,Number=1,Type=String,Description=<Genotype>\n",
                     "#FORMAT=<ID=SB,Number=1,Type=Float,Description=<Strand bias>\n",
                     "#FORMAT=<ID=STITCH,Number=1,Type=Integer,Description=<Number of stitched reads>\n",
                     "#Chr\tPos\tEnd\tREPID\tRef\tRPA\tRPU\tFMT\t" + filename.replace(".vcf", "") + "\n"]
            with open(in_d + filename) as file:
                for line in file:
                    if not line.startswith("#"):
                        pos = line.split("\t")[1]
                        end = line.split("\t")[7].split(";")[0].replace("END=", "")
                        chro = line.split("\t")[0]
                        b = False
                        # The range is the position in which this STR is located
                        # The specific position are derived from grep calls into some of the output files
                        # A source to hg19 positions of genes can be found here:
                        # Source: https://github.com/mcfrith/tandem-genotypes/blob/master/hg19-disease-tr.txt
                        if chro == "X" and int(pos) == 66765159:
                            rep_id = "AR"
                            b = True
                        elif chro == "9" and int(pos) == 27573483:
                            rep_id = "C9ORF72"
                            b = True
                        elif chro == "14" and int(pos) == 92537355:
                            rep_id = "SCA3"
                            b = True
                        elif chro == "19" and int(pos) == 46273463:
                            rep_id = "DM1"
                            b = True
                        if b:
                            ref = line.split("\t")[7].split(";")[3].replace("REF=", "")
                            rpu = line.split("\t")[7].split(";")[5].replace("RU=", "")
                            fmt = line.split("\t")[8]
                            info = line.split("\t")[9]
                            if info.split(":")[0] == "0/0":
                                rpa = ref + "," + ref
                            elif info.split(":")[0] == "1/1":
                                rpa = line.split("\t")[7].split(";")[7].replace("RPA=", "")
                                rpa = rpa + "," + rpa
                            elif info.split(":")[0] == "0/1" or info.split(":")[0] == "1/0":
                                rpa = ref + "," + line.split("\t")[7].split(";")[7].replace("RPA=", "")
                            elif info.split(":")[0] == "1/2" or info.split(":")[0] == "2/1":
                                rpa = line.split("\t")[7].split(";")[7].replace("RPA=", "")
                            else:
                                rpa = ""
                            new_line = f"{chro}\t{pos}\t{end}\t{rep_id}\t{ref}\t{rpa}\t{rpu}\t{fmt}\t{info}"
                            lines.append(new_line)
            new_filename = new_dir + filename.replace(".vcf", ".tsv")
            with open(new_filename, "w") as file:
                file.writelines(lines)


if __name__ == "__main__":
    print("Starting processing of output files.")
    process_files(sys.argv[1], sys.argv[2])
    print("Processing successful.\nNew files can be found in the new directory.")
