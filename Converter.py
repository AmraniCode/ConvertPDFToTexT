from pdf2docx import Converter
import PyPDF2

#Test variables
pdf_file = 'pdf.pdf'
docx_file = 'doc.docx'


class PdfConverter:
    def convertPdfToDocx(self,pdf_file,docx_file):
        # convert pdf to docx
        cv = Converter(pdf_file)
        cv.convert(docx_file)  # all pages by default
        cv.close()

    def convertPdfToText(self,pdf_file,text_file):
        fhandle = open(r''+pdf_file, 'rb')
        pdfReader = PyPDF2.PdfFileReader(fhandle)
        pagehandle = pdfReader.getPage(0)
        with open(text_file, 'w') as f:
            f.write(pagehandle.extractText())

    def convertTextToPdf(self, text_file, pdf_file):
        # convert pdf to docx
        cv = Converter(pdf_file)
        cv.convert(docx_file)  # all pages by default
        cv.close()


if __name__ == '__main__':
    converter = PdfConverter()
    converter.convertPdfToText(pdf_file,"text.txt")
