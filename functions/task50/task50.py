# -*- coding: utf-8 -*-

'''ЗАДАЧА: ЭКЗАМЕН НА ПОЛУЧЕНИЕ ВОДИТЕЛЬСКИХ ПРАВ
[Начинаем программировать на Python. Тони Гэддис (2022)]

Местный отдел по выдаче удостоверений на право вождения автомобиля попросил
вас создать приложение, которое оценивает письменную часть экзамена на
получение водительских прав. Экзамен состоит из 20 вопросов с множественным
выбором. Вот правильные ответы:
    1.А     6.B     11.A    16.C
    2.С     7.C     12.D    17.B
    3.А     8.A     13.C    18.B
    4.А     9.C     14.A    19.D
    5.D     10.B    15.D    20.A

Ваша программа должна сохранить эти правильные ответы в списке. Программа
должна прочитать из текстового файла ответы испытуемого на каждый из 20
вопросов и сохранить эти ответы в еще одном списке. Для тестирования
приложениявоспользуйтесь файлом student_solution.txt. После того как ответы
испытуемого будут считаны из файла, программа должна вывести сообщение о том,
сдал испытуемый экзамен или нет. (Для сдачи экзамена испытуемый должен
правильно ответить на 15 из 20 вопросов.) Затем программа должна вывести
общее количество вопросов, ответы на которые были правильными,
общее количество вопросов, ответы на которые были неправильными, и список с
номерами вопросов, ответы на которые были неправильными.
'''

CORRECT_ANSWERS = {
    1 : 'A',
    2 : 'C',
    3 : 'A',
    4 : 'A',
    5 : 'D',
    6 : 'B',
    7 : 'C',
    8 : 'A',
    9 : 'C',
    10 : 'B',
    11 : 'A',
    12 : 'D',
    13 : 'C',
    14 : 'A',
    15 : 'D',
    16 : 'C',
    17 : 'B',
    18 : 'B',
    19 : 'D',
    20 : 'A'
}

def make_correct_answ_lst():
    correct_answ_lst = []
    for key in sorted(CORRECT_ANSWERS.keys()):
        correct_answ_lst.append(CORRECT_ANSWERS[key])
    return correct_answ_lst

def get_student_solution():
    student_solution_lst = []
    try:
        f = open('student_solution.txt', 'r')
        for sol in f:
            student_solution_lst.append(sol.strip())
    except Exception as err:
        print(err)
    else:
        f.close()
    return student_solution_lst

def main():
    correct_answ_lst = make_correct_answ_lst()
    student_solution_lst = get_student_solution()
    print('Student solution:')
    print(student_solution_lst)
    # check answers
    wrong_answers = []
    for i in range(len(student_solution_lst)):
        if student_solution_lst[i] != correct_answ_lst[i]:
            wrong_answers.append(i + 1)
    correct = len(correct_answ_lst) - len(wrong_answers) if wrong_answers else 0
    # output
    print()
    print('Result:')
    if correct >= 15:
        print('Exam passed')
    else:
        print('Exam not passed')
    print(f'Correct answers: {correct}')
    print(f'Wrong answers: {len(wrong_answers)}')
    print('Numbers of wrong answers:', ','.join(map(str, wrong_answers)))

if __name__ == '__main__':
    main()
