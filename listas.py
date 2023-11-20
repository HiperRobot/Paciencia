def adiciona_item(lista, item):
    """Adiciona um item ao final da lista."""
    lista.append(item)

def remove_item(lista, item):
    """Remove um item da lista."""
    if item in lista:
        lista.remove(item)

def conta_itens(lista):
    """Conta o número de itens na lista."""
    return len(lista)

def embaralha_lista(lista):
    """Embaralha os itens da lista."""
    import random
    random.shuffle(lista)

def ordena_lista(lista):
    """Ordena os itens da lista em ordem crescente."""
    lista.sort()
