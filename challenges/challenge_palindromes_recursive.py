def is_palindrome_recursive(word, low_index, high_index):
    # Se for passado uma string vazia, retorne False
    if len(word) == 0:
        return False

    if low_index >= high_index:
        return True

    if word[low_index] == word[high_index]:
        return is_palindrome_recursive(word, low_index + 1, high_index - 1)
    else:
        return False
