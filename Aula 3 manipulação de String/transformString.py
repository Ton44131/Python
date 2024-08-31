# Trocando palavras dentro de um texto
texto = 'Ewerton Henrique'

trocaPalavra = texto.replace('Henrique', 'Souza')

print(trocaPalavra)

# Deixando os caracteres no maiúsculo

texto = 'ewErTonhSENAI@gmail.com'
textoMaiusculo = texto.upper
print(textoMaiusculo)

# Deixando os caracteres no minusculo
textoMinusculo = texto.lower
print(textoMinusculo)

# Deixando a primeira letra de cada palavra em maiúsculo

texto = 'meu primeiro curso do SENAI'
textoTitle = texto.title()
print(textoTitle)


# Deixando a primeira letra do texto em maiúsculo
textoCaptalizate = texto.capitalize()
print(textoCaptalizate)

# Elimina espaços inúteis
texto = '      SENAI       '
print(f'A palavra {texto} tem {len(texto)} caracters')


textoStrip = texto.strip()

print(f'A palavra {textoStrip} tem {len(textoStrip)} caracters')
