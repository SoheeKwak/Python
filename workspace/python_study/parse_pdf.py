import pdfquery
import pdfrw
import pdfminer

pdf = 'EN-FINAL Table 9.pdf'

with open(pdf) as f:
    doc = pdfminer.pdf(f)

for page in doc[:2]:
    print(page)






