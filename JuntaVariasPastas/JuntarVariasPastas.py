import os
from PyPDF2 import PdfMerger


# Função para juntar PDFs de uma pasta
def merge_pdfs_in_subfolders(base_folder):
    # Percorre cada subpasta no diretório base
    for folder_name in os.listdir(base_folder):
        folder_path = os.path.join(base_folder, folder_name)

        # Verifica se é uma pasta
        if os.path.isdir(folder_path):
            pdf_merger = PdfMerger()

            # Listar e juntar arquivos PDF dentro da subpasta
            for filename in os.listdir(folder_path):
                if filename.endswith('.pdf'):
                    file_path = os.path.join(folder_path, filename)
                    with open(file_path, 'rb') as pdf_file:
                        pdf_merger.append(pdf_file)

            # Se houver PDFs para juntar, salvar o arquivo combinado
            if len(pdf_merger.pages) > 0:
                output_filename = os.path.join(base_folder,
                                               f"{folder_name}.pdf")
                with open(output_filename, 'wb') as output_pdf:
                    pdf_merger.write(output_pdf)

                print(
                    f'PDFs na pasta "{folder_name}" combinados em {output_filename}'
                )
            else:
                print(f'Nenhum PDF encontrado na pasta "{folder_name}".')


# Exemplo de uso
base_folder = 'Pastas para juntar'  # Substitua pelo caminho da pasta principal
merge_pdfs_in_subfolders(base_folder)
