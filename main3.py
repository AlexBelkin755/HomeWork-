class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def average_grade(self):
        total = sum([sum(grades) for grades in self.grades.values()])
        count = sum([len(grades) for grades in self.grades.values()])
        return round(total / count, 2) if count != 0 else 0

    def __str__(self):
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за лекции: {self.average_grade()}'
        )

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return NotImplemented
        return self.average_grade() == other.average_grade()


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course].append(grade)
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.courses_in_progress = []
        self.finished_courses = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course].append(grade)
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def average_grade(self):
        total = sum([sum(grades) for grades in self.grades.values()])
        count = sum([len(grades) for grades in self.grades.values()])
        return round(total / count, 2) if count != 0 else 0

    def __str__(self):
        courses_in_progress = ', '.join(self.courses_in_progress)
        finished_courses = ', '.join(self.finished_courses)
        return (
            f'Имя: {self.name}\n'
            f'Фамилия: {self.surname}\n'
            f'Средняя оценка за домашние задания: {self.average_grade()}\n'
            f'Курсы в процессе изучения: {courses_in_progress}\n'
            f'Завершенные курсы: {finished_courses}'
        )

    def __lt__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() < other.average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented
        return self.average_grade() == other.average_grade()


lect1 = Lecturer('Иван', 'Иванов')
lect2 = Lecturer('Пётр', 'Петров')
stud1 = Student('Ольга', 'Алёхина', 'Ж')
stud2 = Student('Алексей', 'Смирнов', 'М')
rev1 = Reviewer('Семен', 'Борисов')


lect1.courses_attached += ['Python']
lect2.courses_attached += ['Python']
stud1.courses_in_progress += ['Python']
stud2.courses_in_progress += ['Python']
rev1.courses_attached += ['Python']


stud1.rate_lecture(lect1, 'Python', 9)
stud1.rate_lecture(lect2, 'Python', 8)
rev1.rate_hw(stud1, 'Python', 10)
rev1.rate_hw(stud2, 'Python', 7)


print(lect1)
print(stud1)
print(rev1)


print(lect1 > lect2)  # True
print(stud1 < stud2)  # False
