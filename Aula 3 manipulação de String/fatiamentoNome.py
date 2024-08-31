nomeCompleto = 'Ewerton Henrique Marques da Silva'
primeiro = nomeCompleto[0:7]
ultimo = nomeCompleto[28:33]
print (primeiro)
print (ultimo)

quantidadedeLetrasA = nomeCompleto.count('a')

ultimoNome = 'Silva'
palavra1 = 'souza'
palavra2 = 'santos'

posicaoDaPalavra = nomeCompleto.find(ultimoNome)

verificarPalavra = ultimoNome in nomeCompleto or palavra1 in nomeCompleto or palavra2 in nomeCompleto
print (f'No seguinte nome {nomeCompleto} tem {quantidadedeLetrasA} de letras a')
print (f' O ultimo nome si inicia em {ultimoNome}')
print(f' No nome tem souza, silva ou santos? {verificarPalavra}')