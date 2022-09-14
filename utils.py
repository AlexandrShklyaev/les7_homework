import json


def load_list_of_file(filename):  # Загружает список из файла по его имени(пути)
    text = ""
    with open(filename, "r", encoding="utf-8") as file:
        data_file = file.readlines()
        for each in data_file:
            text += each.strip()
    return json.loads(text)


def load_students():  # Загружает список студентов из файла
    return load_list_of_file("students.json")


def load_professions():  # Загружает список профессий из файла
    return load_list_of_file("professions.json")


def get_student_by_pk(pk):  # Получает словарь с данными студента по его pk
    list_stud = load_students()
    for each in list_stud:
        if each["pk"] == pk:
            return each
    # return {}


def get_profession_by_title(title):  # Получает словарь с данными профессии по его title
    list_prof = load_professions()
    for each in list_prof:
        if each["title"] == title:
            return each
    # return {}


def check_fitness(student, profession):
    student_dict = set(get_student_by_pk(student)["skills"])
    profession_dict = set(get_profession_by_title(profession)["skills"])

    has = student_dict.intersection(profession_dict)
    lacks = profession_dict.difference(student_dict)
    proc = int(100 * len(has) / len(profession_dict))

    result_dict = {
        "has": list(has),
        "lacks": list(lacks),
        "fit_percent": proc
    }
    return result_dict
