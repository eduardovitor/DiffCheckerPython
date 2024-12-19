import difflib

def exibir_diferencas(arquivo1, arquivo2):
    """
    Compara dois arquivos e exibe as diferenças linha por linha. Independentemente de ordem

    :param arquivo1: Caminho para o primeiro arquivo.
    :param arquivo2: Caminho para o segundo arquivo.
    """
    try:
        with open(arquivo1, 'r', encoding='utf-8') as f1, open(arquivo2, 'r', encoding='utf-8') as f2:
            conteudo1 = f1.readlines()
            conteudo2 = f2.readlines()
        
        conteudo1 = sorted(conteudo1)
        conteudo2 = sorted(conteudo2)
        diferencas = difflib.unified_diff(
            conteudo1, conteudo2,
            fromfile=arquivo1,
            tofile=arquivo2,
            lineterm=''
        )
        with open("difs.txt", "w") as fdif:
            for dif in diferencas:
                fdif.write(dif)
    except FileNotFoundError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    arquivo1 = "arquivo1.csv"
    arquivo2 = "arquivo2.csv"

    exibir_diferencas(arquivo1, arquivo2)

