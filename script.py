from PyPDF2 import PdfFileWriter, PdfFileReader
import numpy, array,os

pages_to_keep = []
dir = 'C:\\Code\\test' #Path were the pdf files are
page_to_remove=2
page_position=page_to_remove-1

for filename in os.listdir(dir):
    f = os.path.join(dir, filename)
    
    
    if os.path.isfile(f):
        infile = PdfFileReader(f, 'rb')
        totalpages = infile.numPages
        output = PdfFileWriter()
        i = 0

        while i < totalpages:
        
            if i != page_position:
                
                pages_to_keep = numpy.append (pages_to_keep, [i]).astype('int')
            i = i+1

        for i in pages_to_keep:
            p = infile.getPage(i)
            output.addPage(p)

        with open(f, 'wb') as f:
            output.write(f)
    pages_to_keep = []
print("done")