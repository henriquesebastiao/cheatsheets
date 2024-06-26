"""
Como Python ś singleton por padrão, o módulo só é importado uma vez, mesmo que seja importado várias vezes.
Quando importamos o modulo novamente, o Python não executa o código novamente, ele apenas retorna a referência do módulo na memória.

Mas se você quiser que o código seja executado novamente, você pode usar o reload() da biblioteca importlib.
"""

import importlib

print('Tentando importar várias vezes:')
import modulo

for _ in range(10):
    import modulo

print('\nRecarregando a importação várias vezes:')
for _ in range(10):
    importlib.reload(modulo)
