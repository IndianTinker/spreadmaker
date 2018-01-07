from PyPDF2 import PdfFileReader, PdfFileWriter

out = PdfFileWriter()
pdf = PdfFileReader(file( "in.pdf", "rb"))

if pdf.isEncrypted:
    pdf.decrypt('')

pages=pdf.getNumPages()
print(pages)

sections=pages/16
print(sections)
print("Blank Pages "+str(((sections+1)*16)-pages))

for spread_id in range(0,sections):
    print(spread_id)
    k=0
    for i in range((spread_id*16),((spread_id*16)+8)):
        print(str(i)+','+str(((((spread_id+1)*16)-1)-k)))
        out.addPage(pdf.getPage(i))
        out.addPage(pdf.getPage((((spread_id+1)*16)-1)-k))
        k=k+1



outs = file("out.pdf", "wb")
out.write(outs)
outs.close()
