class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def avg_rate(self):
        sum_ = 0
        len_ = 0
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 0
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}\n'
                f'Средняя оценка за домашние задания: {self.avg_rate()}\n'
                f'Курсы в процессе изучения: {', '.join(self.courses_in_progress)}\n'
                f'Завершенные курсы: {', '.join(self.finished_courses)}')

    def __eq__(best_student, best_student1):
        return(best_student.grades == best_student1.grades)


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}


    def avg_rate(self):
        sum_ = 0
        len_ = 1
        for mark in self.grades.values():
            sum_ += sum(mark)
            len_ += len(mark)
        res = round(sum_ / len_, 2)
        return res

    def avg_rate_course(self, course):
        sum_crs = 0
        len_crs = 1
        for crs in self.grades.keys():
            if crs == course:
                sum_crs += sum(self.grades[course])
                len_crs += len(self.grades[course])
        res = round(sum_crs / len_crs, 2)
        return res


    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}'
                f'\nСредняя оценка за лекции: {self.avg_rate()}')

    def __lt__(self, other):
        return self.avg_rate_course() <= other.avg_rate_course()

class Reviewer(Mentor):

    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return (f'Имя: {self.name} \n'
                f'Фамилия: {self.surname}')


best_student = Student('Roy', 'Eman', 'men')
best_student1 = Student('Pavel', 'Kuznezov', 'men')
best_student.courses_in_progress += ['Java', 'Python']
best_student.finished_courses += ['C+']

best_student1.courses_in_progress += ['Python', 'VC']
best_student1.finished_courses += ['Java']

student_list = [best_student, best_student1]

if (best_student == best_student1):
    print("Лучший студент")
else:
    print(best_student1.name, "Лучший студент")

cool_lecturer = Lecturer('Some', 'Buddy')
cool_lecturer1 = Lecturer('Igor', 'Ivanov')
cool_lecturer.courses_attached += ['Python']
lecturer_list = [cool_lecturer, cool_lecturer1]

cool_reviewer = Reviewer('Maria', 'Utkina')
cool_reviewer1 = Reviewer('Svetlana', 'Kotova')
cool_reviewer.courses_attached += ['Python', 'VC']
cool_reviewer1.courses_attached += ['Java', 'C+']

cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)
cool_reviewer1.rate_hw(best_student1, 'Python', 10)
cool_reviewer1.rate_hw(best_student1, 'Python', 8)

best_student.rate_lecturer(cool_lecturer, 'Python', 7)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)
best_student1.rate_lecturer(cool_lecturer1, 'Python', 8)
best_student1.rate_lecturer(cool_lecturer1, 'Python', 9)


