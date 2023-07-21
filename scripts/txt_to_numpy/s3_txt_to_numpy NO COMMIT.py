import os
import numpy as np

def limpar_arquivo_txt(caminho_arquivo):
    # Ler o conteúdo do arquivo de texto
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()

    # Remover colchetes, espaços em branco e quebras de linha indesejados
    dados_limpos = []
    for linha in linhas:
        linha_limpa = linha.replace('[', '').replace(']', '').replace('\n', '').replace(' ', '').rstrip(',')
        dados_limpos.append(linha_limpa)

    # Salvar os dados limpos em um novo arquivo
    caminho_arquivo_limpo = caminho_arquivo.replace('.txt', '_limpo.txt')
    with open(caminho_arquivo_limpo, 'w') as arquivo_limpo:
        for linha in dados_limpos:
            arquivo_limpo.write(linha + '\n')

    return caminho_arquivo_limpo

# Caminho para a pasta que contém os arquivos de texto originais
pasta_origem = r"C:\Users\Lenovo\Desktop\IC\Pitt - Trimmed\Pitt\Dementia\cookie\txt_files\Concatenated"

# Listar todos os arquivos de texto na pasta
arquivos_txt = [arquivo for arquivo in os.listdir(pasta_origem) if arquivo.endswith('.txt')]

# Processar cada arquivo de texto e salvar os arquivos limpos em uma nova pasta
pasta_destino = r"C:\Users\Lenovo\Desktop\IC\Pitt - Trimmed\Pitt\Dementia\cookie\txt_files\Concatenated\txt_files_limpos"
os.makedirs(pasta_destino, exist_ok=True)

for arquivo_txt in arquivos_txt:
    caminho_arquivo_original = os.path.join(pasta_origem, arquivo_txt)
    caminho_arquivo_limpo = limpar_arquivo_txt(caminho_arquivo_original)
    caminho_arquivo_destino = os.path.join(pasta_destino, os.path.basename(caminho_arquivo_limpo))
    os.rename(caminho_arquivo_limpo, caminho_arquivo_destino)

# Ler os arquivos limpos e converter em arrays NumPy
#dados_arrays = []
#for arquivo_txt in os.listdir(pasta_destino):
#    caminho_arquivo_limpo = os.path.join(pasta_destino, arquivo_txt)
#    dados_array = np.loadtxt(caminho_arquivo_limpo, delimiter=',')
#    dados_arrays.append(dados_array)

# Agora dados_arrays contém uma lista de arrays NumPy, onde cada elemento da lista é um arquivo limpo convertido em array.
# Faça o que você precisa com esses arrays.

print("cabei :)")
