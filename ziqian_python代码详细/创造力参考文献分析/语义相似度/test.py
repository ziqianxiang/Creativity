from pytorch_pretrained_bert import BertModel, BertTokenizer
import numpy as np
import torch

model_name = 'bert-base-uncased'
# 加载bert的分词器
tokenizer = BertTokenizer.from_pretrained("E:\\down\\archive\\bert-base-uncased-vocab.txt")
# 加载bert模型，这个路径文件夹下有bert_config.json配置文件和model.bin模型权重文件
model = BertModel.from_pretrained("E:\\down\\archive\\bert-base-uncased\\bert-base-uncased")

s = "The first step is as good as half over"
tokens = tokenizer.tokenize(s)
print(tokens)

tokens = ["[CLS]"] + tokens + ["[SEP]"]
print(tokens)

ids = torch.tensor([tokenizer.convert_tokens_to_ids(tokens)])   #注意此处的[]
print(ids)

all_layers_all_words, pooled = model(ids, output_all_encoded_layers=True)
print(len(all_layers_all_words))


