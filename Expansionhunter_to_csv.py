import os


def process_files(in_d):
    """This function processes the output vcf files from Expansionhunter.
    It writes data needed for a plot to a CSV file.

    :param in_d: str - directory of the output files to be processed. The script loops over the directory.
    """
    lines = ["Sample,Gene,Allele,Tool,Normalised\n"]
    for filename in os.listdir(in_d):
        if filename.endswith(".vcf"):
            print("Working on file: " + filename)
            with open(filename) as file:
                tool = "ExpansionHunter"
                sample = filename.replace(".vcf", "")
                for line in file:
                    if not line.startswith("#"):
                        gene = line.split("\t")[7].split(";")[5].replace("REPID=", "")
                        # Removing this if statement can allow other genes to be plotted
                        if gene == "ATXN3" or gene == "C9ORF72" or gene == "DMPK" or gene == "AR":
                            ref = line.split("\t")[7].split(";")[1].replace("REF=", "")
                            allele = line.split("\t")[4]
                            # Adding a new line to the list lines for each allele with the corresponding information
                            # line.split("\t")[9].split(":")[0] refers to the genotype
                            if line.split("\t")[9].split(":")[0] == "1/2":
                                allele = allele.split(",")
                                for e in allele:
                                    e = e.replace("<STR", "").replace(">", "")
                                    normalised = int(e) - int(ref)
                                    new_line = f"{sample},{gene},{e},{tool},{normalised}\n"
                                    lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "1/1":
                                allele = allele.replace("<STR", "").replace(">", "")
                                normalised = int(allele) - int(ref)
                                new_line = f"{sample},{gene},{allele},{tool},{normalised}\n"
                                lines.append(new_line)
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "0/1":
                                new_line = f"{sample},{gene},{ref},{tool},0\n"
                                lines.append(new_line)
                                allele = allele.replace("<STR", "").replace(">", "")
                                normalised = int(allele) - int(ref)
                                new_line = f"{sample},{gene},{allele},{tool},{normalised}\n"
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "0/0":
                                normalised = 0
                                new_line = f"{sample},{gene},{ref},{tool},{normalised}\n"
                                lines.append(new_line)
                                lines.append(new_line)
                            else:
                                print("Error. " + filename + " seems to be incompatible with the script.")
    # Writes all lines directly to a new file.
    # The filename is hard-coded right now in order to make it easier for the R script to take the right file as input
    # This could be improved on
    with open("results_expansionhunter.csv", "w") as f:
        f.writelines(lines)
