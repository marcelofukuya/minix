import matplotlib.pyplot as plt
import numpy as np

def ler_medias(nome_arquivo):
    tempos_cpu = []
    tempos_io = []

    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            partes = linha.split()

            if len(partes) != 3:
                continue
            
            tipo = partes[0]
            tempo = float(partes[2])

            if tipo == "CPU":
                tempos_cpu.append(tempo)
            elif tipo == "IO":
                tempos_io.append(tempo)

    media_cpu = sum(tempos_cpu) / len(tempos_cpu) if (tempos_cpu) else 0
    media_io = sum(tempos_io) / len(tempos_io) if tempos_io else 0

    return media_cpu, media_io

#Quantidades de processos testados
quantidades = [10, 50, 100, 200]

#Arquivos de cada algoritmo
arquivos = {
    "Padrão": {
        10: "minix_10.txt",
        50: "minix_50.txt",
        100: "minix_100.txt",
        200: "minix_200.txt",
    },
    "Round-robin": {
        10: "rr_10.txt",
        50: "rr_50.txt",
        100: "rr_100.txt",
        200: "rr_200.txt",
    },
    "Fair-share": {
        10: "fs_10.txt",
        50: "fs_50.txt",
        100: "fs_100.txt",
        200: "fs_200.txt",
    },
    "Loteria": {
        10: "loteria_10.txt",
        50: "loteria_50.txt",
        100: "loteria_100.txt",
        200: "loteria_200.txt",
    }
}

medias_cpu = {}
medias_io = {}

for algoritmo, arquivos_algoritmo in arquivos.items():
    medias_cpu[algoritmo] = []
    medias_io[algoritmo] = []

    for qtd in quantidades:
        media_cpu, media_io = ler_medias(arquivos_algoritmo[qtd])
        medias_cpu[algoritmo].append(media_cpu)
        medias_io[algoritmo].append(media_io)

def plotar_grafico(dados, titulo, nome_saida):
    x = np.arange(len(quantidades))
    largura = 0.2

    plt.figure(figsize=(8, 5))

    for i, (algoritmo, medias) in enumerate(dados.items()):
        deslocamento = (i - 1.5) * largura
        plt.bar(x + deslocamento, medias, largura, label=algoritmo, edgecolor="black", linewidth=1)
    
    plt.title(titulo)
    plt.xlabel("Número de processos")
    plt.ylabel("Tempo médio (s)")
    plt.xticks(x, quantidades)
    plt.legend()
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.tight_layout()
    plt.savefig(nome_saida, dpi=300)
    plt.show()

plotar_grafico(medias_cpu, "Processos CPU-bound", "grafico_cpu_bound.png")

plotar_grafico(medias_io, "Processos IO-bound", "grafico_io_bound.png")