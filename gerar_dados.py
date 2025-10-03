
import pandas as pd  
import numpy as np  

def criar_dataset_simulado(n=50):


    # Lista de produtos típicos de supermercado para simulação
    produtos = ["Arroz", "Feijao", "Macarrao", "Azeite", "Cafe", "Acucar", "Refrigerante",
                 "Cerveja", "Carne", "Frango", "Leite", "Ovos", "Queijo"]
    
    # Dicionário que associa cada produto à sua categoria
    categorias = {
        "Arroz": "Alimentos",
        "Feijao": "Alimentos", 
        "Macarrao": "Alimentos",
        "Azeite": "Alimentos",
        "Cafe": "Alimentos",
        "Acucar": "Alimentos",
        "Refrigerante": "Bebidas",  
        "Cerveja": "Bebidas",     
        "Carne": "Alimentos",
        "Frango": "Alimentos",
        "Leite": "Alimentos",
        "Ovos": "Alimentos",
        "Queijo": "Alimentos"
    }

    # Geração Dos Dados Aleatórios
    
    dados = {
        # ID sequencial de 1 até n
        "Id": range(1, n + 1),
        
        # Datas aleatórias distribuídas ao longo do ano de 2023
        "Data": pd.to_datetime(np.random.choice(pd.date_range("2023-01-01", "2023-12-31"), n)),
        
        # Produtos escolhidos aleatoriamente da lista disponível
        "Produto": np.random.choice(produtos, n),
        
        # Quantidades entre 1 e 9 
        "Quantidade": np.random.randint(1, 10, n),
        
        # Preços entre R$ 5,00 e R$ 70,00 
        "Preco": np.round(np.random.uniform(5, 70, n))
    }
    
    # Criar DataFrame a partir do dicionário de dados
    df = pd.DataFrame(dados)
    
    # Mapear categoria para cada produto usando o dicionário
    df["Categoria"] = df["Produto"].map(categorias)

    # Insere produto nulo na linha 5 (índice 5) para testar limpeza
    df.loc[5, "Produto"] = None
    
    # Insere preço nulo na linha 10 (índice 10) para testar limpeza
    df.loc[10, "Preco"] = None
    
    # Cria duplicata da linha 20 para testar remoção de duplicatas
    df = pd.concat([df, df.iloc[[20]]])

    # Visualização dos dados gerados
    print("Dataset bruto\n")
    print(df.head(10))  # Exibir primeiras 10 linhas para verificação
    
    return df

def salvar_dados_brutos(df, nome_arquivo="dados_vendas.csv"):

    # Salvar DataFrame em arquivo CSV sem incluir índice automático do pandas
    df.to_csv(nome_arquivo, index=False)

    print(f"\nDados brutos salvos em {nome_arquivo}")   
