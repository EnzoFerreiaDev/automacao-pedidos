import pandas as pd
import unicodedata

try:
    dados = pd.read_excel("planilha.xlsx")
except:
    print("Arquivo não encontrado. Verifique se 'planilha.xlsx' esta na pasta certa.")
    exit()
    
catalog = ["Camisa G", "Bermuda GG", "Calça P", "Casaco G", "Boné", "Jaqueta P", "Calça G", "Moletom G", "Bermuda PP"]

def normalizar(texto):
    texto_sem_acento = unicodedata.normalize("NFKD", texto)
    resultado = ""
    for caractere in texto_sem_acento:
        if not unicodedata.combining(caractere):
            resultado = resultado + caractere
    return resultado.lower()

def extrair_digitos(texto):
    resultado = ""
    for caractere in texto:
        if caractere.isdigit():
            resultado = resultado + caractere
    return resultado

catalog_normalizado =  [normalizar(item) for item in catalog]

def validacao(linha):
    erros = []
    if pd.isna(linha["cliente"]):
        erros.append("cliente vazio")

    if normalizar(linha["produto"]).strip() not in catalog_normalizado:
        erros.append("produto não encontrado")

    try:
        valor_numerico = int(linha["quantidade"])
        if valor_numerico <= 0:
             erros.append('quantidade inválida')
    except:
        erros.append('quantidade inválida')

    digitos = len(extrair_digitos(linha["telefone"]))
    if digitos != 10 and digitos != 11:
        erros.append("telefone inválido")

    if pd.isna(linha["data"]):
        erros.append("data vazia")

    if erros:
        return "ERRO: " + "; ".join(erros)
    return "OK"

dados["status"] = dados.apply(validacao, axis=1)

dados.to_excel("saida/Planilha_pedidos.xlsx", index=False)   

print(dados)
