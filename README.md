# ✂️ AUTODISTILL
## 1. INTRODUCAO
- O Autodistill usa modelos básicos grandes e mais lentos para treinar modelos supervisionados pequenos e mais rápidos. Usando autodistill, você pode passar de imagens não rotuladas para inferência em um modelo personalizado executado na borda, sem intervenção humana no meio
- [Rotular automaticamente conjuntos de dados](https://docs.autodistill.com/)
  
## 2. CONCEITOS BASICOS
- Para usar autodistill, você insere dados não rotulados em um modelo base que usa uma ontologia para rotular um conjunto de dados que é usado para treinar um modelo de destino que gera um modelo destilado ajustado para executar uma tarefa específica.
- Autodistill define várias primitivas básicas:
    - **Tarefa** - Uma tarefa define o que um modelo de destino irá prever. A tarefa de cada componente (modelo base, ontologia e modelo de destino) de um autodistillpipeline deve corresponder para que sejam compatíveis entre si. Atualmente, a detecção de objetos e a segmentação de instâncias são suportadas por meio da detectiontarefa. classificationo suporte será adicionado em breve.
    - **Modelo Base** - Um Modelo Base é um modelo básico grande que sabe muito sobre muita coisa. Os modelos básicos costumam ser multimodais e podem executar muitas tarefas. Eles são grandes, lentos e caros. Exemplos de modelos básicos são GroundedSAM e a próxima variante multimodal do GPT-4. Usamos um modelo base (junto com dados de entrada não rotulados e uma ontologia) para criar um conjunto de dados.
    - **Ontologia** - uma Ontologia define como seu Modelo Base é solicitado, o que seu Conjunto de Dados descreverá e o que seu Modelo Alvo irá prever. Uma ontologia simples é aquela CaptionOntologyque solicita um modelo base com legendas de texto e os mapeia para nomes de classes. Outras Ontologias podem, por exemplo, usar um vetor CLIP ou imagens de exemplo em vez de uma legenda de texto; uma ontologia em Computação é um modelo de dados que representa um conjunto de conceitos dentro de um domínio e os relacionamentos entre estes.
    - **Conjunto de dados** - um conjunto de dados é um conjunto de dados rotulados automaticamente que pode ser usado para treinar um modelo de destino. É a saída gerada por um Modelo Base.
    - **Modelo de destino** - um modelo de destino é um modelo supervisionado que consome um conjunto de dados e gera um modelo destilado que está pronto para implantação. Os modelos de destino geralmente são pequenos, rápidos e ajustados para executar muito bem uma tarefa específica (mas não generalizam muito além das informações descritas em seu conjunto de dados). Exemplos de modelos de destino são YOLOv8 e DETR.
    - **Modelo Destilado** – um Modelo Destilado é o resultado final do autodistillprocesso; é um conjunto de pesos ajustados para sua tarefa que pode ser implantado para obter previsões.
### 2.1. Conceitos Principais
- Um modelo base , que é usado para rotular dados automaticamente. Os exemplos incluem Grounding DINO, Grounded SAM, DETIC CLIP. 
- Um modelo de destino , que é treinado nos dados rotulados automaticamente. Os exemplos incluem YOLOv5, [**YOLOv8**](https://github.com/autodistill/autodistill-yolov8) e DETR.

## 3. MODELO BASE UTILIZADO
- **Grounding DINO**
    - [Grounding DINO](https://github.com/autodistill/autodistill-grounding-dino): é um detector de objetos de disparo zero eficaz que pode identificar uma ampla variedade de objetos, desde carros até capas de discos de vinil.

# 🔎 ULTRALYTICS YOLOv8
## 1. INTRODUCAO 
- modelo de deteccao de objetos e segmentacao de imagens em tempo real. Aprendizagem profunda e visao computacional. Alem disso, consegue classificar os objetos.
- 5 modelos [YOLOv8](https://docs.ultralytics.com/pt/models/yolov8/): YOLOv8n, YOLOv8s, YOLOv8m, YOLOv8l e YOLOv8x

## 2. CONFIGURACOES
### 2.1. Modos
- YOLO Os modelos podem ser utilizados em diferentes modos, dependendo do problema específico que estás a tentar 
resolver. Estes modos incluem:
    - [**train** ](https://docs.ultralytics.com/pt/modes/train/): Para treinar um modelo YOLOv8 num conjunto de dados personalizado.
    - [**val**](https://docs.ultralytics.com/pt/modes/val/): Para validar um modelo YOLOv8 depois de ter sido treinado.
    - [**predict**](https://docs.ultralytics.com/pt/modes/predict/): Para fazer previsões utilizando um modelo YOLOv8 treinado em novas imagens ou vídeos.
    - [**export**](https://docs.ultralytics.com/pt/modes/export/): Para exportar um modelo YOLOv8 para um formato que possa ser usado para implantação.
    - [**track**](https://docs.ultralytics.com/pt/modes/track/): Para seguir objectos em tempo real utilizando um modelo YOLOv8 .
    - [**benchmark**](https://docs.ultralytics.com/pt/modes/benchmark/): Para aferir a velocidade e a precisão das exportações YOLOv8 (ONNX, TensorRT, etc.).
### 2.2. Tarefas
- YOLO podem ser utilizados para uma variedade de tarefas, incluindo deteção, segmentação, classificação e pose. Estas 
tarefas diferem no tipo de resultados que produzem e no problema específico que foram concebidos para resolver.
    - [**detect**](https://docs.ultralytics.com/pt/tasks/detect/): Para identificar e localizar objectos ou regiões de interesse numa imagem ou vídeo. O resultado de um 
    detetor de objectos é um conjunto de caixas delimitadoras que envolvem os objectos na imagem, juntamente com 
    etiquetas de classe e pontuações de confiança para cada caixa.
    - [**segment**](https://docs.ultralytics.com/pt/tasks/segment/): Para dividir uma imagem ou vídeo em regiões ou pixels que correspondem a diferentes objectos ou 
    classes. O resultado de um modelo de segmentação de instâncias é um conjunto de máscaras ou contornos que delineia 
    cada objeto na imagem, juntamente com etiquetas de classe e pontuações de confiança para cada objeto.
    - [**classify**](https://docs.ultralytics.com/pt/tasks/classify/): Para prever a etiqueta da classe de uma imagem de entrada. O resultado de um classificador de 
    imagens é uma etiqueta de classe única e uma pontuação de confiança.
    - [**pose**](https://docs.ultralytics.com/pt/tasks/pose/): Para identificar objectos e estimar os seus pontos-chave numa imagem ou vídeo.
    - [**OBB**](https://docs.ultralytics.com/pt/tasks/obb/): Caixas delimitadoras orientadas (ou seja, rodadas) adequadas para imagens de satélite ou médicas.
### 2.3. Argumentos
As definições de treino para os modelos YOLO englobam vários [hiperparâmetros e configurações](https://docs.ultralytics.com/pt/modes/train/#train-settings) utilizados durante o processo de treino. Estas definições influenciam o desempenho, a velocidade e a precisão do modelo. As principais definições de treino incluem o tamanho do lote, a taxa de aprendizagem, o momento e a diminuição do peso. Além disso, a escolha do optimizador, a função de perda e a composição do conjunto de dados de treino podem ter impacto no processo de treino. O ajuste cuidadoso e a experimentação com estas definições são cruciais para otimizar o desempenho.

## 3. METRICAS DE TREINAMENTO
![image](https://github.com/vitorAugusto2/tcc-a2d2/assets/131685750/efb27566-e7c7-42ed-aaf8-c876da5e7e23)

- **Epoch**: ciclos de treinamento ou numero de vezes que iteramos 
- **GPU_mem**: memoria da GPU
- **box_loss**: perda de caixa -> perda da localizacao
- **cls_loss**: perda de classificacao -> especifica se o objeto esta classificado corretamente ou nao
- **dfl_loss**: perda focal distribuida -> detectores de objetos sem ancora 
- **instances**: numero de instancias -> numeros de rotulos no lote atual
- **size**: tamanho da entrada -> tamanho da imagem (padrao 640)
- **class**: quantidade de classe
- **images**: quantidade de imagens
- **instances**: quantidade de instancias
- **Boxp**: precisao da caixa
- **R**: valor de recuperacao
- **mAP50**: metrica de precisao

## 4. METRICAS DE DESEMPENHO
[Tabelas com o desempenho de deteccao](https://docs.ultralytics.com/pt/models/yolov8/#supported-tasks-and-modes)

| Modelo  | Tamanho (pixéis)  | mAPval | Velocidade CPU ONNX (ms)  | Velocidade A100 TensorRT (ms) | Params (M) | FLOPs (B)  |
|---------|-------------------|--------|---------------------------|-------------------------------|------------|------------|
| YOLOv8n | 640               | 37.3   | 80.4                      | 0.99                          | 3.2        | 8.7        |
| YOLOv8s | 640               | 44.9   | 128.4                     | 1.20                          | 11.2       | 28.6       |
| YOLOv8m | 640               | 50.2   | 234.7                     | 1.83                          | 25.9       | 78.9       |
| YOLOv8l | 640               | 52.9   | 375.2                     | 2.39                          | 43.7       | 165.2      |
| YOLOv8x | 640               | 53.9   | 479.1                     | 3.53                          | 68.2       | 257.8      |

- Os modelos Detect, Segment e Pose são pré-treinados no conjunto de dados **COCO**, enquanto os modelos classificacao são pré-treinados no conjunto de dados **ImageNet**. 
- **tamanho(pixels)**: resolucao das imagens (padrao=640)
- **Deteccao (**COCO**)/ média de precisão**: mAPval50-95 -> 50 a 95 indica a média da precisão média em diferentes níveis de confiança de detecção, que vão de 50% a 95% de confiança
- **Velocidade CPU ONNX (ms)**: tempo médio de inferência em milissegundos para os modelos executando em uma CPU utilizando a estrutura ONNX 
- **Velocidade A100 TensorRT (ms)**: tempo médio de inferência em milissegundos para os modelos executando em um A100 TensorRT
- **params (M)**: número de parâmetros (em milhões) que o modelo possui
- **FLOPs (B)**: número de operações de ponto flutuante (em bilhões) que o modelo realiza durante a inferência.


## 5. GRAFICO DE TREINAMENTO
![Resultado do grafico de treinamento](https://github.com/vitorAugusto2/tcc-a2d2-autodistill-yolo/blob/main/runs/detect/test2/yolov8n_200i_10e_train/results.png)
### 5.1. Metricas de treinamento (conjunto de treinamento)
- **train/box_loss**: perda (loss) associada à localização (bounding box)
- **train/cls_loss**: perda associada à classificação dos objetos (ou seja, atribuir a categoria correta aos objetos detectados) 
- **train/dfl_loss**: "defocus loss", objetos fora de foco em imagens
### 5.2. Metricas de validacao (conjunto de validacao)
- **val/box_loss**: perda associada à localização dos objetos
- **val/cls_loss**: perda associada à classificação dos objetos
- **val/dfl_loss**: perda associada à localização dos objetos
### 5.3. Metricas de avaliacao (acuracia)
- **metrics/precision(B)**: Precisão (Precision) para a classe 'B'. Isso geralmente se refere à proporção de verdadeiros positivos (TP) sobre a soma de TP e falsos positivos (FP).
- **metrics/recall(B)**: Revocação (Recall) para a classe 'B'. Isso geralmente se refere à proporção de TP sobre a soma de TP e falsos negativos (FN).
- **metrics/mAP50(B)**: Precisao média com threshold de IoU de 0.5 para a classe 'B'.
- **metrics/mAP50-95(B)**: Precisao média com threshold variando de 0.5 a 0.95 para a classe 'B'.
