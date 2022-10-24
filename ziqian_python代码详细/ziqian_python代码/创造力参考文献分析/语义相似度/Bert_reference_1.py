from pytorch_pretrained_bert import BertModel, BertTokenizer
import numpy as np
import torch
import pandas as pd

model_name = 'bert-base-uncased'
# 加载bert的分词器
tokenizer = BertTokenizer.from_pretrained("E:\\down\\archive\\bert-base-uncased-vocab.txt")
# 加载bert模型，这个路径文件夹下有bert_config.json配置文件和model.bin模型权重文件
model = BertModel.from_pretrained("E:\\down\\archive\\bert-base-uncased\\bert-base-uncased")
  
#使用bert计算两个句子的欧式距离
def bert_distance(s1, s2):
    #分词
    tokens1 = tokenizer.tokenize(s1)
    tokens2 = tokenizer.tokenize(s2)
    #加入特殊字符
    tokens1 = ["[CLS]"] + tokens1 + ["[SEP]"]
    tokens2 = ["[CLS]"] + tokens2 + ["[SEP]"]
    #转换为id
    ids1 = torch.tensor([tokenizer.convert_tokens_to_ids(tokens1)])
    ids2 = torch.tensor([tokenizer.convert_tokens_to_ids(tokens2)])
    #计算句子的向量
    all_layers_all_words1, pooled1 = model(ids1, output_all_encoded_layers=True)
    all_layers_all_words2, pooled2 = model(ids2, output_all_encoded_layers=True)
    #取最后一层的[CLS]的向量
    vec1 = all_layers_all_words1[-1][0][0]
    vec2 = all_layers_all_words2[-1][0][0]
    #计算欧式距离
    distance = torch.dist(vec1, vec2, 2)
    return distance

'''
批量读取txt文件
'''
# 使用os库
import os

def csvFilesPath(path):
    '''
    path: 目录文件夹地址
    
    返回值：列表，csv文件全路径
    '''
    filePaths = [] # 存储目录下的所有文件名，含路径
    for root,dirs,files in os.walk(path):
        for file in files:
            filePaths.append(os.path.join(root,file))
    return filePaths

#将csv文件存入列表
def csvFilesList(path): 
    df = pd.read_csv(path, encoding='utf-8')
    titles = df['title'].tolist()
    return titles


#计算titles所有句子的相似度
def bert_distance_all(titles):
    '''
    titles: 列表，所有句子
    
    返回值：列表，所有句子的相似度
    '''
    distance_all = []
    for i in range(len(titles)):
        for j in range(i+1, len(titles)):
            distance = bert_distance(titles[i], titles[j])
            distance_all.append(distance)
    #计算tensor列表中的方差，即相似度的标准差
    distance_sd=torch.std(torch.tensor(distance_all))  
    #计算tensor列表中的均值，即相似度的均值
    distance_mean=torch.mean(torch.tensor(distance_all))
    #计算相似度的最大值
    distance_max=torch.max(torch.tensor(distance_all))
    #计算相似度的最小值
    distance_min=torch.min(torch.tensor(distance_all))
    return distance_all, distance_sd, distance_mean, distance_max, distance_min
import numpy
import csv
if __name__ == '__main__':
    #读取所有csv文件的路径
    path = "D:\\研究生-心理与行为大数据\\ziqianの创造力\\Creativity\\PDF_Text\ICLR2022\\Spotlight Presentations\\reference\\"
    csvFiles = csvFilesPath(path)
    #计算所有csv文件的相似度
    with open('D:\研究生-心理与行为大数据\\ziqianの创造力\\Creativity\\PDF_Text\\ICLR2022\\Spotlight Presentations\\reference_distance_result.csv', 'a', newline='') as f:
      writer = csv.writer(f)
      writer.writerow(['csvFile_name', 'distance_all', 'distance_sd', 'distance_mean', 'distance_max', 'distance_min'])
      for csvFile in csvFiles:
        titles = csvFilesList(csvFile)
        #取csvFile文件名
        csvFile_name = csvFile.split('\\')[-1]
        #去到文件名的后缀
        csvFile_name = csvFile_name.split('.')[0]
        distance_all, distance_sd, distance_mean, distance_max, distance_min = bert_distance_all(titles)
        #print(csvFile)
        print('distance_all:', distance_all)
        print('distance_sd:', distance_sd)
        print('distance_mean:', distance_mean)
        print('distance_max:', distance_max)
        print('distance_min:', distance_min)
        

       
        

        #将结果写入csv文件
        #with open('D:\研究生-心理与行为大数据\\ziqianの创造力\\Creativity\\PDF_Text\\ICLR2022\\Spotlight Presentations\\reference_distance_result.csv', 'a', newline='') as f:
            
        writer.writerow([ csvFile_name,distance_all, distance_sd, distance_mean, distance_max, distance_min])

        
#存储相似度bert_distance_list至numpy文件
#np.save("D:\\研究生-心理与行为大数据\\ziqianの创造力\\Creativity\\PDF_Text\\ICLR2022\\Spotlight Presentations\\reference_similarity\\9XhPLAjjRB.npy", bert_distance_list)
#计算tensor列表中的方差，即相似度的标准差
#print(torch.std(torch.tensor(bert_distance_list)))
#计算tensor列表中的均值，即相似度的平均值
#print(torch.mean(torch.tensor(bert_distance_list)))
#计算tensor中的最大值和最小值
#print(torch.max(torch.tensor(bert_distance_list)))
#print(torch.min(torch.tensor(bert_distance_list)))