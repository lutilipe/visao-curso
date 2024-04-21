import pandas as pd

dados = {
    'Data': ['2024-01-01', '2024-01-02',
    '2024-01-03', '2024-01-04'],
    'Vendas_Produto_A': [100, 120, 90, 110],
    'Vendas_Produto_B': [80, 85, 88, 85]
}

df = pd.DataFrame(dados)
df['Data'] = pd.to_datetime(df['Data'])

address = ["Delhi", "Bangalore", "Chennai", "Patna"]
 
df["Address"] = address

teste = ["isso", "eh", "um", "teste"]
df["Teste"] = teste
print(df)