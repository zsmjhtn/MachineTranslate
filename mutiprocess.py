# -*- coding:UTF-8 -*-
import os
from multiprocessing import Pool
import time
import translate
import utils


def single_process(index, target):
    print('Run process %s (%s)...' % (index, os.getpid()))
    translate.work(target,True, '子进程 %s (%s) ' % (index, os.getpid()), False)


def workPool(tasklist, processcount=4):
    p = Pool(processcount)
    time_start = time.time()
    for i, target in enumerate(tasklist):
        p.apply_async(single_process, args=(i, target, ))
    print(' Open %s processes, Waiting for all subprocesses done...' %
          processcount)
    p.close()
    p.join()
    print(' All subprocesses done!')
    print('[+]翻译总计耗时{}'.format(utils.format_time(time.time() - time_start)))
    finallist = list(map(lambda x: utils.rename(x), tasklist))
    utils.zip(finallist)
