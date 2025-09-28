from gerar_dados import criar_dataset_simulado, salvar_dados_brutos
from limpar_dados import limpar_dados, salvar_dados_limpos
from analisar_dados import gerar_relatorio
from visualizar_dados import criar_graficos, analisar_padroes_vendas


def main():
    print("Gerando dataset simulado...")
    df_bruto = criar_dataset_simulado(50)
    salvar_dados_brutos(df_bruto, "dados_vendas.csv")

    print("\nLimpando dados...")
    df_limpo = limpar_dados(df_bruto)
    salvar_dados_limpos(df_limpo, "data_clean.csv")

    print("\nAnalisando dados...")
    gerar_relatorio(df_limpo)
    print("\nCriando visualizações...")
    criar_graficos(df_limpo)
    print("\nAnalisando padrões de vendas...")
    analisar_padroes_vendas(df_limpo)

if __name__ == "__main__":
    main()