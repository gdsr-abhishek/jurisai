from pathlib import Path
from pypdf import PdfReader

directory = Path('../data/raw')
all_pdf_files = list(directory.rglob('*.pdf'))

for i in all_pdf_files:
    file_name = i.stem
    pdfReader = PdfReader(i)
    file_text = ''
    for page in pdfReader.pages:
        file_text += page.extract_text()

    with open('../data/processed/'+file_name+".txt","w",encoding='utf-8') as file:
        file.write(file_text)
        print(f"{file_name}.txt is created successfully in data/processed")

