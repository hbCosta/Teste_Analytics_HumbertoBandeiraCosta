# Teste Analytics - Análise de Dados de Vendas

Projeto de análise exploratória de dados simulados de vendas, incluindo limpeza, visualização e consultas SQL.

## Estrutura do Repositório

```
├── main.py                  # Script principal - executa todo o pipeline
├── gerar_dados.py          # Geração de dataset simulado
├── limpar_dados.py         # Limpeza e tratamento dos dados
├── analisar_dados.py       # Análise e relatórios estatísticos
├── visualizar_dados.py     # Gráficos e visualizações
├── consultas_sql.sql       # Consultas SQL para análise
├── relatorio_insights.md   # Relatório com insights e recomendações
├── dados_vendas.csv        # Dataset bruto gerado
├── data_clean.csv          # Dataset limpo
└── README.md               # Este arquivo
```

## Dependências

```bash
pip install pandas matplotlib seaborn numpy
```

## Como Executar

### Executar Pipeline Completo
```bash
python main.py
```

### Executar Módulos Individuais
```python
# Gerar apenas os dados
from gerar_dados import criar_dataset_simulado
df = criar_dataset_simulado(50)

# Limpar dados
from limpar_dados import limpar_dados
df_limpo = limpar_dados(df)

# Criar visualizações
from visualizar_dados import criar_graficos, analisar_padroes_vendas
criar_graficos(df_limpo)
analisar_padroes_vendas(df_limpo)
```

## Funcionalidades

- **Geração de dados**: Dataset simulado com 50 registros de vendas
- **Limpeza**: Tratamento de valores nulos e duplicatas
- **Análise**: Relatórios de faturamento por produto
- **Visualização**: Gráficos de tendência e padrões de vendas
- **SQL**: Consultas para análise de dados
- **Insights**: Relatório com recomendações de negócio

## Autor

Projeto desenvolvido para Teste para Estagiário de Analytics Quod