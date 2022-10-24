'''
批量读取txt文件
'''
# 使用os库
import os

def txtFilesPath(path):
    '''
    path: 目录文件夹地址
    
    返回值：列表，txt文件全路径
    '''
    filePaths = [] # 存储目录下的所有文件名，含路径
    for root,dirs,files in os.walk(path):
        for file in files:
            filePaths.append(os.path.join(root,file))
    return filePaths

# 文件所在文件夹
#filepath = r"D:\研究生-心理与行为大数据\创造力\PDF_Text\PDF_Text\ICLR2022\Oral Presentations\txt"
#txtFilesPath(filepath)




