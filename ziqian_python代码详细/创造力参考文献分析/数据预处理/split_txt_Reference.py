from argparse import ONE_OR_MORE
from asyncio.windows_events import NULL
import os
import re
'''提取文档"D:\研究生-心理与行为大数据\ziqianの创造力\ziqian_python\_CfpJazzXT2.txt"中Reference和Appendix之间的文本'''
# 读取文档函数def read_file(file_path):
def read_File(file_path):
    with open(file_path, 'r',encoding='UTF-8') as f:
        content = f.read()
        start_index = content.rfind("References")
        
        #查找最后一次出现的Reference
        end_index = content.rfind("Appendix")
        
            
        #查找最后一次出现的Appendix
        s=content[start_index:end_index]
        newref=re.split(', \d\d\d\d.\n|, \d\d\d\d\w.\n|,\n\d\d\d\d.\n|. \d\d\d\d\w.\n|\d\d\d\d. \n|\d\d\d\d.\n|\d.\n|\.\n',s)
        #newref=re.split('\d\n|\d\d\n',s)
        #newref=re.split('\n',s)
        newreference=[]    #存储处理后的参考文献
        for x in newref:
            newreference.append(x.replace("\n", ""))
        newreference2=[]
        for x in newreference:
            newreference2.append(x.split('.'))#以‘.’分割列表中的每一条参考文献
        #这里有bug，如果作者名字中有‘.’，会被分割，需要改进

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
    return newreference3  #列表


#read_file("D:\\研究生-心理与行为大数据\\创造力\\PDF_Text\\PDF_Text\\ICLR2022\\Oral Presentations\\txt\\3wU2UX0voE.txt")
#print(read_file("D:\\研究生-心理与行为大数据\\创造力\\PDF_Text\\PDF_Text\\ICLR2022\\Oral Presentations\\txt\\0EXmFzUn5I.txt"))
