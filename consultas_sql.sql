
-- ============================================
-- CONSULTA 1: TOTAL DE VENDAS POR PRODUTO
-- ============================================

-- EXPLICAÇÃO DA LÓGICA:
-- Esta consulta lista o nome do produto, categoria e a soma total de vendas
-- (Quantidade * Preço) para cada produto, ordenando pelo valor total de vendas
-- em ordem decrescente.

SELECT
    Produto, 
    Categoria,
    SUM(Quantidade * Preco) AS Total_Vendas
FROM vendas
WHERE Produto IS NOT NULL
GROUP BY Produto, Categoria
ORDER BY Total_Vendas DESC;


-- ============================================
-- CONSULTA 2: PRODUTOS COM MENOR VENDA EM JUNHO DE 2024
-- ============================================

-- EXPLICAÇÃO DA LÓGICA:
-- Esta consulta identifica os produtos que venderam menos no mês de junho de 2024.
-- OBSERVAÇÃO: O dataset atual contém dados de 2023, seria necessário gerar dados
-- para 2024 ou adaptar a consulta para junho de 2023.

SELECT
    Produto,
    SUM(Quantidade) AS Total_Quantidade_Junho
FROM vendas
WHERE MONTH(Data) = 6 AND YEAR(Data) = 2024
    AND Produto IS NOT NULL
GROUP BY Produto   
ORDER BY Total_Quantidade_Junho ASC;
