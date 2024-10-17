import os
import PyPDF2
import re  # Biblioteca para trabalhar com expressões regulares


def sanitize_filename(filename):
    # Substitui caracteres inválidos por _
    return re.sub(r'[\/:*?"<>|]', '_', filename)


def extract_name(path_pdf):
    try:
        with open(path_pdf, 'rb') as archive_pdf:
            reader_pdf = PyPDF2.PdfReader(archive_pdf)
            text = ""
            for page in reader_pdf.pages:
                text += page.extract_text()

            # Dividindo o texto em linhas
            lines = text.split("\n")
            
            # Encontra a linha com o nome do funcionário, neste caso seria a linha 4, mas está na 1...
            if len(lines) >= 1:
                name_employee = lines[0].strip() 
                return name_employee
            else:
                print(f"O arquivo {path_pdf} não está na mesma configuração, verificar.")
    except Exception as e:
        print(f"Erro ao ler o arquivo {path_pdf}: {e}")
    return None


def rename_pdfs(directory):
    # Verificando se o diretório existe
    if not os.path.exists(directory):
        print(f"O diretório {directory} não foi encontrado.")
        return

    # Verifica se há arquivos no diretório
    files = [f for f in os.listdir(directory) if f.endswith(".pdf")]
    if not files:
        print(f"Não foram encontrados arquivos PDF no diretório {directory}.")
        return

    # Itera sobre cada arquivo PDF no diretório
    for archive in files:
        path_complete = os.path.join(directory, archive)
        name_employee = extract_name(path_complete)
        if name_employee:
            # Sanitize the name to remove invalid characters
            sanitized_name = sanitize_filename(name_employee)
            new_name = f"{sanitized_name}.pdf"
            new_path = os.path.join(directory, new_name)

            # Se o arquivo já existir, adiciona um número incremental ao nome
            counter = 1
            while os.path.exists(new_path):
                new_name = f"{sanitized_name}_{counter}.pdf"
                new_path = os.path.join(directory, new_name)
                counter += 1

            # Renomear o arquivo
            try:
                os.rename(path_complete, new_path)
                print(f"Arquivo {archive} renomeado para {new_name}")
            except Exception as e:
                print(f"Erro ao renomear o arquivo {archive}: {e}")
        else:
            print(f"Nome do funcionário não encontrado no arquivo {archive}")


# Diretório onde estão os PDFs
directory_pdfs = "pdf"
rename_pdfs(directory_pdfs)
