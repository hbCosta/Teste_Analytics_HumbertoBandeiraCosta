import pandas as pd

def calcular_totais_por_produto(df):
    df = df.copy()  # Cria uma cópia para evitar SettingWithCopyWarning
    df.loc[:, "Total_Venda"] = df["Quantidade"] * df["Preco"]
    total_por_produto = df.groupby("Produto")["Total_Venda"].sum().sort_values(ascending=False)
    return total_por_produto    

def encontrar_produto_mais_vendido(total_por_produto):
    produto_mais_vendido = total_por_produto.idxmax()
    valor_mais_vendido = total_por_produto.max()
    return produto_mais_vendido, valor_mais_vendido

def gerar_relatorio(df):
    total_por_produto =  calcular_totais_por_produto(df)
    print("\nTotal de vendas por produto:\n")
    for produto, valor in total_por_produto.items():
        print(f"{produto}: R$ {valor:.2f}")

    produto_mais_vendido, valor_produto = encontrar_produto_mais_vendido(total_por_produto)
    print(f"\nProduto mais vendido: {produto_mais_vendido} com total de vendas de R$ {valor_produto:.2f}")

    