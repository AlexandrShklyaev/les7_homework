import json


def load_list_of_file(filename):
    """
    Загружает список из файла по его имени(пути)
    :param filename: путь к файлу
    :return: json.loads
    """
    text = ""
    with open(filename, "r", encoding="utf-8") as file:
        data_file = file.readlines()
        for each in data_file:
            text += each.strip()
    return json.loads(text)


def load_students():
    """
    Загружает список студентов из файла
    :return: list
    """
    return load_list_of_file("students.json")


def load_professions():
    """
    Загружает список профессий из файла
    :return: list
    """
    return load_list_of_file("professions.json")


def get_student_by_pk(pk):
    """
    Получает словарь с данными студента по его pk
    :param pk: int
    :return: dict
    """
    list_stud = load_students()
    for each in list_stud:
        if each["pk"] == pk:
            return each


def get_profession_by_title(title):
    """
    Получает словарь с данными профессии по его title
    :param title: str
    :return: dict
    """
    list_prof = load_professions()
    for each in list_prof:
        if each["title"] == title:
            return each


def check_fitness(student, profession):
    """
    Получает словарь пригодности к профессии
    :param student: dict
    :param profession: dict
    :return: dict
    """
    student_set = set(student["skills"])  # скилы студента представим в виде множества
    profession_set = set(profession["skills"])  # скилы для профессии представим в виде множества

    has = student_set.intersection(profession_set)  # пересечение множеств (подходящие скилы)
    lacks = profession_set.difference(student_set)  # различия множеств (отсутствующие скилы)
    proc = int(100 * len(has) / len(profession_set))  # высчитаем процент количество подходящих скилов/кол-во всех

    result_dict = {
        "has": list(has),
        "lacks": list(lacks),
        "fit_percent": proc
    }
    return result_dict
