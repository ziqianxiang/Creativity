from argparse import ONE_OR_MORE
from asyncio.windows_events import NULL
from lib2to3.pgen2.token import TILDE
from logging.handlers import TimedRotatingFileHandler
import os
import re
from turtle import title
'''提取文档"D:\研究生-心理与行为大数据\ziqianの创造力\ziqian_python\_CfpJazzXT2.txt"中Reference和Appendix之间的文本'''


'''
以‘.’分割列表中的每一条参考文献,名字bug
以第一个前一个字符不是大写字母的句号对句子进行分割
'''
def filter_ref_name(string):
    
        names = re.search(r'.*?[^A-Z]\.', string).group(0)
    
        #return names.rstrip('.').split(',')
        return names

# 读取文档
with open(r"D:\研究生-心理与行为大数据\创造力\PDF_Text\PDF_Text\ICLR2022\Desk Rejected Withdrawn Submissions\txt\5alVAdi6wW4.txt",encoding='UTF-8') as f:
  
        content = f.read()
        start_index = content.rfind("References")#查找最后一次出现的Reference
        #end_index = content.rfind("Appendix")#查找最后一次出现的Appendix
        end_index=-1
        print(start_index)
        print(end_index)
        s=content[start_index:end_index]
        #print(s)
        #re.split('\d\n,',s)
        #print(re.split('.\n',s))
        reference=re.split('\d\n',s)
        referencelist=[]    #存储处理后的参考文献
        for i in reference:
            referencelist.append(i.replace("\n", ""))  #去除每一条参考文献中的换行符
        #print(referencelist)
        filter_reference_list=[]
        #删除文献中的作者，有.,影响后续的分割
        for i in referencelist:
            if i.find('.')!=-1:
                name=filter_ref_name(i)
                filter_reference=i.split(name) #以name分割论文题目和会议名称
                filter_reference_list.append(filter_reference)
                print(filter_reference)
        #提取filter_reference中的title和conference,year
        title_conference_year_list=[]  
       
       
        for i in filter_reference_list:
             #建立一个空字典，用于存储title和conference以及对应的年份
               title_conference_year_dict={}
               title=i[1].split('.')[0] #提取title
               #print(re.split(',',i[1]))
               title_confernce=(re.split(',',i[1]))[0]
               #提取conference
               new_title_conference=title_confernce.split('.')
               if len(new_title_conference)<2:
                    conference=NULL
               else:
                    conference=new_title_conference[1]
                #提取year
               year=re.findall("\ \d\d\d\d\w\.|\ \d\d\d\d\.",i[1])
               newyear=re.findall("\d\d\d\d",str(year))
               #将title和conference以及对应的year存入字典
               title_conference_year_dict['title']=title
               if len(newyear)==0:
                    title_conference_year_dict['year']=NULL
               else:
                    title_conference_year_dict['year']=newyear[0]
             
               title_conference_year_dict['conference']=conference
               title_conference_year_list.append(title_conference_year_dict)
               print(title_conference_year_dict)
               
'''
将列表中的字典写入csv文件
'''
import csv
with open(r"D:\研究生-心理与行为大数据\创造力\PDF_Text\PDF_Text\ICLR2022\Desk Rejected Withdrawn Submissions\txt\5alVAdi6wW4.csv", 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['title', 'year','conference'])
    for i in title_conference_year_list:
        writer.writerow([i['title'], i['year'],i['conference']])



