from collections import Counter


def verifica_comprimento_nums(lista_nums):
    # não passe nenhum valor
    # nums não tenha pelo menos 2 inteiros
    if len(lista_nums) < 2:
        return False


def find_duplicate(nums):
    verifica_comprimento_nums(nums)

    # Dicionário que indica a qtd de cada elemento
    counter = Counter(nums)

    # Lista de Tuplas que indica a qtd de cada elemento
    mais_comuns = counter.most_common()

    maior_qtd_num = 1

    for num, qtd_num in mais_comuns:
        # algum valor é string ou é inteiro negativo
        if type(num) == str or num < 0:
            return False

        if qtd_num > maior_qtd_num:
            maior_qtd_num = qtd_num

    # não há valores repetidos
    if maior_qtd_num == 1:
        return False

    return mais_comuns[0][0]
