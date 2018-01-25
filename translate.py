# -*- coding:UTF-8 -*-
import requests
import execjs
import json
import sys
import os
import time
import utils
from CalcTk import CalcTk

headers = {
    'Host': 'translate.google.cn',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'Referer': 'https://translate.google.cn/',
    'Cookie': 'NID=101=pkAnwSBvDm2ACj2lEVnWO7YEPUoWCTges7B7z2jJNyrNwAZ2OL9FFOQLpdethA_20gCVqukiHnVm1hUbMGZc_ItQFdP5AHoq5XoMeEORaeidU196NDVRsrAu_zT0Yfsd; _ga=GA1.3.1338395464.1492313906',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0'
}

params = {
    'client': 't', 'sl': 'en', 'tl': 'zh-CN', 'hl': 'zh-CN',
    'dt': 'at', 'dt': 'bd', 'dt': 'ex', 'dt': 'ld', 'dt': 'md',
    'dt': 'qca', 'dt': 'rw', 'dt': 'rm', 'dt': 'ss', 'dt': 't',
    'ie': 'UTF-8', 'oe': 'UTF-8', 'source': 'bh', 'ssel': '0',
    'tsel': '0', 'kc': '1', 'tk': '376032.257956'
}

TK = CalcTk()


def get_res(url, data, params):
    try:
        res = requests.post(url, headers=headers, data=data,
                            params=params, timeout=2)
        res.raise_for_status()
        return res
    except Exception as ex:
        print('[-]ERROR: ' + str(ex))
        return res


def parse_json(res):
    return json.loads(res)


def translate(text):
    global params, TK
    url = 'https://translate.google.cn/translate_a/single'
    data = {'q': text}
    try:
        params['tk'] = TK.get_tk(text)
        res = get_res(url, data, params)
        ret_list = parse_json(res.text)
        return ret_list[0]
    except Exception as ex:
        print('[-]ERROR: ' + str(ex))
        return None


def work(source, deleteTemp=False, pid=None, closemutiprocess=True):
    lines = []
    target = ''
    p, f = os.path.split(source)
    target = p + '//T_' + f

    lines = utils.totalLines(source)
    total_lines = len(lines)
    if total_lines == 0:
        return

    for i in range(total_lines):
        lines[i] = lines[i].strip('\n')
        if not lines[i]:
            total_lines -= 1
    print('[+]共{}段'.format(total_lines)
          if closemutiprocess else '[+]{} 共{}段'.format(pid, total_lines))

    i = 0
    err_times = 0
    en_str_list = []  # google翻译段落是返回分句的list，这里整合一下
    cn_str_list = []
    count = 1  # 记录当前翻译段数
    chinese = open(target, 'wt', encoding='utf-8')
    chinese.truncate()
    time_start = time.time()
    while i < len(lines):
        line = lines[i]
        if not line:
            chinese.write('\n')
            i += 1
            continue
        if closemutiprocess:
            print('[+]正在翻译第{}段 ...已耗时{}'.format(count,
                                                utils.format_time(time.time() - time_start)))
        try:
            ret = translate(line)
            if not ret:
                raise Exception('Empty Response')
            for item in ret:
                en_str_list.append(item[1])
                cn_str_list.append(item[0])
            chinese.write('{}\n{}\n'.format(
                ''.join(en_str_list), ''.join(cn_str_list)))
            chinese.write('\n')  # 每段间隔一行
            en_str_list.clear()
            cn_str_list.clear()
            i += 1
            count += 1
            err_times = 0
        except Exception as ex:
            print('[-]ERROR: ' + str(ex))
            print('对geoogle翻译请求太过频繁，休息30秒, 30秒之后继续请求')
            time.sleep(15)
            err_times += 1
            if(err_times > 10):  # 连续十次未获取成功就令URL为None，并跳过
                print('[-]跳过')
                chinese.write('\n缺\n')
                i += 1
                count += 1
    chinese.close()
    print('[+]翻译完成' if closemutiprocess else '[+]{} 翻译完成'.format(pid))
    if deleteTemp:
        os.remove(source)
        print('[+]{} 文件已删除'.format(source))
    print('总计耗时{}'.format(utils.format_time(time.time() - time_start))
          if closemutiprocess else '[+]{} 总计耗时{}'.format(pid, utils.format_time(time.time() - time_start)))
