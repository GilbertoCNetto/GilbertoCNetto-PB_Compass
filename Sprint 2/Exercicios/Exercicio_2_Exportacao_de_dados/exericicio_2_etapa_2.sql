SELECT 
	e.codeditora AS CodEditora,
	e.nome AS NomeEditora,
	count(l.editora) AS QuantidadeLivros
FROM editora e
INNER JOIN livro l ON l.editora = e.codeditora 
GROUP BY l.editora 
ORDER BY QuantidadeLivros DESC 
LIMIT 5
