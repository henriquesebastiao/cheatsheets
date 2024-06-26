try:
    print(8 / 0)
except ZeroDivisionError:
    # Aqui você poderia realizar alguma lógica no seu backend
    print('Erro, divisão por zero (EXCEPT)')
    raise  # Relança a exceção
else:
    print('Não deu erro (ELSE)')
finally:  # Sempre executa esse bloco, independente de dar erro ou não
    print('Terminei (FINALLY)')
