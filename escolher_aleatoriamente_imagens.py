import os
import random
import shutil

def copiar_imagens_aleatorias(pasta_imagens, pasta_destino, qte):
    imagens_disponiveis = os.listdir(pasta_imagens)

    if len(imagens_disponiveis) < qte:
        print("A pasta não contém imagens suficientes.")
        return

    imagens_selecionadas = random.sample(imagens_disponiveis, qte)

    for imagem in imagens_selecionadas:
        caminho_imagem_origem = os.path.join(pasta_imagens, imagem)
        caminho_imagem_destino = os.path.join(pasta_destino, imagem)
        shutil.copy(caminho_imagem_origem, caminho_imagem_destino)

    print(f"{qte} imagens selecionadas e copiadas com sucesso.")


pasta_imagens = "C:/Users/vitor/.vscode/scritps/test_tcc/total_images"
pasta_destino = "C:/Users/vitor/.vscode/scritps/test_tcc/images"
quantidade_imagens = 1000

copiar_imagens_aleatorias(pasta_imagens, pasta_destino, quantidade_imagens)