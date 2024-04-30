from sqlalchemy import func

from connect_db import session
from models import Student, Mark, Group,Subject,Teacher

# Запит для знаходження 5 студентів з найвищим середнім балом
top_students = session.query(Student).join(Mark).group_by(Student).order_by(func.avg(Mark.mark_score).desc()).limit(
    5).all()
print(top_students)
# Знайдіть студента із найвищим середнім балом з певного предмета
subject_id = 1
top_student_in_subject = session.query(Student).join(Mark).filter(Mark.subject_id == subject_id).group_by(
    Student).order_by(func.avg(Mark.mark_score).desc()).first()
print(top_student_in_subject)
# Знайдіть середній бал у групах з певного предмета

subject_id = 1
average_score_by_group = session.query(Group.group_name, func.avg(Mark.mark_score).label('average_score')).\
    select_from(Group).join(Student).join(Mark, Student.student_id == Mark.student_id).\
    filter(Mark.subject_id == subject_id).\
    group_by(Group.group_name).all()
print(average_score_by_group)
# Знайдіть середній бал на потоці
average_score_overall = session.query(func.avg(Mark.mark_score)).scalar()
print(average_score_overall)
#Знайдіть, які курси читає певний викладач

teacher_id = 1
subject_id = session.query(Teacher.subject_id).filter(Teacher.teacher_id == teacher_id).scalar()
subject_name = session.query(Subject.subject_name).filter(Subject.subject_id == subject_id).scalar()
print(subject_name)

#Знайдіть список студентів у певній групі
group_id = 1
students_in_group = session.query(Student).filter(Student.group_id == group_id).all()
print(students_in_group)
#Знайдіть оцінки студентів в окремій групі з певного предмета
group_id = 1
subject_id = 1
grades_in_group_and_subject = session.query(Mark).join(Student).filter(Student.group_id == group_id, Mark.subject_id == subject_id).all()
print(grades_in_group_and_subject)
# Знайдіть середній бал, який ставить певний викладач зі своїх предметів
teacher_id = 1
average_score_given_by_teacher = session.query(func.avg(Mark.mark_score))\
    .join(Teacher, Mark.subject_id == Teacher.subject_id)\
    .filter(Teacher.teacher_id == teacher_id)\
    .scalar()
print(average_score_given_by_teacher)

# Знайдіть список курсів, які відвідує певний студент
student_id = 16
courses_attended_by_student = session.query(Subject.subject_name)\
    .join(Mark, Mark.subject_id == Subject.subject_id)\
    .filter(Mark.student_id == student_id)\
    .distinct()\
    .all()
print(courses_attended_by_student)

# Список курсів, які певному студенту читає певний викладач
teacher_id = 4
student_id = 16
courses_taught_to_student_by_teacher = session.query(Subject.subject_name)\
    .join(Mark, Mark.subject_id == Subject.subject_id)\
    .join(Teacher, Mark.subject_id == Teacher.subject_id)\
    .filter(Mark.student_id == student_id, Teacher.teacher_id == teacher_id)\
    .distinct()\
    .all()
print(courses_taught_to_student_by_teacher)