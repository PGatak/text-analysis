import PyPDF2

pdf = open('book.pdf', 'rb')
reader = PyPDF2.PdfFileReader(pdf)
pages = reader.numPages

for i in range(pages):
    page = reader.getPage(i)
    print(page.extractText())


