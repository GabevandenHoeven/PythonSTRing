import os


def process_files(in_d):
    """This function processes the output vcf files from lobSTR. It writes data needed for a plot to an Excel file.

    :param in_d: str - directory of the output files to be processed. The script loops over the directory.

    """

    lines = ["Sample,Gene,Allele,Tool,Normalised\n"]
    for filename in os.listdir(in_d):
        if filename.endswith(".vcf"):
            print("Working on file: " + filename)
            with open(in_d + filename) as f:
                for line in f:
                    if not line.startswith("#"):
                        pos = line.split("\t")[1]
                        chro = line.split("\t")[0]
                        b = False
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
                            sample = filename.replace(".vcf", "")
                            tool = "LobSTR"
                            if line.split("\t")[9].split(":")[0] == "0/0":
                                allele = ref
                                normalised = 0
                                new_line = sample + "," + gene + "," + str(allele) + "," + tool + "," \
                                           + str(normalised) + "\n"
                                lines.append(new_line)
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "1/1":
                                allele = float(line.split("\t")[7].split(";")[7].replace("RPA=", ""))
                                normalised = allele - ref
                                new_line = sample + "," + gene + "," + str(allele) + "," + tool + "," \
                                           + str(normalised) + "\n"
                                lines.append(new_line)
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "0/1" or \
                                    line.split("\t")[9].split(":")[0] == "1/0":
                                allele = ref
                                normalised = 0
                                new_line = sample + "," + gene + "," + str(allele) + "," + tool + "," \
                                           + str(normalised) + "\n"
                                lines.append(new_line)
                                allele = float(line.split("\t")[7].split(";")[7].replace("RPA=", ""))
                                normalised = allele - ref
                                new_line = sample + "," + gene + "," + str(allele) + "," + tool + "," \
                                           + str(normalised) + "\n"
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "1/2" or \
                                    line.split("\t")[9].split(":")[0] == "2/1":
                                ls = line.split("\t")[7].split(";")[7].replace("RPA=", "").split(",")
                                for allele in ls:
                                    normalised = float(allele) - ref
                                    new_line = sample + "," + gene + "," + str(allele) + "," + tool + "," \
                                               + str(normalised) + "\n"
                                    lines.append(new_line)
                            else:
                                print("Error. This file seems to be incompatible with the script.")
    new_file = check_file("results_lobstr.csv")
    with open(new_file, "w") as f:
        f.writelines(lines)


def check_file(file_path):
    if os.path.exists(file_path):
        numb = 1
        while True:
            new_path = "{0}_{2}{1}".format(*os.path.splitext(file_path) + (numb,))
            if os.path.exists(new_path):
                numb += 1
            else:
                return new_path
    return file_path


if __name__ == "__main__":
    print("Processing output now...")
    d = "/Users/ghoeven2/Documents/test_vcf/"
    process_files(d)
    print("Processing complete.")
