import json

dado = {
    'nome': 'Henrique',
    'sobrenome': 'Sebastiao',
    'nascimento': [5, 4, 2003],
    'idade': 21,
}

with open('dado.json', 'w') as file:
    json.dump(dado, file, ensure_ascii=False, indent=2)

with open('dado.json', 'r', encoding='utf8') as file:
    dado = json.load(file)
    print(dado['nome'])
