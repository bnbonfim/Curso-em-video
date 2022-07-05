nome = str(input('Diga o nome de uma cidade:')).title().strip()
n1 = nome.split()
s = 'Santo' in n1[0:]
print(s)
###
cid = str(input('Digite o nome da sua cidade:')).strip()
print(cid[:5].upper() == 'SANTO')
