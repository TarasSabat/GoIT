from sqlalchemy import func, desc

from conf.connect_db import session
from conf.models import Teacher, Group, Student, Subject, Grade


def select_01():  # Знаходимо 5 студентів із найбільшим середнім балом з усіх предметів.
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM students s
    JOIN grades g ON s.id = g.student_id
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 5;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2
                                                                    ).label('average_grade')).select_from(
        Student).join(Grade).group_by(Student.id
                                      ).order_by(desc('average_grade')).limit(5).all()
    return result


def select_02():  # Знаходимо студента із найвищим середнім балом з певного предмета.
    """
    SELECT
        s.id,
        s.fullname,
        ROUND(AVG(g.grade), 2) AS average_grade
    FROM grades g
    JOIN students s ON s.id = g.student_id
    where g.subject_id = 1
    GROUP BY s.id
    ORDER BY average_grade DESC
    LIMIT 1;
    """
    result = session.query(Student.id, Student.fullname, func.round(func.avg(Grade.grade), 2
                                                                    ).label('average_grade')).select_from(
        Grade).join(Student).filter(Grade.subject_id == 1
                                    ).group_by(Student.id).order_by(desc('average_grade')).limit(1).all()
    return result


def select_03(subject_id):  # Знаходимо середній бал у групах з певного предмета.
    """
    SELECT
        groups.name AS group_name,
        AVG(grades.grade) AS average_grade
    FROM grades
    JOIN students ON grades.student_id = students.id
    JOIN groups ON students.group_id = groups.id
    WHERE grades.subject_id = :subject_id    -- Вказуємо id предмета, для якого шукається середній бал груп
    GROUP BY groups.name;
    """
    result = session.query(Group.name.label('group_name'), func.avg(Grade.grade).label('average_grade')
                           ).join(Student, Group.id == Student.group_id).join(Grade,
                                                                              Student.id == Grade.student_id
                                                                              ).filter(
        Grade.subject_id == subject_id).group_by(Group.name).all()
    return result


def select_04():  # Знаходимо середній бал на потоці (по всій таблиці оцінок).
    '''
    SELECT AVG(grade) AS average_grade FROM grades;
    '''
    result = session.query(func.avg(Grade.grade).label('average_grade')).scalar()
    return result


def select_05(teacher_id):  # Знаходимо які курси читає певний викладач.
    '''
    SELECT subjects.name AS course_name
    FROM subjects
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE teachers.id = :teacher_id;
    '''
    result = session.query(Subject.name.label('course_name')).join(Teacher).filter(
        Teacher.id == teacher_id).all()
    return result


def select_06(group_id):  # Знаходимо який список студентів у певній групі.
    '''
    SELECT * FROM students WHERE group_id = :group_id;
    '''
    result = session.query(Student.id.label('id'), Student.fullname.label('fullname'),
                           Student.group_id.label('group_id')).filter(Student.group_id == group_id).all()
    return result


def select_07(group_id, subject_id):  # Знаходимо оцінки студентів у окремій групі з певного предмета.
    '''
    SELECT students.fullname, grades.grade
    FROM students
    JOIN groups ON students.group_id = groups.id
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE group_id = :group_id AND subject_id = :subject_id;
    '''
    result = session.query(Student.fullname, Grade.grade).join(Group, Student.group_id == Group.id
                                                               ).join(Grade,
                                                                      Student.id == Grade.student_id).join(
        Subject, Grade.subject_id == Subject.id
    ).filter(Group.id == group_id, Subject.id == subject_id).all()
    return result


def select_08(teacher_id):  # Знаходимо середній бал, який ставить певний викладач зі своїх предметів.
    '''
    SELECT teachers.fullname AS teacher_name, AVG(grades.grade) AS average_grade
    FROM teachers
    JOIN subjects ON teachers.id = subjects.teacher_id
    JOIN grades ON subjects.id = grades.subject_id
    WHERE teacher_id = :teacher_id;
    '''
    result = session.query(Teacher.fullname.label('teacher_name'), func.avg(Grade.grade
                                                                            ).label('average_grade')).join(
        Subject, Teacher.id == Subject.teacher_id
    ).join(Grade, Subject.id == Grade.subject_id).filter(Teacher.id == teacher_id
                                                         ).group_by(Teacher.fullname).all()
    return result


def select_09(fullname):  # Знаходимо список курсів, які відвідує студент.
    '''
    SELECT DISTINCT subjects.name AS course_name
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON grades.subject_id = subjects.id
    WHERE fullname = :fullname;
    '''
    result = session.query(Subject.name.label('course_name')).join(Grade, Subject.id == Grade.subject_id
                                                                   ).join(Student,
                                                                          Student.id == Grade.student_id).filter(
        Student.fullname == fullname).distinct().all()
    return result


def select_10(student_fullname,
              teacher_fullname):  # Знаходимо список курсів, які певному студенту читає певний викладач.
    '''
    SELECT DISTINCT subjects.name AS course_name
    FROM students
    JOIN grades ON students.id = grades.student_id
    JOIN subjects ON subjects.id = grades.subject_id
    JOIN teachers ON subjects.teacher_id = teachers.id
    WHERE students.fullname = :students_fullname AND teachers.fullname = :teachers_fullname;
    '''
    result = session.query(Subject.name.label('course_name')).join(Grade, Subject.id == Grade.subject_id
                                                                   ).join(Student,
                                                                          Student.id == Grade.student_id).join(
        Teacher, Subject.teacher_id == Teacher.id
        ).filter(Student.fullname == student_fullname, Teacher.fullname == teacher_fullname).distinct().all()
    return result


if __name__ == '__main__':
    print(select_01())
    print(select_02())
    print(select_03(input("subject_id > ")))
    print(select_04())
    print(select_05(input("teacher_id > ")))
    print(select_06(input("group_id > ")))
    print(select_07(input("group_id > "), input("subject_id > ")))
    print(select_08(input("teacher_id > ")))
    print(select_09(input("student_fullname > ")))
    print(select_10(input("student_fullname > "), input("teacher_fullname > ")))
