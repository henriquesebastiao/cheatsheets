"""
Interpolação básica de strings
s - string
d e i - inteiro
f - float
x e X - Hexadeicmal
"""

nome = 'Henrique'
dinheiro = 512.64
id = 0xFFAFFF

variavel = '%s tem R$%.2f e seu id é: 0x%x' % (nome, dinheiro, id)
print(variavel)
