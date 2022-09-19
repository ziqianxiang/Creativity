from argparse import ONE_OR_MORE
import os
import re
'''提取文档"D:\研究生-心理与行为大数据\ziqianの创造力\ziqian_python\_CfpJazzXT2.txt"中Reference和Appendix之间的文本'''
# 读取文档
with open(r"D:\研究生-心理与行为大数据\ziqianの创造力\ziqian_python\_CfpJazzXT2.txt",encoding='UTF-8') as f:
  
        content = f.read()
        start_index = content.rfind("Reference")#查找最后一次出现的Reference
        end_index = content.rfind("Appendix")#查找最后一次出现的Appendix
        print(start_index)
        print(end_index)
        s=content[start_index:end_index]
        #去除参考文献中的多余空格，仅保留一个
       # newtext=' '.join(Referencetext.split())
        #print(newtext)
        #去除文本中的换行符
        #正则表达式\n分割参考文献txt
        #re.split(', \d\d\d\d.|, \d\d\d\d\w.',s)
        #re.split(', \d\d\d\d.',s)
        #re.split(', \d\d\d\d.|, \d\d\d\d\w.',s)
        #newref=re.split(', \d\d\d\d.|, \d\d\d\d\w.',s)
        #print(re.split(', \d\d\d\d.\n|, \d\d\d\d\w.\n|,\n\d\d\d\d.\n|. \d\d\d\d\w.\n',s))
        newref=re.split(', \d\d\d\d.\n|, \d\d\d\d\w.\n|,\n\d\d\d\d.\n|. \d\d\d\d\w.\n',s)
        print(newref[1])
        oneref=re.split('\.',newref[1])
        print(oneref)
#使用正则表达式分离每一条参考文献，数据仍旧存在一些噪音，之后查阅如何存储，以字典形式。(作者；论文题目；会议名称，年份（年份以及被抹去hh）)
'''处理文本中的换行符
newrel,列表形式存储，为提出出来的参考文献，每一条参考文献为一个元素，包括作者，论文题目，会议名称
'''
newreference=[]    #存储处理后的参考文献
for x in newref:
   newreference.append(x.replace("\n", ""))
print(newreference)

'''
建立csv文件，一列为论文题目，一列为发表会议
newrel为提出出来的参考文
'''