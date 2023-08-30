def study_schedule(permanence_period, target_time):
    # Se o target_time é vazio, retornar None
    if target_time is None:
        return None

    # Iniciar um contador zerado
    presentes_no_horario = 0

    # Para cada estudante da lista, verificar se está presente no target_time
    for estudante in permanence_period:
        # Se um elemento da tupla é inválido, retornar None
        if type(estudante[0]) != int or type(estudante[1]) != int:
            return None

        # Se estiver presente, somar 1 ao contador
        if estudante[0] <= target_time <= estudante[1]:
            presentes_no_horario += 1

    # Retornar o contador
    return presentes_no_horario
