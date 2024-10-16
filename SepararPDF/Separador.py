import os
from PyPDF2 import PdfReader, PdfWriter


# Função para encontrar o primeiro PDF em uma pasta e separar suas páginas
def split_first_pdf_in_folder(folder_path, output_folder):
    # Criar a pasta de saída se não existir
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Encontrar o primeiro arquivo PDF na pasta
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):  # Verifica se é um arquivo PDF
            input_pdf = os.path.join(folder_path, filename)
            print(f"Encontrado o arquivo PDF: {input_pdf}")

            # Abrir o arquivo PDF de entrada
            with open(input_pdf, 'rb') as pdf_file:
                reader = PdfReader(pdf_file)
                total_pages = len(reader.pages)

                # Separar cada página em um arquivo individual
                for page_num in range(total_pages):
                    writer = PdfWriter()
                    writer.add_page(reader.pages[page_num])

                    # Nome do arquivo de saída com base no número da página e nome do arquivo original
                    output_filename = os.path.join(
                        output_folder,
                        f"{filename[:-4]}_page_{page_num + 1}.pdf")

                    # Salvar a página como PDF individual
                    with open(output_filename, 'wb') as output_pdf:
                        writer.write(output_pdf)

                    print(
                        f'Página {page_num + 1} do arquivo {filename} salva como {output_filename}'
                    )

            # Parar o loop após encontrar e processar o primeiro PDF
            break
    else:
        print("Nenhum arquivo PDF encontrado na pasta.")


# Exemplo de uso
folder_path = 'PDF'  # Substitua pelo caminho da pasta com seu PDF
output_folder = 'PDF_Separado'  # Substitua pelo caminho da pasta onde os PDFs serão salvos

split_first_pdf_in_folder(folder_path, output_folder)
