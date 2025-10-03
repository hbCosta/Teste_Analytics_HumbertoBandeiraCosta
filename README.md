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

## Requisitos

- Python 3.7 ou superior
- Bibliotecas Python (instalar via pip)

## Dependências

```bash
pip install pandas matplotlib seaborn numpy
```

Ou instalar todas as dependências de uma vez:
```bash
pip install -r requirements.txt
```

## Como Executar

### Executar Pipeline Completo
```bash
python main.py
```

### Executar Módulos Individuais

#### Gerar dados simulados
```bash
python gerar_dados.py
```

#### Limpar dados
```bash
python limpar_dados.py
```

#### Analisar dados
```bash
python analisar_dados.py
```

#### Criar visualizações
```bash
python visualizar_dados.py
```

#### Usar como módulos Python
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

## Arquivos Gerados

Após a execução, os seguintes arquivos serão criados:
- `dados_vendas.csv`: Dataset bruto com dados simulados
- `data_clean.csv`: Dataset limpo após tratamento

## Estrutura dos Dados

O dataset contém as seguintes colunas:
- **Id**: Identificador único da venda
- **Data**: Data da venda (2023)
- **Produto**: Nome do produto vendido
- **Quantidade**: Quantidade vendida (1-9)
- **Preco**: Preço unitário (R$ 5,00 - R$ 70,00)
- **Categoria**: Categoria do produto (Alimentos/Bebidas)


Projeto desenvolvido para Teste para Estagiário de Analytics Quod