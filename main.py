import utils


def input_pk():  # вводим номер студента пока он не будет корректным (из цифр)
    while True:
        pk = input("Введите номер студента: ")
        if pk.isdigit():
            pk = int(pk)
            break
        else:
            print("Номер должен состоять только из цифр")
    return pk


if __name__ == '__main__':
    stud_pk = input_pk()  # вводим номер студента
    student = utils.get_student_by_pk(stud_pk)  # получаем студента по номеру
    if student != None:  # если нашли студента
        full_name = student["full_name"]  # получаем имя студента
        stud_skils = ", ".join(student["skills"])  # получаем скилы студента и форматируем результат
        print(f"Студент {full_name}\nЗнает {stud_skils}")
    else:  # если по номеру студента не нашли
        print("У нас нет такого студента")
        quit()

    prof_title = input(f"Выберите специальность для оценки студента {full_name}: ").title()  # ввод специальности
    profession = utils.get_profession_by_title(prof_title)  # получим специальность по названию
    if profession != None:  # если нашли специальность
        data_stud_prof = utils.check_fitness(student, profession)  # получим данные пригодности
        has = ", ".join(data_stud_prof["has"])  # получаем нужные скилы студента и форматируем результат
        lacks = ", ".join(data_stud_prof["lacks"])  # получаем отсутствующие скилы и форматируем результат
        fit_percent = data_stud_prof["fit_percent"]  # процент пригодности
        print(f"Пригодность {fit_percent}%\n{full_name} знает {has}\n{full_name} не знает {lacks}")
    else:
        print("У нас нет такой специальности")
        quit()
