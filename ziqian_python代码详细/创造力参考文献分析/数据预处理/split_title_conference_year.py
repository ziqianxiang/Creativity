from argparse import ONE_OR_MORE
from asyncio.windows_events import NULL
import os
import re

'''
以‘.’分割列表中的每一条参考文献,名字bug
以第一个前一个字符不是大写字母的句号对句子进行分割
'''
def filter_ref_name(string):
    
        names = re.search(r'.*?[^A-Z]\.', string).group(0)
    
        #return names.rstrip('.').split(',')
        return names

'''
读取txt文档，提取参考文献，将其分割为title,conference,year
'''
def txt_to_title_conference_year(txt_path):
     with open(txt_path, 'r',encoding='UTF-8') as f:
        content = f.read()
        start_index = content.rfind("References")
        end_index = content.rfind("Appendix")#查找最后一次出现的Appendix
        #如果不存在Appendix，将end_index设为-1
        if end_index==-1:
            end_index=-1
        #print(start_index)
        #print(end_index)
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
            
        #使用try，group报错
          try:
               name=filter_ref_name(i)
               filter_reference=i.split(name) #以name分割论文题目和会议名称
               filter_reference_list.append(filter_reference)
          except AttributeError:
               print("请检查正则表达式标签是否对应")
                    #name=filter_ref_name(i)
                #filter_reference=i.split(name) #以name分割论文题目和会议名称
               #filter_reference_list.append(filter_reference)
                #print(filter_reference)
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
               #print(title_conference_year_dict)
        return title_conference_year_list
