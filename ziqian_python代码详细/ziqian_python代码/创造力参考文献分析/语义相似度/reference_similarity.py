from pytorch_pretrained_bert import BertModel, BertTokenizer
import numpy as np
import torch

model_name = 'bert-base-uncased'
# 加载bert的分词器
tokenizer = BertTokenizer.from_pretrained("E:\\down\\archive\\bert-base-uncased-vocab.txt")
# 加载bert模型，这个路径文件夹下有bert_config.json配置文件和model.bin模型权重文件
model = BertModel.from_pretrained("E:\\down\\archive\\bert-base-uncased\\bert-base-uncased")
  

#计算使用bert计算两个句子的相似度
def bert_similarity(s1, s2):
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
    #计算余弦相似度
    cos = torch.nn.CosineSimilarity(dim=0, eps=1e-6)
    similarity = cos(vec1, vec2)
    return similarity

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

#读取csv文件，title列存入列表
import pandas as pd
df = pd.read_csv("D:\\研究生-心理与行为大数据\\ziqianの创造力\\Creativity\\PDF_Text\\ICLR2022\\Spotlight Presentations\\reference\\9XhPLAjjRB.csv")
titles = df['title'].tolist()
print(titles)

#计算titles所有句子的相似度
bert_distance_list=[]
for i in range(len(titles)):
    for j in range(i+1, len(titles)):
        print(titles[i], titles[j], bert_distance(titles[i], titles[j]))
        bert_distance_list.append(bert_distance(titles[i], titles[j]))
print(bert_distance_list)
#存储相似度bert_distance_list至numpy文件
np.save("D:\\研究生-心理与行为大数据\\ziqianの创造力\\Creativity\\PDF_Text\\ICLR2022\\Spotlight Presentations\\reference_similarity\\9XhPLAjjRB.npy", bert_distance_list)
#计算tensor列表中的方差，即相似度的标准差
print(torch.std(torch.tensor(bert_distance_list)))
#计算tensor列表中的均值，即相似度的平均值
print(torch.mean(torch.tensor(bert_distance_list)))
#计算tensor中的最大值和最小值
print(torch.max(torch.tensor(bert_distance_list)))
print(torch.min(torch.tensor(bert_distance_list)))

#新建字典，存储句子和相似度
bert_distance_dict={}
for i in range(len(titles)):
    for j in range(i+1, len(titles)):
        bert_distance_dict[titles[i]+titles[j]]=bert_distance(titles[i], titles[j])
print(bert_distance_dict)


#将字典按照相似度从大到小排序
bert_distance_dict_sorted=sorted(bert_distance_dict.items(), key=lambda x: x[1], reverse=True)
print(bert_distance_dict_sorted)








