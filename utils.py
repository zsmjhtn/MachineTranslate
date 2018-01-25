# -*- coding:UTF-8 -*-
import os
import time
import math


def zip(arraylist):
    p, f = os.path.split(arraylist[0])
    finalname = os.path.splitext(f)[0].split('_')[2]
    target = p + '//谷歌翻译_' + finalname + '.txt'
    finalfile = open(target, 'w+', encoding='utf-8')
    for block in arraylist:
        for line in open(block):
            finalfile.writelines(line)
        finalfile.write('\n')
    finalfile.close()


def delete(arraylist):
    for block in arraylist:
        os.remove(block)


def totalLines(source):
    lines = []
    try:
        stream = open(source, 'rt', encoding='utf-8')
        lines = stream.readlines()
        stream.close()
        return lines
    except Exception as ex:
        print('[-]ERROR: ' + str(ex))
        return lines


def split(source, limit = 200):
    p, f = os.path.split(source)
    filename = os.path.splitext(f)[0]
    line_list = []
    split_list = []  # split文件 uri list
    for index, line in enumerate(open(source, 'rt', encoding='utf-8'), 1):
        line_list.append(line)
        if index % limit == 0:
            target = (p + '//block%d_' + filename + '.txt') % (index / limit)
            split_list.append(target)
            with open(target, 'w+', encoding='utf-8') as tmp:
                tmp.write(''.join(line_list))
            line_list = []
        else:
            continue
    target = p + '//blockN_' + filename + '.txt'
    split_list.append(target)
    with open(target, 'w+', encoding='utf-8') as tmp:
        tmp.write(''.join(line_list))

    return split_list


def rename(source):
    p, f = os.path.split(source)
    return p + '//T_' + f


def format_time(time_process, fixed=2):
    processTime = round(time_process, fixed)
    day = 24 * 60 * 60
    hour = 60 * 60
    min = 60
    if processTime < 60:
        return "%.2f s" % processTime
    elif processTime > day:
        days = divmod(processTime, day)
        return "%d d, %s" % (int(days[0]), format_time(days[1]))
    elif processTime > hour:
        hours = divmod(processTime, hour)
        return '%d h, %s' % (int(hours[0]), format_time(hours[1]))
    else:
        mins = divmod(processTime, min)
        return "%d m, %.2f s" % (int(mins[0]), mins[1])
