"""
Generators retornando um valor novo a cada vez que é chamado,
não salvando todos os itens na memória como ocorreria com uma list comprehension

Um bom exemplo seria um script para gerar muitas combinações de senhas
sem ter salva-las na memória sobrecarregando o computar para somente depois usar os dados.
"""


def pgen(iterable):
    if hasattr(iterable, '__iter__'):
        for item in iterable:
            print(item)
    else:
        raise TypeError(f'O objeto {iterable} não é iterável')


# Generetor expressions
print('Generetor expressions:')
gen = (i for i in range(10))
pgen(gen)

# Generator functions
print('\nGenerator functions:')


def gen_func(lenght: int):
    number = 0
    while True:
        yield number

        number += 1
        if number >= lenght:
            return


gen = gen_func(10)
pgen(gen)

# Yield from
print('\nYield from:')


def gen1():
    yield 1
    yield 2
    yield 3


def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6


gen = gen2()
pgen(gen)
pgen(1)
