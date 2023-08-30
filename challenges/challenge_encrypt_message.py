# Recebe uma string message e um inteiro key como parâmetros
def encrypt_message(message: str, key: int):
    # Se key não possui o tipo correto, uma exceção é lancada
    if not isinstance(key, int):
        raise TypeError("tipo inválido para key")

    # Se message não possui o tipo correto, uma exceção é lancada
    if not isinstance(message, str):
        raise TypeError("tipo inválido para message")

    # Se key não for um índice positivo válido de message,
    # retorna a string message invertida
    if key not in range(1, len(message)):
        return "".join(reversed(message))

    # Se key for ímpar:
    # divide message no índice key, inverte os caracteres de cada parte,
    # e retorna a união das partes novamente com "_" entre elas

    # Se key for par:
    # divide message no índice key, inverte a posição das partes,
    # inverte os caracteres de cada parte, e retorna a união das partes
    # novamente com "_" entre elas
    part_one = reversed(message[:key])
    part_two = reversed(message[key:])

    if not key % 2:
        part_two, part_one = part_one, part_two

    return "".join(part_one) + "_" + "".join(part_two)
