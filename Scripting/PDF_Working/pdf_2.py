# PDF Merger
import PyPDF2
import sys

inputs = sys.argv[1:]  # gets all the arguments in terminal after the first one !!! Important !!!


def pdf_combiner(pdf_list):  # do not need to open these files, just give the paths as args in terminal
    # and merge in the loop
    merger = PyPDF2.PdfFileMerger()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('./Saved_PDFs/super.pdf')


pdf_combiner(inputs)
