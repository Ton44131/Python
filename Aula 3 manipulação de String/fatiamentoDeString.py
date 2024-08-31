texto = 'cursO de python'
setimaPosicaoTexto = texto[6]
print(setimaPosicaoTexto)

textoCurso = texto [0:5]
print(textoCurso)

textoPython = texto [9:15]
print(textoPython)

# Contar o numero de caracteres dentro do texto

quantidadeChar = len(texto)
print(f'Na frase temos {quantidadeChar} cracteres')

# Contar um numero específico de letras dentro do texto
quantidadeDeLetrasO = texto.count('o')
print(f'Na frase temos {quantidadeDeLetrasO} letras O')

# Indentificar a posição onde indica uma palavra
palavra = 'python'
posicaoPalavra = texto.find(palavra)
print(f'A palavra se inicia na posição {posicaoPalavra}')

# Indentificar se existe a palavra no texto
verificarPalavra = palavra in texto
print (f'A palavra {palavra} esta no texto? {verificarPalavra}')