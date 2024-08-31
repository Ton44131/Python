# texto = 'Alex Caio Ewerton Isaac Ruth Stefane'

# # Juntar todos os caracters e os separar por um delimitador

# joiString = '-'.join(texto)
# print(joiString) 

# # Divide as palavras de um texto

# splitString = texto.split()
# print(splitString[4])




# Desafio 1
nome = input('escreva o seu nome')
nomeMaiusculo = nome.upper()
nomeMinusculo = nome.lower()
nomeSemEspaço = nome.replace (' ', '')
primeiroNome = nome.split()
print (f'seu nome e {nome}')
print (f'seu nome com todas as letras maiusculas {nomeMaiusculo}')
print (f'seu nome com todas as letras maiusculas {nomeMinusculo}')
print (f'seu nome sem espaços {nomeSemEspaço}')
print(primeiroNome[0])


# desafio 2
palavra = 'Santo'
cidade = input('Digite o nome de uma cidade')
verificarPalavra = palavra in cidade

print(f'A cidade escolhida foi {cidade} e ela {verificarPalavra} Santo')

# # Desafio 3
palavra = 'Silva'
nome = input('Digite seu nome')
verificarPalavra = palavra in nome
print(f'Seu nome é {nome} e ele {verificarPalavra} Silva')

# Desafio 4
palavra = input('Escreva alguma palavra')
textoMaiusculo = palavra.upper()
palavra1 = 'A'
letraA = textoMaiusculo.count('A')
posicaoPalavra = textoMaiusculo.find(palavra1)
posicaoPalavra1 = textoMaiusculo.rfind(palavra1)
print(f'Na palavra tem {letraA}  letras A ')
print(f'Na palavra a letra A aparece em {posicaoPalavra}  ')
print(f'Na palavra a letra A aparece em {posicaoPalavra1}  ')


# Desafio 5
nome = input('escreva seu nome')
primeiroNome = nome.split()
ultimoNome = nome.rsplit()
print(f'Primeiro nome e {primeiroNome[0]}')
print(f'Ultimo nome e {ultimoNome[-1]}')
