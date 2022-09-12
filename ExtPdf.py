import PyPDF2

#Colocar o arquivo PDF na Mesma Pasta
# Load arquivo PDF
PdfFileObj = open('PDF', 'rb')

# Leitura do arquivo PDF
PdfReader = PyPDF2.PdfFileReader(PdfFileObj)

# Cap pagina do PDF
PageObj = PdfReader.getPage(0)

# Extrai o arquivo PDF e manda para a Variavel
text = PageObj.extractText()

print(text)

