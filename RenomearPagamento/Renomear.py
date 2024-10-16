import os

import PyPDF2


def extract_name(path_pdf):
    try:
        with open(path_pdf, 'rb') as archive_pdf:
            reader_pdf = PyPDF2.PdfReader(archive_pdf)
            text = ""
            for page in reader_pdf.pages:
                text += page.extract_text()

            # Aqui assumo que o nome do funcionário está em uma parte específica do PDF.
            # Por exemplo, o nome pode estar logo no início ou ter algum identificador único.
            # Altere esta parte de acordo com o padrão do seu PDF (neste caso usarei 'Funcionários:'".
            lines = text.split("\n")
            for line in lines:
                if "Funcionário:" in line:
                    # Exemplo de como o nome pode ser extraído
                    line_content = line.split("Funcionário:")[-1].strip()
                    # Dividindo o conteúdo para separar nome e CPF
                    name_parts = line_content.split(
                        "CPF")[0].strip()  # Pega tudo antes de 'CPF'
                    return name_parts
    except Exception as e:
        print(f"Erro ao ler o archive {path_pdf}: {e}")
    return None


def rename_pdfs(directory):
    for archive in os.listdir(directory):
        if archive.endswith(".pdf"):
            path_complete = os.path.join(directory, archive)
            name_employee = extract_name(path_complete)
            if name_employee:
                nem_name = f"{name_employee}.pdf"
                new_path = os.path.join(directory, nem_name)
                os.rename(path_complete, new_path)
                print(f"Arquivo {archive} renomeado para {nem_name}")
            else:
                print(
                    f"Nome do funcionário não encontrado no archive {archive}")


# Diretório onde estão os PDFs
directory_pdfs = "pdf"
rename_pdfs(directory_pdfs)
