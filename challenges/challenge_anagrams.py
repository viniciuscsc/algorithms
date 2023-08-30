def ordenar_lista_string(lista_string):
    if len(lista_string) == 1:
        return lista_string

    indice_meio = len(lista_string) // 2
    lado_esq = lista_string[:indice_meio]
    lado_dir = lista_string[indice_meio:]

    lado_esq = ordenar_lista_string(lado_esq)
    lado_dir = ordenar_lista_string(lado_dir)

    lista_string_ordenada = []
    indice_esquerda = 0
    indice_direita = 0

    while indice_esquerda < len(lado_esq) and indice_direita < len(lado_dir):
        if lado_esq[indice_esquerda] < lado_dir[indice_direita]:
            lista_string_ordenada.append(lado_esq[indice_esquerda])
            indice_esquerda += 1
        else:
            lista_string_ordenada.append(lado_dir[indice_direita])
            indice_direita += 1

    lista_string_ordenada.extend(lado_esq[indice_esquerda:])
    lista_string_ordenada.extend(lado_dir[indice_direita:])

    return lista_string_ordenada


def is_anagram(first_string, second_string):
    # Retorne False se alguma das palavras passadas por parâmetro for
    # uma string vazia
    if len(first_string) == 0 or len(second_string) == 0:
        return False

    first_string = first_string.lower()
    second_string = second_string.lower()

    first_string_ordenada = "".join(ordenar_lista_string(list(first_string)))
    second_string_ordenada = "".join(ordenar_lista_string(list(second_string)))

    comparacao = first_string_ordenada == second_string_ordenada

    return (first_string_ordenada, second_string_ordenada, comparacao)
