# Geral
- Um script foi utilizado para selecionar aleatoriamente 1000 imagens, as quais foram posteriormente rotuladas pelo modelo base GroundDINO, com 5 classes de interesse. Essas imagens foram então divididas em 800 para treinamento e 200 para validação. Em seguida, o modelo destino Yolov8n foi então treinado utilizando as imagens de validação.
  
# Configuracoes
- GPU: NVIDA 1660Ti
- Torch + CUDA: 2.2.2+cu121
- Python 3.12.3

# Rotulacao de imagens (Autodistill)
- Modelo base: GroundDINO
- 1000 imagens
- 800 train
- 200 valid
- Classes: 'Car', 'Bicycle', 'Pedestrian', 'Truck' e 'Traffic sign'
- Tempo: 55:34

# Resultados
## Test1
- Modelo destino: yolov8n
- Epochs: 5
- Tempo: 6:12

**Resultados**
![image](https://github.com/vitorAugusto2/tcc-a2d2-autodistill-yolo/assets/131685750/4610e25e-8c1b-4903-82e3-cd1f58fbec88)
![image](https://github.com/vitorAugusto2/tcc-a2d2-autodistill-yolo/blob/main/runs/detect/test1/yolov8n_200i_5e_train/results.png)

**Matriz de confusao**
![image](https://github.com/vitorAugusto2/tcc-a2d2-autodistill-yolo/blob/main/runs/detect/test1/yolov8n_200i_5e_train/confusion_matrix.png)

**Vizualizacao do resultado de validacao**
![image](https://github.com/vitorAugusto2/tcc-a2d2-autodistill-yolo/blob/main/runs/detect/test1/yolov8n_200i_5e_val/val_batch0_labels.jpg)

#

## Test2
- Model destino: yolov8n
- Epochs: 10
- Tempo: 12:33

**Resultados**
![image](https://github.com/vitorAugusto2/tcc-a2d2-autodistill-yolo/assets/131685750/95d4f461-cee2-4083-b1ca-a0a2f1c2e3f5)
![image](https://github.com/vitorAugusto2/tcc-a2d2-autodistill-yolo/blob/main/runs/detect/test2/yolov8n_200i_10e_train/results.png)

**Matriz de confusao**
![image](https://github.com/vitorAugusto2/tcc-a2d2-autodistill-yolo/blob/main/runs/detect/test2/yolov8n_200i_10e_train/confusion_matrix.png)

**Vizualizacao do resultado de validacao**
![image](https://github.com/vitorAugusto2/tcc-a2d2-autodistill-yolo/blob/main/runs/detect/test2/yolov8n_200i_10e_val/val_batch0_labels.jpg)
