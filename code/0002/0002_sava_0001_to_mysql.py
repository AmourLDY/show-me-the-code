# coding: utf-8

"""
@file: 0002_sava_0001_to_mysql.py
@time: 2020/12/26 18:40
"""

import base64

from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


def gen_code(code: str, gen_num):
    for num in range(gen_num):
        yield base64.b64encode(f"{code}_{num}".encode('utf-8'))


def parse_code(gen_code_lst):
    for base64_code in gen_code_lst:
        result = base64.b64decode(base64_code).decode('utf-8')
        print(f"加密数据{base64_code}, 解密数据{result}")
        yield base64_code, result


def init_database_and_table(engine, Base):
    if not database_exists(engine.url):
        create_database(engine.url)
    Base.metadata.create_all(engine)


class Cupon(Base):
    __tablename__ = 'cupon'

    id = Column('id', Integer, primary_key=True)
    cupon_key = Column('cupon_key', String(50))
    cupon_value = Column('cupon_value', String(50))


def main():
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/host')
    # 创建数据库和表
    init_database_and_table(engine, Base)
    session = sessionmaker(bind=engine)()
    for key, value in parse_code(gen_code('id', 200)):
        session.add(Cupon(cupon_key=key, cupon_value=value))
    session.commit()


if __name__ == '__main__':
    main()
