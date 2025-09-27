from gerar_dados import criar_dataset_simulado, salvar_dados_brutos
from limpar_dados import limpar_dados, salvar_dados_limpos
from analisar_dados import gerar_relatorio

def main():
    print("Gerando dataset simulado...")
    df_bruto = criar_dataset_simulado(50)
    salvar_dados_brutos(df_bruto, "dados_vendas.csv")

    print("\nLimpando dados...")
    df_limpo = limpar_dados(df_bruto)
    salvar_dados_limpos(df_limpo, "data_clean.csv")

    print("\nAnalisando dados...")
    gerar_relatorio(df_limpo)

if __name__ == "__main__":
    main()