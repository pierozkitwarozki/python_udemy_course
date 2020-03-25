# tool that WATERMARKS Pages in pdf file

import PyPDF2

template = PyPDF2.PdfFileReader(open('./PDF_Files/super.pdf', 'rb'))  # shortcut from with open etc...
watermark = PyPDF2.PdfFileReader(open('./PDF_Files/wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))  # merging page from template with watermark
    output.addPage(page)  # adds two new pdf file
with open('./Saved_PDFs/watermarked_super.pdf', 'wb') as save_file:
    output.write(save_file)
