# Задание 3
# Напишите класс Designer, который учитывает количество международных премий.
# Подсказки в коде занятия в разделе “Домашнее задание задача 3”.


class Employee:
    def __init__(self, name, seniority):
        self.name = name
        self.seniority = seniority
        self.grade = 1

    def grade_up(self):
        """Повышает уровень сотрудника"""
        self.grade += 1

    def publish_grade(self):
        """Публикация результатов аккредитации сотрудников"""
        print(self.name, self.grade)

    def check_if_it_is_time_for_upgrade(self):
        pass


class Designer(Employee):
    def __init__(self, name, seniority, awards):
        super().__init__(name, seniority)
        self.awards = awards

    def give_award(self):
        self.awards += 1
        self.seniority += 2

        if self.seniority % 7 == 0:
            self.grade_up()

    def check_if_it_is_time_for_upgrade(self):
        # для каждой аккредитации увеличиваем счетчик на 1
        # пока считаем, что все разработчики проходят аккредитацию
        self.seniority += 1

        # условие повышения сотрудника из презентации
        if self.seniority % 7 == 0:
            self.grade_up()

        # публикация результатов
        return self.publish_grade()


# test
elena = Designer('Елена', seniority=0, awards=2)
for i in range(20):
    if i % 4 == 0:
        elena.give_award()
    elena.check_if_it_is_time_for_upgrade()
