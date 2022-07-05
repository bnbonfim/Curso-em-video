f = str(input('Digite uma frase:')).lower().strip()
print('Aparecem {} letras "a"'.format(f.count('a')))
print('A letra "a" aparece primeiro na posição {}'.format(f.find('a')+1))
print('A letra "a" aparece por ultimo na posição {}'.format(f.rfind('a')+1))
