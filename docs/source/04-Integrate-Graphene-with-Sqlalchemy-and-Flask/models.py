# -*- coding: utf-8 -*-

import sqlalchemy as sa
import sqlalchemy.orm as orm

engine = sa.create_engine("sqlite:///database.sqlite3", convert_unicode=True)
db_session = orm.scoped_session(
    orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

Base = orm.declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


class Department(Base):
    __tablename__ = "department"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)


class Employee(Base):
    __tablename__ = "employee"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    hired_on = sa.Column(sa.DateTime, default=sa.func.now())
    department_id = sa.Column(sa.Integer, sa.ForeignKey("department.id"))

    department = orm.relationship(
        Department,
        backref=orm.backref("employees", uselist=True, cascade="delete,all"),
    )
