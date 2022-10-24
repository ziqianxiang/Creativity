'''定义函数将列表中内容保存至csv文件'''
import csv
import re
import os




def listtoCsv(title_conference_year_list,filename):
    with open(filename, 'w', newline='',encoding='utf-8') as f:
        
        writer = csv.writer(f)
        writer.writerow(['title', 'year','conference'])
        for i in title_conference_year_list:
           writer.writerow([i['title'], i['year'],i['conference']])
       
    return "success: save to csv file"
    
#read_File("D:\\研究生-心理与行为大数据\\创造力\\PDF_Text\\PDF_Text\\ICLR2022\\Oral Presentations\\txt\\3wU2UX0voE.txt")
#listtoCsv(read_File("D:\\研究生-心理与行为大数据\\创造力\\PDF_Text\\PDF_Text\\ICLR2022\\Desk Rejected Withdrawn Submissions\\txt\\_qjEae4op-.txt"),"D:\\研究生-心理与行为大数据\\创造力\\PDF_Text\\PDF_Text\\ICLR2022\\Desk Rejected Withdrawn Submissions\\txt\\_qjEae4op-.csv")
