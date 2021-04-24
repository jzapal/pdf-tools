from PyPDF2 import PdfFileMerger
from PyPDF2 import PdfFileReader


def merge_pdfs(pdfs, output_filename):
    if len(pdfs) == 0:
        print("No files to merge")
        return
    merger = PdfFileMerger(strict=False)
    for pdf in pdfs:
        if pdf == output_filename:
            continue
        print("Parse '%s'" % pdf)
        merger.append(PdfFileReader(open(pdf, 'rb')))
    print("Start writing '%s'" % output_filename)
    merger.write(output_filename)
