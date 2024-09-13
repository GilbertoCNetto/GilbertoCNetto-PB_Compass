SELECT 
	l.cod AS CodLivro, 
	l.titulo AS Titulo, 
	a.codautor AS CodAutor, 
	a.nome AS NomeAutor, 
	l.valor AS Valor,
	e.codeditora AS CodEditora,
	e.nome AS NomeEditora
FROM livro l
LEFT JOIN autor a ON a.codautor = l.autor
LEFT JOIN editora e ON e.codeditora = l.editora 
ORDER BY valor DESC 
LIMIT 10
