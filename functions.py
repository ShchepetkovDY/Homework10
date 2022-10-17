import json


def load_json():
    """
    Функция чтения из файла
    Args: -
    Returns: список с кандидатами
    """
    with open("candidates.json", "r", encoding="utf-8") as file:
        candidates = json.load(file)
        return candidates


def format_candidates(candidates):
    """
    Функция, которая форматирует список кандидатов
    Args: список кандидатов
    Returns: отформатированный список кандидатов
    """

    result = "<pre>"

    for candidate in candidates:
        result += f"""
            {candidate["name"]}\n
            {candidate["position"]}\n
            {candidate["skills"]}\n
        """
    result += "</pre>"
    return result


def get_all():
    """
    Функция, которая выводит всех кандидатов
    """
    return load_json()


def get_by_pk(uid):
    """
    Функция, которая осуществляет поиск кандидатов по pk
    Args: uid
    Returns: Кандидат в зависимости от pk
    """
    candidates = get_all()
    for candidate in candidates:
        if candidate["pk"] == uid:
            return candidate
    return None


def get_by_skills(skill):
    """
    Функция, которая осуществляет поиск кандидатов по скиллам
    Args: Название скилла
    Returns: Кандидаты в зависимости от скилла
    """
    candidates = get_all()
    result = []
    for candidate in candidates:
        if skill in candidate["skills"].lower().split(", "):
            result.append(candidate)
    return result
