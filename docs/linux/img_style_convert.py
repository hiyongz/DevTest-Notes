#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/10/1 22:26
# @Author:  hiyongz
# @File:    img_style_convert.py
import os,re
import sys
import time
import glob

def img_convert(file):

    print('\n当前文件：%s'%file)
    reg_img = r'(?<=src=\").*?(?=\")'# 图片名称
    reg_img2 = r'(?<=!\[).*?(?=\])'
    reg_img3 = r'(?<=]\().*?(?=\))'# 图片名称
    reg_img4 = r'<center><b>.*<b></center>'# 图片名称

    with open(file, 'r', encoding='utf-8') as f:
        lines = []  # 创建了一个空列表，里面没有元素
        filename = file.split("\\")[-1]
        filename = filename.split(".md")[0]
        for line in f.readlines():
            if re.search("^<img.*/>$", line):
                img_name = re.findall(reg_img, line)[0]  # 图片名称
                print(line)
                line1 = f"![]({filename}/{img_name})"
                print(line1)
                lines.append(line1)
                continue
            if re.search(reg_img2, line):
                img_name = re.findall(reg_img3, line)[0]  # 图片名称
                print(line)
                line2 = f"![]({filename}/{img_name})"
                lines.append(line2)
                print(line2)
                continue
            if re.search(reg_img4, line):
                lines.append("\n")
                continue
            lines.append(line)
        f.close()
    with open(file, 'w', encoding='utf-8') as f:
        for line in lines:
            f.write('%s' % line)
        f.close()

def headline_edit(file):
    with open(file, 'r', encoding='utf-8') as f:
        reg_title = r"(?<=title: ).*"
        title_block = []
        lines = []
        index = 0
        flag = 0
        for line in f.readlines():
            if len(title_block) == 2 and flag == 0:
                lines.append(f"# {title_name}\n")
                flag = 1
                continue
            elif flag == 1:
                lines.append(line)
                continue
            if line == '---\n':
                title_block.append(index)
            if re.search(reg_title, line):
                title_name = re.findall(reg_title, line)[0]  # 图片名称
                print(title_name)
            index += 1

        f.close()
    if len(lines) != 0:
        with open(file, 'w', encoding='utf-8') as f:
            for line in lines:
                f.write('%s' % line)
            f.close()


if __name__=='__main__':
    md_file = []
    if len(sys.argv) < 2:
        path = os.getcwd()
        md_file = glob.glob(path + "/*.md")
        print(md_file)

        if len(md_file) != 0:
            print('当前目录下的Markdown文件：')
            for file in md_file:
                print(file)
        else:
            print('该目录下无Markdown文件，即将退出...')
            time.sleep(2)
            os._exit(0)
    else:
        md_file[0] = sys.argv[1]

    for file in md_file:
        if os.path.exists(file) and os.path.isfile(file):
            img_convert(file)
            headline_edit(file)
        else:
            msg = "未找到文件"
            print(msg)
