import PyPDF2

# content_pdf = 'super.pdf'
# watermark = 'wtr.pdf'
# merged_file = 'merged.pdf'


# # reading content of super.pdf
# reader = PyPDF2.PdfFileReader(content_pdf)
# page_indices = list(range(0, len(reader.pages)))

# # reading the first page of file 'wtr.pdf'
# reader_stamp = PyPDF2.PdfFileReader(watermark)
# image_page = reader_stamp.pages[0]

# # create instance of writer to prepare write file
# writer = PyPDF2.PdfFileWriter()

# for index in page_indices:
#     content_page = reader.pages[index]
#     mediabox = content_page.mediaBox

#     content_page.mergePage(image_page)
#     content_page.mediabox = mediabox
#     writer.addPage(content_page)

# with open(merged_file, "wb") as fp:
#     writer.write(fp)

# SOLUTION

template = PyPDF2.PdfFileReader(open('super.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.getNumPages()):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

with open('watermarked_output.pdf', 'wb') as file:
    output.write(file)
