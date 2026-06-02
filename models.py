from datetime import datetime
from sqlalchemy import create_engine,Column
from sqlalchemy import Integer,Text,Date,VARCHAR,SmallInteger,Boolean,ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker,relationship

engine = create_engine("sqlite:///learning.db",echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

import utils as ut

class User(Base):
    __tablename__ = "users"
    id = Column(Integer,primary_key=True,autoincrement=True)
    vk_id,ip_id = Column(Integer),Column(Integer)
    first_name,last_name = Column(VARCHAR(30),nullable=False),Column(VARCHAR(30),nullable=False)
    email = Column(VARCHAR(30),nullable=False,unique=True)
    user_class = Column(SmallInteger,default=11,name="class")
    physic,math = Column(Boolean,default=False),Column(Boolean,default=False)
    created_at = Column(Date,default=datetime.utcnow)
    result = relationship("Results",back_populates="student")
    columns = ("id","vk_id","ip_id","first_name","last_name","email","class","physic","math","created_at")

    def __repr__(self):
        return f"Ученик {self.last_name.title()} {self.first_name.title()}, \
{self.user_class} {ut.print_class(self.user_class)}. \
Физика - {self.physic}, Математика - {self.math}. email - {self.email}"

    def __iter__(self):
        for i in self.__dict__:
            if i in User.columns: yield i,self.__dict__[i]
    def dct(self): return {i[0]:i[1] for i in self}

    def get_id(self): return (self.vk_id, self.ip_id)

    @classmethod
    def add_user(cls,**kwargs):
        with Session() as session:
            if all(i in kwargs for i in ("first_name","last_name","email")):
                user = cls(**kwargs)
                session.add(user)
            else: raise ValueError("not all arguments to add new user")
            session.commit()

    @classmethod
    def select_user(cls,idscond:tuple=tuple()):
        with Session() as session:
            lenght = len(idscond)
            if lenght == 0: return session.query(cls).all()
            if lenght == 1 and type(idscond[0])==int: return session.query(cls).get(idscond[0])
            if all(type(i)==int for i in idscond):
                return session.query(cls).filter(" AND ".join(f"id == {i}" for i in idscond)).all()
            if all(type(i)==str for i in idscond):
                return session.query(cls).filter(" AND ".join(i for i in idscond)).all()
            raise ValueError("all elements of idscond must be of the same type ('str' or 'int')")


class Study(Base):
    __tablename__ = "study"
    id = Column(Integer,primary_key=True,autoincrement=True)
    math = Column(Boolean,default=1)
    theme = Column(VARCHAR(30),nullable=False)
    index = Column(Integer,default=0)
    exersize,answer = Column(Text,nullable=False),Column(Text,nullable=False)
    study_class = Column(SmallInteger,default=11,name="class")
    result = relationship("Results",back_populates="exersize")
    columns = ("id","math","theme","index","exersize","answer","class")

    def __repr__(self)->str:
        return f"{self.exersize}. Ответ - {self.answer}. \
Для {self.study_class}-го {ut.print_class(self.study_class)}а. По {'математике' if self.math else 'физике'}."
    
    def __iter__(self):
        for i in self.__dict__:
            if i in Study.columns: yield i,self.__dict__[i]
    def dct(self): return {i[0]:i[1] for i in self}

    @classmethod
    def add_exersize(cls,**kwargs):
        with Session() as session:
            if all(i in kwargs for i in ("exersize","answer","theme")):
                exersize = cls(**kwargs)
                session.add(exersize)
            else: raise ValueError("not all arguments to add new user")
            session.commit()
    select_exersize = User.select_user


class Results(Base):
    __tablename__ = "results"
    id = Column(Integer,primary_key=True,autoincrement=True)
    user_id = Column(Integer,ForeignKey("users.id"))
    student = relationship("User",back_populates="result")
    exersize_id = Column(Integer,ForeignKey("study.id"))
    exersize = relationship("Study",back_populates="result")
    variant = Column(Integer,nullable=False)
    ball = Column(SmallInteger,default=-1)

    def __repr__(self):
        return f"Это вариант ученика {str(User.select_user((self.user_id,)))}. \
Задание {str(Study.select_exersize((self.exersize_id,)))}."
    
    def add_test(cls,**kwargs):
        with Session() as session:
            if all(i in kwargs for i in ("user_id","exersize_id","variant")):
                user = cls(**kwargs)
                session.add(user)
            else: raise ValueError("not all arguments to add new user")
            session.commit()

    select_test = User.select_user


Base.metadata.create_all(engine)
        