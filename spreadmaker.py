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
blank_pgs=((sections+1)*16)-pages

for k in range(0,pages+blank_pgs):
    if k<pages:
        out.addPage(pdf.getPage(k))
    else:
        print(k)
        out.addBlankPage()

outs = file("out.pdf", "wb")
out.write(outs)
outs.close()


pdf = PdfFileReader(file( "out.pdf", "rb"))
out2 = PdfFileWriter()

for spread_id in range(0,sections+1):
    print(spread_id)
    k=0
    for i in range((spread_id*16),((spread_id*16)+8)):
        if (k%2 == 0):
            print(str(((((spread_id+1)*16)-1)-k))+','+str(i)+','+str(k))
            out2.addPage(pdf.getPage((((spread_id+1)*16)-1)-k))
            out2.addPage(pdf.getPage(i))
        else:
            print(str(i)+','+str(((((spread_id+1)*16)-1)-k))+','+str(k))
            out2.addPage(pdf.getPage(i))
            out2.addPage(pdf.getPage((((spread_id+1)*16)-1)-k))

        k=k+1



outs = file("out_final.pdf", "wb")
out2.write(outs)
outs.close()
