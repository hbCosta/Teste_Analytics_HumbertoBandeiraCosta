import pandas as pd
import numpy as np

def criar_dataset_simulado(n=50):

    produtos = ["Arroz", "Feijao", "Macarrao", "Azeite", "Cafe", "Acucar", "Refrigerante",
                 "Cerveja", "Carne", "Frango", "Leite", "Ovos", "Queijo"]
    
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

    dados = {
        "Id": range(1, n + 1),
        "Data": pd.to_datetime(np.random.choice(pd.date_range("2023-01-01", "2023-12-31"), n)),
        "Produto": np.random.choice(produtos, n),
        "Quantidade": np.random.randint(1, 10, n),
        "Preco": np.round(np.random.uniform(5, 70, n))
    }
    df = pd.DataFrame(dados)
    df["Categoria"] = df["Produto"].map(categorias)

    df.loc[5, "Produto"] = None
    df.loc[10, "Preco"] = None
    df = pd.concat([df, df.iloc[[20]]])

    print("Dataset bruto\n")
    print(df.head(10))
    return df

def salvar_dados_brutos(df, nome_arquivo="dados_vendas.csv"):
    df.to_csv(nome_arquivo, index=False)
    print(f"\nDados brutos salvos em {nome_arquivo}")   

