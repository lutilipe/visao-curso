import matplotlib.pyplot as plt

label = ['Batata', 'Processador', 'Camisa']
values = [100, 29, 89]

plt.title("Vendas do Mercadinho BigBom")
plt.xlabel("Produto")
plt.ylabel("Quantidade de itens vendidos")

plt.bar(label, values)
plt.show()