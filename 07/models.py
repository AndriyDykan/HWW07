from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime

Base = declarative_base()


class Group(Base):
    __tablename__ = "groups"
    group_id = Column(Integer, primary_key=True)
    group_name = Column(String(25), nullable=False, unique=True)

    def __str__(self):
        return f"Group ID: {self.group_id}, Group Name: {self.group_name}"

class Student(Base):

    __tablename__ = "students"
    student_id = Column(Integer, primary_key=True)
    student_name = Column(String(25), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey(Group.group_id, ondelete="CASCADE"))

    def __repr__(self):
        return f"Student ID: {self.student_id}, Student Name: {self.student_name}"


class Subject(Base):
    __tablename__ = "subjects"
    subject_id = Column(Integer, primary_key=True)
    subject_name = Column(String(25), nullable=False, unique=True)

    def __repr__(self):
        return f"Subject ID: {self.subject_id}, Subject Name: {self.subject_name}"


class Teacher(Base):
    __tablename__ = "teachers"
    teacher_id = Column(Integer, primary_key=True)
    teacher_name = Column(String(25), nullable=False, unique=True)
    subject_id = Column(Integer, ForeignKey(Subject.subject_id, ondelete="CASCADE"))

    def __repr__(self):
        return f"Teacher ID: {self.teacher_id}, Teacher Name: {self.teacher_name}"


class Mark(Base):
    __tablename__ = "marks"
    mark_id = Column(Integer, primary_key=True)
    mark_score = Column(Integer, nullable=False)
    date = Column(DateTime())
    teacher_id = Column(Integer, ForeignKey(Teacher.teacher_id, ondelete="CASCADE"))
    subject_id = Column(Integer, ForeignKey(Teacher.subject_id, ondelete="CASCADE"))
    student_id = Column(Integer, ForeignKey(Student.student_id, ondelete="CASCADE"))

    def __repr__(self):
        return f"Mark ID: {self.mark_id}, Score: {self.mark_score}, Date: {self.date}"