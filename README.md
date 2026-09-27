# Automação de Validação de Pedidos

Script em Python que lê uma planilha de pedidos, identifica erros de digitação e gera um relatório com o status de cada linha.

## O problema

Comércios que registram pedidos manualmente (planilha, caderno, WhatsApp) estão sujeitos a erros de digitação — telefone incompleto, produto que não existe no catálogo, quantidade digitada errada. Esses erros geram retrabalho e atrasos na hora de separar e entregar os pedidos.

## O que o script faz

1. Lê uma planilha de pedidos (`.xlsx`)
2. Valida cada pedido contra 5 regras diferentes
3. Marca cada linha com o status `OK` ou `ERRO`, detalhando o(s) problema(s) encontrado(s)
4. Gera uma nova planilha com o resultado, pronta para o dono do negócio revisar

## Erros detectados

- Cliente não informado
- Telefone com quantidade de dígitos inválida
- Produto fora do catálogo (com tolerância a acentuação e maiúsculas/minúsculas)
- Quantidade não numérica ou menor/igual a zero
- Data não informada

## Como rodar

\`\`\`bash
pip install pandas openpyxl
python main.py
\`\`\`

O script espera encontrar o arquivo `planilha.xlsx` na mesma pasta. O resultado é salvo em `saida/Planilha_pedidos.xlsx`.

## Resultado do teste

Em uma planilha de teste com 14 pedidos, o script identificou 5 pedidos com problema (36%), cobrindo os 5 tipos de erro mapeados.

## Tecnologias

- Python
- pandas
- openpyxl

## Autor

Enzo Ferreira