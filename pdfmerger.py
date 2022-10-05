import PyPDF2
import sys
import os

def main():

    merger = PyPDF2.PdfMerger()

    desktop = os.path.expanduser("~\Desktop")
    dir = f'{desktop}\pdfMerger'

    if not os.path.exists(dir):
        raise Exception("This directory does not exist.")

    for file in os.listdir(dir):
        if file.endswith(".pdf"):
            merger.append(open(f'{dir}\{file}', "rb"))
    merger.write(f'{dir}\combinedPDFdocs.pdf')
    merger.close()

if __name__ == "__main__":
    pass