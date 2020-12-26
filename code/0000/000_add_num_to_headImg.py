# coding: utf-8

"""
@file: 000_add_num_to_headImg.py
@time: 2020/12/26 17:39
"""

from PIL import Image, ImageFont, ImageDraw


def add_num_to_img():
    src_img = Image.open('./head_img.png', mode='r')
    width, height = src_img.size
    font = ImageFont.truetype(font='Arimo for Powerline.ttf')  # 字体文件 源码里面有写具体目录在哪 不同平台不一样
    draw = ImageDraw.Draw(src_img)
    draw.text((4 * width / 5, height / 5), '4', fill=(255, 10, 10), font=font)
    dst_img_name = 'dst_img.png'
    src_img.save(dst_img_name, 'png')
    dst_img = Image.open(dst_img_name)
    dst_img.show()


if __name__ == '__main__':
    add_num_to_img()
