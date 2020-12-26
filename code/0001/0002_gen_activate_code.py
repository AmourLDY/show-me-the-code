# coding: utf-8

"""
@file: 0002_gen_activate_code.py
@time: 2020/12/26 18:17
"""
import base64


def gen_code(code: str, gen_num):
    for num in range(gen_num):
        yield base64.b64encode(f"{code}_{num}".encode('utf-8'))


def parse_code(gen_code_lst):
    for base64_code in gen_code_lst:
        result = base64.b64decode(base64_code).decode('utf-8')
        print(f"加密数据{base64_code}, 解密数据{result}")
        yield base64_code, result


def main():
    gen_code_lst = gen_code('id', 200)
    return parse_code(gen_code_lst)


if __name__ == '__main__':
    main()

