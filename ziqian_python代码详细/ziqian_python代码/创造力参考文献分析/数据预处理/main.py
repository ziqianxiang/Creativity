from split_txt_Reference import read_File
from reflist_to_csv import listtoCsv
from ReadingfilePath import txtFilesPath

#read_File("D:\\研究生-心理与行为大数据\\创造力\\PDF_Text\\PDF_Text\\ICLR2022\\Oral Presentations\\txt\\0EXmFzUn5I.txt")
#listtoCsv(read_File("D:\\研究生-心理与行为大数据\\创造力\\PDF_Text\\PDF_Text\\ICLR2022\\Oral Presentations\\txt\\0EXmFzUn5I.txt"),"D:\\研究生-心理与行为大数据\\创造力\\PDF_Text\\PDF_Text\\ICLR2022\\Oral Presentations\\txt\\0EXmFzUn5I.csv")


'''批量读取"D:\研究生-心理与行为大数据\创造力\PDF_Text\PDF_Text\ICLR2022\Oral Presentations\txt"文件夹下的txt文件，将txt文件中的参考文献列表保存至csv文件'''
# 读取txt文件夹下的所有txt文件
txtFilePath = txtFilesPath("D:\\研究生-心理与行为大数据\\创造力\\PDF_Text\\PDF_Text\\ICLR2022\\Spotlight Presentations\\txt")
# 读取txt文件夹下的所有txt文件
for txtFile in txtFilePath:
    listtoCsv(read_File(txtFile),txtFile.replace(".txt",".csv"))
