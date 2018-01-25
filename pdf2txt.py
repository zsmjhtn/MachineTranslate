# -*- coding:UTF-8 -*-
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from io import StringIO
from io import open
import sys
import os
import paragraphFormat
import translate
import utils
import mutiprocess


def readPDF(pdfFile):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)

    process_pdf(rsrcmgr, device, pdfFile)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


def main():
    pdf_src = ''
    target = ''
    deleteTemp = False
    if len(sys.argv) == 3:
        pdf_src = sys.argv[1]
        target = sys.argv[2]
    elif len(sys.argv) == 2:
        pdf_src = sys.argv[1]
        p, f = os.path.split(pdf_src)
        filename, extension = os.path.splitext(f)
        target = p + '//pdf2txt_' + filename + '.txt'
    else:
        pdf_src = input(
            "请 copy 待翻译的文件的地址(后缀名要带上 like：C://xx/xx/xx.txt  or  X://xx/xx/xx.pdf):")
        p, f = os.path.split(pdf_src)
        filename, extension = os.path.splitext(f)
        target = p + '//pdf2txt_' + filename + '.txt'
        # print('[-]ERROR: \nUsage: You can only pull one file into...')
        # return

    if extension == '.pdf':
        deleteTemp = True
        target = p + '//pdf2txt_' + filename + '.txt'
        print('开始 pdf => txt , 请稍等...')
        pdfFile = open(pdf_src, 'rb')
        outputString = readPDF(pdfFile)
        pdfFile.close()
        print('pdf => txt 完成\n正在对txt文件进行格式化...')
        paragraphFormat.paragraph_format(outputString, target)
        print('txt文件格式化完成，文件放在您的同目录下: pdf2txt_xxx.txt')
    elif extension == '.txt':
        target = pdf_src
    else:
        print('[-]ERROR: \n sourceFile is  neither  pdf  nor  txt')
        return

    # 600行以上启用多线程

    linecount = len(utils.totalLines(target))
    if linecount == 0:
        return
    elif linecount > 600:
        split_list = utils.split(target, linecount // 4 + 1)
        mutiprocess.workPool(split_list)
        utils.delete(split_list)
    else:
        translate.work(target, deleteTemp)


if __name__ == '__main__':
    main()
