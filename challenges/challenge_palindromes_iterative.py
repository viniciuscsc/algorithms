def is_palindrome_iterative(word):
    # Se for passado uma string vazia, retorne False
    if len(word) == 0:
        return False

    word_reversed = ""

    for index in range(len(word) - 1, -1, -1):
        word_reversed += word[index]

    if word == word_reversed:
        return True
    else:
        return False
