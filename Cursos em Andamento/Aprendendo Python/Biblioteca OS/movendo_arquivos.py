import os
import shutil
CAMINHO = "C:\\Users\\"

def mover_pdfs(caminho):
    for raiz, pastas, arquivos in os.walk(CAMINHO):
        for arquivo in arquivos:
            
            # obter o caminho absoluto do arquivo
            caminho_arquivo = os.path.join(raiz, arquivo)

            # separar a extensão do arquivo
            _, ext = os.path.splitext(caminho_arquivo)
            if ext.lower() == '.pdf':
                
                # criar pasta para os pdfs
                pasta_pdfs = "C:\\Users\\valte\\Desktop\\pdfs2" 
                os.makedirs(pasta_pdfs, exist_ok=True)
                
                # mover todos os pdfs
                shutil.move(caminho_arquivo, os.path.join(pasta_pdfs, arquivo))
    return pasta_pdfs


def separar_por_tema(local_de_busca, tema):

    for raiz, pastas, arquivos in os.walk(arquivos_pdf):
        for arquivo in arquivos:
            caminho_arquivo = os.path.join(raiz, arquivo)
            nome_pdf, extensao = os.path.splitext(caminho_arquivo)
            if extensao =='.pdf' and tema in nome_pdf.lower().replace('_', " ").replace('-', ' '):
                pasta_python = local_de_busca + f'\\{tema.replace(" ", '')}'
                os.makedirs(pasta_python, exist_ok=True)
                shutil.move(caminho_arquivo, os.path.join(pasta_python, arquivo))

arquivos_pdf = mover_pdfs(CAMINHO)
separar_por_tema(arquivos_pdf, ' java ')
separar_por_tema(arquivos_pdf, 'javascript')
separar_por_tema(arquivos_pdf, 'machine learning')
separar_por_tema(arquivos_pdf, ' c ')
separar_por_tema(arquivos_pdf, 'algoritmos')
separar_por_tema(arquivos_pdf, 'matematica')
separar_por_tema(arquivos_pdf, 'sistemas operacionais')
separar_por_tema(arquivos_pdf, 'logica')
separar_por_tema(arquivos_pdf, 'python')
separar_por_tema(arquivos_pdf, 'tenenbaum')
separar_por_tema(arquivos_pdf, 'redes neurais')
