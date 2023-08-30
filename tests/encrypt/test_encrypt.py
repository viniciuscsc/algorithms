from challenges.challenge_encrypt_message import encrypt_message

import pytest


def test_encrypt_message():
    # Se key não possui o tipo correto, uma exceção é lancada
    # TypeError("tipo inválido para key")
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("123456", "3")

    # Se message não possui o tipo correto, uma exceção é lancada
    # TypeError("tipo inválido para message")
    with pytest.raises(TypeError, "tipo inválido para message"):
        encrypt_message(123456, 3)

    # Se key não for um índice positivo válido de message,
    # retorna a string message invertida
    assert encrypt_message("123456", -1) == "654321"  # índice negativo
    assert encrypt_message("123456", 10) == "654321"  # índice posicao invalida

    # Se key for ímpar:
    # divide message no índice key, inverte os caracteres de cada parte,
    # e retorna a união das partes novamente com "_" entre elas
    assert encrypt_message("123456", 3) == "321_654"

    # Se key for par:
    # divide message no índice key, inverte a posição das partes,
    # inverte os caracteres de cada parte, e retorna a união das partes
    # novamente com "_" entre elas
    assert encrypt_message("123456", 4) == "65_4321"
