'''
Extract text content between two keywords in local text
'''
import os
def extract_text(filename, start, end):
    with open(filename, 'r',encoding='UTF-8') as f:
        content = f.read()
        start_index = content.find(start)
        end_index = content.find(end)
        return content[start_index:end_index]


file="D:\\研究生-心理与行为大数据\\ziqianの创造力\\ziqian_python\\_CfpJazzXT2.txt"
start='Published as a conference paper at ICLR 2022\nReferences'
end='Appendix'

print(extract_text(file,start,end))





   