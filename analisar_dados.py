
import pandas as pd

def calcular_totais_por_produto(df):

    # Criar cópia do DataFrame para evitar modificar o original
    df = df.copy()
    
    # Calcular valor total de cada venda (Quantidade × Preço)
    df.loc[:, "Total_Venda"] = df["Quantidade"] * df["Preco"]
    
    # Agrupar por produto, somar os totais e ordenar de forma decrescente
    total_por_produto = df.groupby("Produto")["Total_Venda"].sum().sort_values(ascending=False)
    
    return total_por_produto    

def encontrar_produto_mais_vendido(total_por_produto):

    # Encontrar o índice com maior valor
    produto_mais_vendido = total_por_produto.idxmax()
    
    # Obter o valor máximo de vendas
    valor_mais_vendido = total_por_produto.max()
    
    return produto_mais_vendido, valor_mais_vendido

def gerar_relatorio(df):

    # Calcular faturamento total para cada produto
    total_por_produto = calcular_totais_por_produto(df)

    print("\nTotal de vendas por produto:\n")
    
    # Iterar sobre cada produto e exibir seu faturamento formatado
    for produto, valor in total_por_produto.items():
        print(f"{produto}: R$ {valor:.2f}")


    # Encontrar o produto com maior faturamento
    produto_mais_vendido, valor_produto = encontrar_produto_mais_vendido(total_por_produto)
    
    # Exibir resultado do produto mais vendido
    print(f"\nProduto mais vendido: {produto_mais_vendido} com total de vendas de R$ {valor_produto:.2f}")