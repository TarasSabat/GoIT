import random

from faker import Faker
from sqlalchemy.exc import SQLAlchemyError

from conf.connect_db import session
from conf.models import Teacher, Group, Student, Subject, Grade

fake = Faker('uk-UA')


# Додавання викладачів
def insert_teachers():
    teachers = [Teacher(fullname=fake.name()) for _ in range(random.randint(3, 5))]
    session.add_all(teachers)


# Додавання груп
def insert_groups():
    groups = [Group(name=fake.word()) for _ in range(3)]
    session.add_all(groups)


# Додавання предметів з id викладача
def insert_subjects():
    teachers = session.query(Teacher).all()
    for _ in range(random.randint(5, 8)):
        subjects = Subject(name=fake.word(), teacher_id = random.choice(teachers).id)
        session.add(subjects)


# Додавання студентів
def insert_students():
    students = []
    groups = session.query(Group).all()
    for _ in range(random.randint(30, 50)):
        student = Student(fullname=fake.name(), group_id=random.choice(groups).id)
        students.append(student)
    session.add_all(students)


# Додавання оцінок
def insert_grades():
    students = session.query(Student).all()
    subjects = session.query(Subject).all()

    for student in students:
        for _ in range(random.randint(0, 20)):
            grades = Grade(student_id=student.id,
                           subject_id=random.choice(subjects).id,
                           grade=random.randint(60, 100),
                           grade_date=fake.date_time_between(start_date="-1y", end_date="now")
                           )
            session.add(grades)


if __name__ == '__main__':
    try:
        insert_teachers()
        insert_groups()
        insert_subjects()
        insert_students()
        insert_grades()
        session.commit()
    except SQLAlchemyError as e:
        print(e)
        session.rollback()
    finally:
        session.close()
