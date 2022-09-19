from argparse import ONE_OR_MORE
from asyncio.windows_events import NULL
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
#print(newreference)



'''
以‘.’分割列表中的每一条参考文献
'''

newreference2=[]
for x in newreference:
        newreference2.append(x.split('.'))#以‘.’分割列表中的每一条参考文献
#print(newreference2)

#提取每一条参考文献中的作者，论文题目，会议名称
newreference3=[]
for x in newreference2:
    listelement=[]
    if len(x)>=2:
       listelement.append(x[1])
    if len(x)>2:
        x[2].split(',')
        ref=x[2].split(',')
        listelement.append(ref[0])
    if len(listelement)==2:
        newreference3.append(listelement)
print(newreference3)
print(len(newreference3))
'''提取列表每一项的论文题目以及会议，写入csv文件'''
import csv
with open(r"reference3.csv",'w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f)
    writer.writerow(['论文题目','会议名称'])
    for x in newreference3:
        #遇到缺失值时，使用空字符串填充
        writer.writerow([x[0] if len(x)>1 else NULL,x[1] if len(x)>1 else NULL])
        #writer.writerow([x[0] , x[1]])
        




'''
提取列表中每一项中的论文题目以及会议，写入csv文件

import csv
with open(r"D:\研究生-心理与行为大数据\ziqianの创造力\ziqian_python\reference.csv",'w',newline='',encoding='utf-8') as f:
        writer=csv.writer(f)
        writer.writerow(['论文题目','会议名称'])
        for x in newreference2:
                #遇到缺失值时，使用空字符串填充
                writer.writerow([x[1] if len(x)>1 else 'null',x[2] if len(x)>2 else 'null'])

'''
