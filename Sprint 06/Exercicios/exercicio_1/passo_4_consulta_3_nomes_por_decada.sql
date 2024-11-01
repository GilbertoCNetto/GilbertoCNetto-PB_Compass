SELECT decada, nome, frequencia_por_nome
FROM (
    SELECT 
        FLOOR(ano / 10) * 10 AS decada,  -- Calcula a década
        nome,
        SUM(total) AS frequencia_por_nome,
        ROW_NUMBER() OVER (PARTITION BY FLOOR(ano / 10) * 10 ORDER BY SUM(total) DESC) AS rank
    FROM meubanco.nomes
    WHERE ano >= 1950
    GROUP BY FLOOR(ano / 10) * 10, nome
) AS nomes_rankeados
WHERE rank <= 3
ORDER BY decada, frequencia_por_nome DESC;