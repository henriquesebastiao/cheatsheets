from array import array

int_array = array('h', [x for x in range(10)])
lista = [10, 11, 12]

print(int_array)


int_array.fromlist(lista)
print(int_array)
print(int_array.itemsize)  # Tamanho em Bytes de cada item da lista na memória
