class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.lecturer_grades:
                lecturer.lecturer_grades[course] += [grade]
            else:
                lecturer.lecturer_grades[course] = [grade]
        else:
            return 'Ошибка'

    def midlle_grade(self):
        all_sum = 0
        quantity = 0
        for course in self.courses_in_progress:
            all_sum += sum(self.grades[course])
            quantity += len(self.grades[course])
        middle = all_sum / quantity
        return middle

    def __lt__(self, other):
        if self.midlle_grade() < other.midlle_grade():
            return f'{other.name} {other.surname} имеет среднюю оценку за домашние задания {other.midlle_grade()},' \
                   f' что выше чем у {self.name} {self.surname}, на {other.midlle_grade() - self.midlle_grade()}'
        else:
            return f'{other.name} {other.surname} имеет среднюю оценку за домашние задания {other.midlle_grade()},' \
                   f' что ниже чем у {self.name} {self.surname}, на {self.midlle_grade() - other.midlle_grade()}'

    def __gt__(self, other):
        if self.midlle_grade() > other.midlle_grade():
            return f'{self.name} {self.surname} имеет среднюю оценку за домашние задания {self.midlle_grade()},' \
                   f' что выше чем у {other.name} {other.surname}, на {self.midlle_grade() - other.midlle_grade()}'
        else:
            return f'{self.name} {self.surname} имеет среднюю оценку за домашние задания {self.midlle_grade()},' \
                   f' что ниже чем у {other.name} {other.surname}, на {other.midlle_grade() - self.midlle_grade()}'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {self.midlle_grade()}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.lecturer_grades = {}

    def midlle_grade(self):
        all_sum = 0
        quantity = 0
        for course in self.courses_attached:
            all_sum += sum(self.lecturer_grades[course])
            quantity += len(self.lecturer_grades[course])
        middle = all_sum / quantity
        return middle

    def __lt__(self, other):
        if self.midlle_grade() < other.midlle_grade():
            return f'{other.name} {other.surname} имеет среднюю оценку за лекции {other.midlle_grade()},' \
                   f' что выше чем у {self.name} {self.surname}, на {other.midlle_grade() - self.midlle_grade()}'
        else:
            return f'{other.name} {other.surname} имеет среднюю оценку за лекции {other.midlle_grade()},' \
                   f' что ниже чем у {self.name} {self.surname}, на {self.midlle_grade() - other.midlle_grade()}'

    def __gt__(self, other):
        if self.midlle_grade() > other.midlle_grade():
            return f'{self.name} {self.surname} имеет среднюю оценку за лекции {self.midlle_grade()},' \
                   f' что выше чем у {other.name} {other.surname}, на {self.midlle_grade() - other.midlle_grade()}'
        else:
            return f'{self.name} {self.surname} имеет среднюю оценку за лекции {self.midlle_grade()},' \
                   f' что ниже чем у {other.name} {other.surname}, на {other.midlle_grade() - self.midlle_grade()}'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {self.midlle_grade()}'


class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}'


def middle_grade_students(students, course):
    total_grades = 0
    total_students = 0
    for student in students:
        if course in student.courses_in_progress:
            total_grades += sum(student.grades[course])
            total_students += len(student.grades[course])

    if total_students > 0:
        return total_grades / total_students
    else:
        return 0


def middle_grade_lecturer(lecturers, course):
    total_grades = 0
    total_lecturers = 0
    for lecturer in lecturers:
        if course in lecturer.courses_attached:
            total_grades += sum(lecturer.lecturer_grades[course])
            total_lecturers += len(lecturer.lecturer_grades[course])

    if total_lecturers > 0:
        return total_grades / total_lecturers
    else:
        return 0


student1 = Student('Miles', 'Morales', 'male')
student2 = Student('Gven', 'Stacy', 'female')

mentor1 = Mentor('Peter', 'Parker')
mentor2 = Mentor('Harry', 'Osborn')

lecturer1 = Lecturer('Ben', 'Parker')
lecturer2 = Lecturer('Mary', 'Jane')

reviewer1 = Reviewer('Otto', 'Octavius')
reviewer2 = Reviewer('Cletus', 'Kasady')

student1.finished_courses += ['Введение в программирование']
student2.finished_courses += ['Основы Python']

student1.courses_in_progress += ['Python']
student2.courses_in_progress += ['Java']

mentor1.courses_attached += ['Python']
mentor2.courses_attached += ['Java']

reviewer1.courses_attached += ['Python', 'Java']
reviewer2.courses_attached += ['Python', 'Java']

lecturer1.courses_attached += ['Python']
lecturer2.courses_attached += ['Java']

reviewer1.rate_hw(student1, 'Python', 8)
reviewer1.rate_hw(student2, 'Java', 6)
reviewer2.rate_hw(student1, 'Python', 10)
reviewer2.rate_hw(student2, 'Java', 9)

student1.rate_lecturer(lecturer1, 'Python', 10)
student2.rate_lecturer(lecturer2, 'Java', 4)

print(lecturer1.lecturer_grades)
print(lecturer2.lecturer_grades)
print('___________________________________________________')
print(student1.grades)
print(student2.grades)
print('___________________________________________________')
print(student1)
print(student2)
print('___________________________________________________')
print(lecturer1)
print(lecturer2)
print('___________________________________________________')

course = "Python"
print(f"Средняя оценка за домашние задания по курсу '{course}': {middle_grade_students([student1, student2], course)}")

course = "Python"
print(f"Средняя оценка за лекции по курсу '{course}': {middle_grade_lecturer([lecturer1, lecturer2], course)}")
