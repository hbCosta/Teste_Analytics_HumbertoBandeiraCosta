import pandas as pd

def limpar_dados(df):
    # Corrige FutureWarnings usando fillna no DataFrame completo
    df = df.fillna({"Produto": "Desconhecido"})
    df = df.fillna({"Preco": df["Preco"].mean()})

    df = df.drop_duplicates()

    # Corrige FutureWarning e SettingWithCopyWarning usando astype no DataFrame completo
    df["Quantidade"] = pd.to_numeric(df["Quantidade"], errors='coerce').fillna(0)
    df["Preco"] = pd.to_numeric(df["Preco"], errors='coerce')
    
    # Converte os tipos usando astype no DataFrame completo
    df = df.astype({"Quantidade": "int64", "Preco": "float64"})

    return df

def salvar_dados_limpos(df, nome_arquivo="data_clean.csv"):
    df.to_csv(nome_arquivo, index=False)
    print(f"\nDados limpos salvos em {nome_arquivo}")   
    

