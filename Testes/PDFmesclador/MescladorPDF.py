import PyPDF2
import os

merger = PyPDF2.PdfMerger(strict=False)

listaArquivos = os.listdir("PDFs")
for arquivo in listaArquivos:
    if ".pdf" in arquivo:
        merger.append(f"PDFs/{arquivo}")

merger.write("Documentação.pdf")