import datetime
import random

from faker import Faker

from connect_db import session
from models import Student, Group, Subject, Teacher, Mark

GROUPS = ['MTP11', 'MTP12', 'MTP13', 'MTP14', 'MTP15', 'MTP16']
TEACHERS = [Faker().name() for i in range(11)]
SUBJECTS = ['math', 'art', 'science', 'history', 'music', 'geography', 'P.E (Physical Education)', 'drama']

if __name__ == '__main__':
    for group in GROUPS:
        gr = Group(group_name=group)
        session.add(gr)

    for _ in range(40):
        st = Student(student_name=Faker().name(), group_id=random.randint(1, 6))
        session.add(st)

    for subject in SUBJECTS:
        sb = Subject(subject_name=subject)
        session.add(sb)

    for teacher in TEACHERS:
        tr = Teacher(teacher_name=teacher, subject_id=random.randint(1, 8))
        session.add(tr)

    for _ in range(40):
        mr = Mark(mark_score=random.randint(1, 12), date=datetime.datetime.now(),
                  subject_id=random.randint(1, 8),student_id= random.randint(1,39))
        session.add(mr)

    session.commit()
