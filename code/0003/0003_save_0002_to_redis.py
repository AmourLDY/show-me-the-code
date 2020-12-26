# coding: utf-8

"""
@file: 0003_add_0002_redis.py
@time: 2020/12/26 19:15
"""
import base64

import redis


def gen_code(code: str, gen_num):
    for num in range(gen_num):
        yield base64.b64encode(f"{code}_{num}".encode('utf-8'))


def parse_code(gen_code_lst):
    for base64_code in gen_code_lst:
        result = base64.b64decode(base64_code).decode('utf-8')
        print(f"加密数据{base64_code}, 解密数据{result}")
        yield base64_code, result


def make_redis_session():
    return redis.Redis()


def main():
    session = make_redis_session()
    for key, value in parse_code(gen_code('id', 200)):
        session.set(key, value)


if __name__ == '__main__':
    main()
