# Carregar dados da base Loja, exibir a lista de vendas e exibir o total de vendas realizadas.

# Carregar dados
import baseLoja

lista_vendas = baseLoja.vendas["vendas"]

# Exibir a lista de Vendas
print("Lista de Vendas:")
print("ID | Produto | Categoria | Valor Unitário(R$) | Quantidade")

for venda in lista_vendas:
    print(f"{venda["id"]} | {venda["produto"]} | {venda["categoria"]} | R$ {venda["valor_unitario"]:.2f} | {venda["quantidade"]}")

# Produzir as métricas e exibi-las ao usuário:
print()
print("------- RESUMO ------")
# 1. Total e Média das vendas gerais

total_geral = 0
media_geral = 0

for venda in lista_vendas:
    total_geral += venda["quantidade"] * venda["valor_unitario"]

media_geral = total_geral/len(lista_vendas)

print(f"Total das vendas: R$ {total_geral:.2f}")
print(f"Ticket Médio: R$ {media_geral}")
print(f"Quantidade de Vendas: {len(lista_vendas)}")

#Exibir total de unidades vendidas
total_unidades = 0
for venda in lista_vendas:
    total_unidades += venda["quantidade"]

print(f"Total de Unidades Vendidas: {total_unidades}")

#Maior e Menor Venda
maior_venda = lista_vendas[0]["valor_unitario"] * lista_vendas[0]["quantidade"] 
menor_venda = lista_vendas[0]["valor_unitario"] * lista_vendas[0]["quantidade"] 

for venda in lista_vendas:
    total_venda = venda["quantidade"] * venda["valor_unitario"]

    if total_venda > maior_venda:
        maior_venda = total_venda

    if total_venda < menor_venda:
        menor_venda = total_venda

print(f"Maior Valor de Venda: R$ {maior_venda}")
print(f"Menor Valor de Venda: R$ {menor_venda}")

#Exibir a quantidade de vendas que superou a meta de venda de 5000 reais

#Exibir o nome dos Vendedores

lista_vendedores = []

print("""
----LISTA VENDEDORES-----""")
for venda in lista_vendas:
    if venda["vendedor"] not in lista_vendedores:
        lista_vendedores.append(venda["vendedor"])
    
lista_vendedores.sort()
for vendedor in lista_vendedores:
    print(vendedor)
print("-------------------------")

print(f"""
Quantidade vendedores: {len(lista_vendedores)}
            """)

#Exibir o nome das Regiões
lista_região = []

print("""
----LISTA REGIÕES-----""")

for venda in lista_vendas:
    if venda["regiao"] not in lista_região:
        lista_região.append(venda["regiao"])
    
lista_região.sort()
for região in lista_região:
    print(região)
print("-----------------------")


# 2. Total das vendas por categoria

venda_por_categoria = {}
for venda in lista_vendas:
    if venda["categoria"] not in venda_por_categoria:
        venda_por_categoria[venda["categoria"]] = 0
    
    
    

# 3. Total das vendas por vendedor
# 4. Total das vendas por região