import torch

# Verifica se o CUDA (GPU) está disponível
if torch.cuda.is_available():
    device = torch.device("cuda")          # Utiliza a GPU
    print("GPU está disponível.")
    print("Número de GPUs disponíveis:", torch.cuda.device_count())
    print("Nome da GPU disponível:", torch.cuda.get_device_name(0))  # Obtém o nome da GPU atual
    print("Índice da GPU atual:", torch.cuda.current_device())       # Obtém o índice da GPU atual
else:
    device = torch.device("cpu")           # Utiliza a CPU
    print("GPU não está disponível. Usando CPU.")

print("Versão do PyTorch:", torch.__version__)
print("Dispositivo atual:", device)
