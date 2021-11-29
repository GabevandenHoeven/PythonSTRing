import os
import sys

import xlsxwriter


def process_files(in_d):
    """This function processes the output vcf files from lobSTR. It writes data needed for a plot to an Excel file.

    :param in_d: str - directory of the output files to be processed. The script loops over the directory.

    """

    lines = [
        ["Sample", "Gene", "Allele", "Tool", "Normalised"]
    ]
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
                                new_line = [sample, gene, allele, tool, normalised]
                                lines.append(new_line)
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "1/1":
                                allele = float(line.split("\t")[7].split(";")[7].replace("RPA=", ""))
                                normalised = allele - ref
                                new_line = [sample, gene, allele, tool, normalised]
                                lines.append(new_line)
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "0/1" or \
                                    line.split("\t")[9].split(":")[0] == "1/0":
                                allele = ref
                                normalised = 0
                                new_line = [sample, gene, allele, tool, normalised]
                                lines.append(new_line)
                                allele = float(line.split("\t")[7].split(";")[7].replace("RPA=", ""))
                                normalised = allele - ref
                                new_line = [sample, gene, allele, tool, normalised]
                                lines.append(new_line)
                            elif line.split("\t")[9].split(":")[0] == "1/2" or \
                                    line.split("\t")[9].split(":")[0] == "2/1":
                                ls = line.split("\t")[7].split(";")[7].replace("RPA=", "").split(",")
                                for allele in ls:
                                    normalised = float(allele) - ref
                                    new_line = [sample, gene, float(allele), tool, normalised]
                                    lines.append(new_line)
                            else:
                                print("Error. This file seems to be incompatible with the script.")

    workbook = xlsxwriter.Workbook("LobSTR_results.xlsx")
    worksheet = workbook.add_worksheet("Sheet1")
    row = 0
    col = 0
    for sample, gene, allele, tool, normalised in lines:
        worksheet.write(row, col, sample)
        worksheet.write(row, col + 1, gene)
        worksheet.write(row, col + 2, allele)
        worksheet.write(row, col + 3, tool)
        worksheet.write(row, col + 4, normalised)
        row += 1

    workbook.close()


if __name__ == "__main__":
    print("Processing output now...")
    process_files(sys.argv[1])
    print("Processing complete.")
