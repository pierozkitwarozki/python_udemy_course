# this script rotates pdf and saves as a new file, not something special
import PyPDF2

with open('./PDF_Files/dummy.pdf', 'rb') as file:  # read binary
    reader = PyPDF2.PdfFileReader(file)
    page = reader.getPage(0)
    page.rotateCounterClockwise(90)
    writer = PyPDF2.PdfFileWriter()
    writer.addPage(page)
    with open('./Saved_PDFs/tilt.pdf', 'wb') as save_file:
        writer.write(save_file)

