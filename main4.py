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

    def avg_grade(self):
        all_grades = [g for grades in self.grades.values() for g in grades]
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0

    def __str__(self):
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за лекции: {self.avg_grade()}')

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade() if isinstance(other, Lecturer) else NotImplemented

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade() if isinstance(other, Lecturer) else NotImplemented


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached \
                and course in student.courses_in_progress:
            student.grades.setdefault(course, []).append(grade)

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
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress \
                and course in lecturer.courses_attached:
            lecturer.grades.setdefault(course, []).append(grade)

    def avg_grade(self):
        all_grades = [g for grades in self.grades.values() for g in grades]
        return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0

    def __str__(self):
        courses_in_prog = ', '.join(self.courses_in_progress)
        finished = ', '.join(self.finished_courses)
        return (f'Имя: {self.name}\nФамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.avg_grade()}\n'
                f'Курсы в процессе изучения: {courses_in_prog}\n'
                f'Завершенные курсы: {finished}')

    def __lt__(self, other):
        return self.avg_grade() < other.avg_grade() if isinstance(other, Student) else NotImplemented

    def __eq__(self, other):
        return self.avg_grade() == other.avg_grade() if isinstance(other, Student) else NotImplemented


lect1 = Lecturer('Иван', 'Иванов')
lect2 = Lecturer('Пётр', 'Петров')
stud1 = Student('Ольга', 'Алёхина', 'Ж')
stud2 = Student('Алексей', 'Смирнов', 'М')
rev1 = Reviewer('Семен', 'Борисов')
rev2 = Reviewer('Мария', 'Кузнецова')

lect1.courses_attached = ['Python', 'Git']
lect2.courses_attached = ['Python', 'C++']
stud1.courses_in_progress = ['Python', 'Git']
stud2.courses_in_progress = ['Python', 'C++']
stud1.finished_courses = ['Введение в программирование']
stud2.finished_courses = ['Введение в программирование']
rev1.courses_attached = ['Python', 'C++']
rev2.courses_attached = ['Python', 'Git']


stud1.rate_lecture(lect1, 'Python', 10)
stud1.rate_lecture(lect1, 'Git', 9)
stud1.rate_lecture(lect2, 'Python', 8)
stud2.rate_lecture(lect2, 'Python', 7)
stud2.rate_lecture(lect2, 'C++', 9)

rev1.rate_hw(stud1, 'Python', 10)
rev1.rate_hw(stud2, 'Python', 8)
rev1.rate_hw(stud2, 'C++', 7)
rev2.rate_hw(stud1, 'Git', 9)


print(lect1)
print(lect2)
print(stud1)
print(stud2)
print(rev1)
print(rev2)


print(lect1 > lect2)
print(stud1 < stud2)


def avg_hw(students, course):
    all_grades = [g for s in students for g in s.grades.get(course, [])]
    return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0


def avg_lect(lecturers, course):
    all_grades = [g for l in lecturers for g in l.grades.get(course, [])]
    return round(sum(all_grades) / len(all_grades), 2) if all_grades else 0


students = [stud1, stud2]
lecturers = [lect1, lect2]

print('Средняя оценка студентов по Python:', avg_hw(students, 'Python'))
print('Средняя оценка студентов по Git:', avg_hw(students, 'Git'))
print('Средняя оценка лекторов по Python:', avg_lect(lecturers, 'Python'))
print('Средняя оценка лекторов по C++:', avg_lect(lecturers, 'C++'))
