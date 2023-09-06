import pytest
from challenges.challenge_encrypt_message import encrypt_message


def test_encrypt_message():
    pass
    # key não é do tipo int
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("abcde", "3")

    # message não é do tipo str
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(3, 3)

    # key não é um índice válido
    assert encrypt_message("abcde", 5) == "edcba"

    # key é par
    assert encrypt_message("abcde", 2) == "edc_ba"

    # key é ímpar
    assert encrypt_message("acb", 1) == "a_bc"
