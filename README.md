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

使用方式：
```dos
Win机:
python translate.py sourceFile [targetFile]
or
python translate.py sourceFile

MAC:
点开cmd，将需要翻译的英文txt，拖入到cmd里即可
```
文件默认生成在sourceFile的目录下


下一版：gui可视化待续...
-----
部分代码参考自最初作者 https://github.com/Dayunxi/googleTranslate
