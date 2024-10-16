import os
from PyPDF2 import PdfMerger


# Função para juntar PDFs de uma pasta
def merge_pdfs_from_folder(folder_path, output_filename):
    pdf_merger = PdfMerger()

    # Listar arquivos no diretório
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as pdf_file:
                pdf_merger.append(pdf_file)

    # Salvar o arquivo PDF combinado
    with open(output_filename, 'wb') as output_pdf:
        pdf_merger.write(output_pdf)

    print(f'PDFs combinados em {output_filename}')


folder_path = 'pdf'  # Substitua pelo caminho da pasta
output_filename = 'output.pdf'  # Nome do arquivo PDF final

merge_pdfs_from_folder(folder_path, output_filename)
