#!/usr/bin/python
# -*- coding: UTF-8 -*-
import re
import os
from jsReg import jsReg


# 非正常段落的正则替换，解决pdf2txt的格式问题

# before:

# Item scoring

# Although most of the items are dichotomously scored (that is, responses are awarded either credit or no credit), the open
# constructed-response items can sometimes involve partial credit scoring, which allows responses to be assigned credit
# according to differing degrees of “correctness” of responses. For each such item, a detailed coding guide that allows
# for full credit, partial credit or no credit is provided to persons trained in the coding of student responses across the
# range of participating countries to ensure coding of responses is done in a consistent and reliable way. To maximise the
# comparability between the paper-based and computer-based assessments, careful attention is given to the scoring guides
# in order to ensure that the important elements are included.

# after:
# Item scoring

# Although most of the items are dichotomously scored (that is, responses are awarded either credit or no credit), the open constructed-response items can sometimes involve partial credit scoring, which allows responses to be assigned credit according to differing degrees of “correctness” of responses. For each such item, a detailed coding guide that allows for full credit, partial credit or no credit is provided to persons trained in the coding of student responses across the range of participating countries to ensure coding of responses is done in a consistent and reliable way. To maximise the comparability between the paper-based and computer-based assessments, careful attention is given to the scoring guides in order to ensure that the important elements are included.

def paragraph_format(src, dst):
    input_file = ''
    if os.path.isfile(src):
        source = open(src, 'r', encoding='UTF-8')
        out_file = source.read()
        source.close()
        input_file = jsReg().get_reg_text(out_file)
    else:
        input_file = jsReg().get_reg_text(src)

    dst_file = open(dst, "wt", encoding='utf-8')
    dst_file.write(input_file)
    dst_file.close()
