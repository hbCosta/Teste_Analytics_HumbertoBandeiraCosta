
import pandas as pd

def limpar_dados(df):

    # Preencher produtos nulos com "Desconhecido"
    df = df.fillna({"Produto": "Desconhecido"})
    
    # Preencher preços nulos com a média dos preços válidos
    df = df.fillna({"Preco": df["Preco"].mean()})

    
    # Remover linhas completamente duplicadas
    df = df.drop_duplicates()

    # Converter Quantidade para numérico, substituindo valores inválidos por 0
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors='coerce').fillna(0)
    
    # Converter Preço para numérico, mantendo valores nulos como NaN
    df["Preco"] = pd.to_numeric(df["Preco"], errors='coerce')
    
    # Garantir tipos corretos: Quantidade como inteiro e Preço como float
    df = df.astype({"Quantidade": "int64", "Preco": "float64"})

    return df

def salvar_dados_limpos(df, nome_arquivo="data_clean.csv"):

    # Salvar DataFrame em arquivo CSV 
    df.to_csv(nome_arquivo, index=False)
   
    print(f"\nDados limpos salvos em {nome_arquivo}")   