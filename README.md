# googleTranslate

调用Google翻译， 每次翻译一行文本
结果以每段落及其对应的翻译呈现

-----

假设原文：
This phrase is meant to capture the full scope of situations in which reading literacy plays a role, from private to public, from school to work, from formal education to lifelong learning and active citizenship.“To achieve one’s goals and to develop one’s knowledge and potential” spells out the idea that reading literacy enables the fulfilment of individual aspirations – both defined ones, such as graduating or getting a job, and those less defined and less immediate that enrich

那么返回结果为:
This phrase is meant to capture the full scope of situations in which reading literacy plays a role, from private to public, from school to work, from formal education to lifelong learning and active citizenship.“To achieve one’s goals and to develop one’s knowledge and potential” spells out the idea that reading literacy enables the fulfilment of individual aspirations – both defined ones, such as graduating or getting a job, and those less defined and less immediate that enrich
这个短语是为了抓住读写能力在私人到公众，从学校到工作，从正规教育到终身学习和积极的公民身份等方面发挥作用的全部领域。 “实现自己的目标，发展自己的知识和潜力”阐明了阅读素养能够实现个人愿望的观念 - 既有定义的，如毕业或找工作，也有那些不那么明确，

-----
环境：
```dos
1.基本的python执行环境，我自己是python3.6
2.依赖包：requests，PyExecJS
```

Bugs：
```dos
1.pdf2txt的正则替换，会将连续段落整合为一大段。这是不可接受的！
2.VS Code js传参给python 会编码报错，而cmd不会。初步断定VS Code的问题。
3.无意义的table，reference，页眉页脚暂无有效手段去除。
```

2018-12-18：
```dos
1.calTKK方法失效了，更换了新的获取tkk的代码后，目前程序可以正常运行。
```



使用方式：
```dos
Win机:
python pdf2txt.py sourceFile [targetFile]
or
python pdf2txt.py sourceFile

MAC:
双击 **MachineTranslate.command** ，将需要翻译的英文txt/pdf，拖入到cmd里即可
```
文件默认生成在sourceFile的目录下

0.1：支持pdf，txt文件拖进cmd，进行机器翻译
-----
0.2：对600行以上段落的大文件进行4等分，开启4进程翻译。问题在于google会拒绝频繁访问，只能不断重试
部分代码参考自最初作者 https://github.com/Dayunxi/googleTranslate
