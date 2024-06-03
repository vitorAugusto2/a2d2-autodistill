# DATASET A2D2
## Link para Download
Alguns arquivos não estão completos devido ao seu tamanho, mas você pode baixá-los através deste [link]([https://www.a2d2.audi/a2d2/en/download.html](https://aev-autonomous-driving-dataset.s3.eu-central-1.amazonaws.com/a2d2-preview.tar)).

## Estrutura do diretório
``` python
Data A2D2
    |
    |------camera_lidar
    |            |
    |            |----- cena (...)
    |            |       |
    |            |       |-- camera
    |            |       |       |
    |            |       |       |-- cam_front_center (...)
    |            |       |                |-- .JSON
    |            |       |                |-- .NPZ
    |            |       |       
    |            |       |
    |            |       |-- lidar
    |            |               |-- cam_front_center (...)
    |            |                        |-- .NPZ
    |            |       
    |     bus_signals.JSON
    |
    |
    |
    |------camera_lidar_semantic
    |            |
    |            |------cena (...)
    |            |        |
    |            |        |-- camera
    |            |        |       |
    |            |        |       |-- cam_front_center (...)
    |            |        |                |-- .JSON
    |            |        |                |-- .NPZ
    |            |        |           
    |            |        |-- label
    |            |        |       |-- cam_front_center (...)
    |            |        |                |-- .PNG
    |            |        |       
    |            |        |
    |            |        |-- lidar
    |            |        |       |-- cam_front_center (...)
    |            |        |                |-- .NPZ
    |            |
    |        class_list.JSON
    |  
    |
    |
    |------camera_lidar_semantic_bboxes
    |            |
    |            |------ cena (...)
cams_lidars.JSON |        |
                 |        |-- camera
                 |        |       |
                 |        |       |-- cam_front_center (...)
                 |        |                |-- .JSON
                 |        |                |-- .NPZ
                 |        |           
                 |        |-- label
                 |        |       |-- cam_front_center (...)
                 |        |                |-- .PNG
                 |        |       
                 |        |-- label3D
                 |        |       |-- cam_front_center (...)
                 |        |                |-- .JSON
                 |        |-- lidar
                 |        |       |-- cam_front_center (...)
                 |        |                |-- .NPZ
                 |
            class_list.JSON
```
            
# Configurações do veículo
Cada cidade fornecida possui um arquivo Configuration.json contendo informações abrangentes sobre o setup do veículo, 
câmeras e sensores. Nas Tabelas 1, 2 e 3, são apresentadas as configurações dos veículos para cada sensor.

### Tabela 1 – Arquivo de configuração: Vehicle Configuration
| **Campo**          | **Descrição**                                    |
|--------------------|--------------------------------------------------|
| origin             | Cordenadas de origem do Veículo.                 |  
| X-axis e Y-axis    | Cordenadas da posicão atual do veículo.          |
| ego-dimensions     | Dimensões X,Y e Z do veículo utilizado (metros). |

### Tabela 2 – Arquivo de configuração: Lidar Configuration
| **Campo**          | **Descrição**                                                             |
|--------------------|---------------------------------------------------------------------------|
| origin             | Cordenadas do sensor em relação a origem do carro.                        |  
| X-axis e Y-axis    | Cordenadas do sensor em relação ao frame de referência do carro.          |

### Tabela 3 – Arquivo de configuração: Camera Configuration
| **Campo**          | **Descrição**                                                    |
|--------------------|------------------------------------------------------------------|
| tstamp-delay       | Atraso configurado entre os frames da câmera (default 0).        |
| origin             | Cordenadas da câmera em relação a origem do carro.               |
| X-axis e Y-axis    | Cordenadas do câmera em relação ao frame de referência do carro. |  
| CamMatrix          | Matriz da câmera das imagens não distorcidas.                    |   
| CamMatrixOriginal  | Matriz da câmera das imagens distorcidas.                        |   
| Distortion         | Parametros utilizados nas imagens originais.                     |   
| Resolution         | Resolução da câmera.                                             |   
| Lens               | Tipo de lente utilizado (Fisheye ou Telecam).                    |   

Em cada cidade, os dados estão organizados por frame, sendo que cada captura é composta
por três arquivos distintos: uma imagem em formato PNG, um arquivo JSON que referencia
as configurações da imagem e dos sensores naquele instante, e um arquivo NPZ contendo as
informações dos sensores LiDAR. Na Tabela 4 e 5, são apresentadas as informações dos sensores
LiDAR.

### Tabela 4 – Arquivo de configuração: Image Frame Information
| **Campo**        | **Descrição**                                                        | 
|------------------|----------------------------------------------------------------------|
| cam_tstamp       | Timestamp do frame.                                                  |   
| cam_name         | Qual das cameras foi utilizada.                                      |  
| image_zoom       | Zoom da imagem (default 1.0).                                        |   
| image_png        | Nome do arquivo png referenciado                                     |   
| pcld_npz         | Nome do arquivo npz referenciado (arquivo com os dados dos sensores) |   
| origin           | Cordenadas da câmera em relação a origem do carro.                   |  
| X-axis e Y-axis  | Cordenadas da câmera em relação ao frame de referência do carro.     |   
| lidar_ids        | Relação de todos os Lidar Ids.                                       | 

### Tabela 5 – Arquivo de configuração: Lidar Frame Information
| Campo       | Descrição                                                      |
|-------------|----------------------------------------------------------------|
| col         | Coordenadas dos pontos do sensor.                              |
| row         | Coordenadas dos pontos do sensor.                              |  
| distance    | Distância do sensor até o objeto medido.                       |
| azimuth     | Ângulo do sensor até o objeto medido.                          |   
| timestamp   | Timestamp da aferição do sensor.                               |   
| points      | Pontos X, Y e Z dos pontos do sensor (col, row e distance).    |  
| depth       | Profundidade do ponto de medição.                              |  
| lidar_id    | ID do sensor que realizou a medição.                           | 
| reflectance | Mede a quantidade refletida pelo objeto que está sendo medido. | 

Fonte: [GEYER et al. 2020](https://www.a2d2.audi/a2d2/en.html)  
