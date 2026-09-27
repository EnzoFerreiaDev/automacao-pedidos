import pandas as pd
from validacao import validacao

try:
    dados = pd.read_excel("planilha.xlsx")
except:
    print("Arquivo não encontrado. Verifique se 'planilha.xlsx' esta na pasta certa.")
    exit()

dados["status"] = dados.apply(validacao, axis=1)

dados.to_excel("saida/Planilha_pedidos.xlsx", index=False)   

print(dados)
