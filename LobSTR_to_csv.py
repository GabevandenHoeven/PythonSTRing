import os


def process_files(in_d):
    """This function processes the output vcf files from lobSTR. It writes data needed for a plot to a CSV file.

    :param in_d: str - directory of the output files to be processed. The script loops over the directory.

    """

    lines = ["Sample,Gene,Allele,Tool,Normalised\n"]
    for filename in os.listdir(in_d):
        if filename.endswith(".vcf"):
            print("Working on file: " + filename)
            with open(in_d + filename) as f:
                sample = filename.replace(".vcf", "")
                tool = "LobSTR"
                for line in f:
                    if not line.startswith("#"):
                        pos = line.split("\t")[1]
                        chro = line.split("\t")[0]
                        b = False
                        # These are the positions for ATXN3, C9ORF72, DMPK and AR
                        # If other genes have to be included this should be changed to a more efficient method
                        if chro == "X" and int(pos) == 66765159:
                            gene = "AR"
                            b = True
                        elif chro == "9" and int(pos) == 27573483:
                            gene = "C9ORF72"
                            b = True
                        elif chro == "14" and int(pos) == 92537355:
                            gene = "ATXN3"
                            b = True
                        elif chro == "19" and int(pos) == 46273463:
                            gene = "DMPK"
                            b = True
                        if b:
                            ref = float(line.split("\t")[7].split(";")[3].replace("REF=", ""))
                            if line.split("\t")[9].split(":")[0] == "0/0":
                                normalised = 0
                                new_line = f"{sample},{gene},{ref},{tool},{normalised}\n"
                                lines.append(new_line)
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "1/1":
                                allele = float(line.split("\t")[7].split(";")[7].replace("RPA=", ""))
                                normalised = allele - ref
                                new_line = f"{sample},{gene},{allele},{tool},{normalised}\n"
                                lines.append(new_line)
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "0/1" or \
                                    line.split("\t")[9].split(":")[0] == "1/0":
                                normalised = 0
                                new_line = f"{sample},{gene},{ref},{tool},{normalised}\n"
                                lines.append(new_line)
                                allele = float(line.split("\t")[7].split(";")[7].replace("RPA=", ""))
                                normalised = allele - ref
                                new_line = f"{sample},{gene},{allele},{tool},{normalised}\n"
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "1/2" or \
                                    line.split("\t")[9].split(":")[0] == "2/1":
                                ls = line.split("\t")[7].split(";")[7].replace("RPA=", "").split(",")
                                for allele in ls:
                                    normalised = float(allele) - ref
                                    new_line = f"{sample},{gene},{allele},{tool},{normalised}\n"
                                    lines.append(new_line)
                            else:
                                print("Error." + filename + " seems to be incompatible with the script.")
    # Writes all lines directly to a new file.
    # The filename is hard-coded right now in order to make it easier for the R script to take the right file as input
    # This could be improved on
    with open("results_lobstr.csv") as f:
        f.writelines(lines)
