
import pandas as pd             
import matplotlib.pyplot as plt  
import seaborn as sns           
from datetime import datetime 

def criar_graficos(df):
  
    # Converter a coluna Data para períodos mensais (formato YYYY-MM)
    df["Mes"] = df["Data"].dt.to_period("M")
    
    # Agrupar dados por mês e somar as quantidades vendidas
    vendas_mensais = df.groupby("Mes")["Quantidade"].sum()

    # Criar figura com tamanho específico 
    plt.figure(figsize=(12, 6))
    
    # Plotar gráfico de linha com marcadores circulares nos pontos
    vendas_mensais.plot(kind="line", marker='o')
    
    plt.title("Tendencias de vendas Mensais")
    plt.xlabel("Mês")
    plt.ylabel("Quantidade Vendida")
    
    # Rotacionar labels do eixo X para melhor legibilidade
    plt.xticks(rotation=45)
    
    # Adicionar grade com transparência para facilitar leitura
    plt.grid(True, alpha=0.3)
    
    # Ajustar layout automaticamente para evitar sobreposições
    plt.tight_layout()
    
    # Exibir o gráfico
    plt.show()


def analisar_padroes_vendas(df):
    
    # Agrupar vendas por categoria 
    vendas_por_categoria = df.groupby("Categoria")["Quantidade"].sum()

    # Extrair trimestre das datas 
    df["Trimestre"] = df["Data"].dt.quarter
    
    # Agrupar vendas por trimestre do ano
    vendas_trimestre = df.groupby("Trimestre")["Quantidade"].sum()
    
    # Criar figura com dois subgráficos lado a lado
    plt.figure(figsize=(15, 6))

    # === GRÁFICO 1: Vendas por Categoria ===
    plt.subplot(1, 2, 1)  # Posição: 1 linha, 2 colunas, gráfico 1
    vendas_por_categoria.plot(kind='bar', color='skyblue')
    plt.title("Vendas por Categoria", fontsize=14)
    plt.xlabel("Categoria", fontsize=12)
    plt.ylabel("Quantidade Vendida", fontsize=12)
    # Rotacionar labels das categorias para melhor legibilidade
    plt.xticks(rotation=45, fontsize=10)
    plt.yticks(fontsize=10)

    # === GRÁFICO 2: Vendas por Trimestre ===
    plt.subplot(1, 2, 2)  # Posição: 1 linha, 2 colunas, gráfico 2
    vendas_trimestre.plot(kind='bar', color='lightcoral')
    plt.title("Vendas por Trimestre", fontsize=14)
    plt.xlabel("Trimestre", fontsize=12)
    plt.ylabel("Quantidade Vendida", fontsize=12)
    plt.xticks(rotation=0, fontsize=10)
    plt.yticks(fontsize=10)

    # Ajustar espaçamento entre os subgráficos automaticamente
    plt.tight_layout()
    
    # Exibir os gráficos
    plt.show()

    # === ANÁLISE DE INSIGHTS ===
    print("\n=== INSIGHTS IDENTIFICADOS ===")
    print("1. Padrão por categoria: Observado uma diferença de vendas entre categorias")
    print("2. Sazonalidade trimestral: Variações nas vendas ao longo dos trimestres do ano")
    print("3. Distribuição de produtos: Alguns produtos têm maior demanda que outros")

    return vendas_por_categoria, vendas_trimestre
