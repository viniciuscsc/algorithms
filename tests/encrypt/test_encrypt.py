import pytest

from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    # Se key não possui o tipo correto, uma exceção é lancada
    # TypeError("tipo inválido para key")
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("ABCDEF", "3")

    # Se message não possui o tipo correto, uma exceção é lancada
    # TypeError("tipo inválido para message")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)

    # Se key não for um índice positivo válido de message,
    # retorna a string message invertida
    assert encrypt_message("ABCDEF", -1) == "FEDCBA"  # índice negativo
    assert encrypt_message("ABCDEF", 10) == "FEDCBA"  # índice posicao invalida

    # Se key for ímpar:
    # divide message no índice key, inverte os caracteres de cada parte,
    # e retorna a união das partes novamente com "_" entre elas
    assert encrypt_message("ABCDEF", 3) == "CBA_FED"

    # Se key for par:
    # divide message no índice key, inverte a posição das partes,
    # inverte os caracteres de cada parte, e retorna a união das partes
    # novamente com "_" entre elas
    assert encrypt_message("ABCDEF", 4) == "FE_DCBA"
