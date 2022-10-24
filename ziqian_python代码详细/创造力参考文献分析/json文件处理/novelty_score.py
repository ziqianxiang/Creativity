import json
#读取json文件
def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

#读取"D:\研究生-心理与行为大数据\创造力\Reviews\Reviews\ICLR2022\Spotlight Presentations\review_deal\_xwr8gOBeV1.json"
path = "D:\\研究生-心理与行为大数据\\创造力\\Reviews\\Reviews\\ICLR2022\\Spotlight Presentations\\review_deal\\_xwr8gOBeV1.json"
data = read_json(path)
#print(data)
#读取键值为“technical_novelty_and_significance”的值
novelty_score = data["Reviews"]
#print(novelty_score)
#历遍review的值
#建立两个空列表，用于存储novelty_score的值
technical_novelty_score_list = []
empirical_novelty_score_list = []
for i in novelty_score:
    #print(i)
    #读取键值为“technical_novelty_and_significance”的值
    technical_novelty_score = i["technical_novelty_and_significance"]
    #print(novelty_score)
    #使用:分割字符串
    technical_novelty_score = technical_novelty_score.split(":")[0]
    #读取键值为empirical_novelty_and_significance的值
    empirical_novelty_score = i["empirical_novelty_and_significance"]
    empirical_novelty_score = empirical_novelty_score.split(":")[0]
   
    empirical_novelty_score_list.append(empirical_novelty_score)
    technical_novelty_score_list.append(technical_novelty_score)
    
print(technical_novelty_score_list)
print(empirical_novelty_score_list)

#将list technical_novelty_score_list 和empirical_novelty_score_list写入csv
import csv
with open("D:\\研究生-心理与行为大数据\\创造力\\Reviews\\Reviews\\ICLR2022\\Spotlight Presentations\\novelty_score\\_xwr8gOBeV1.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["technical_novelty_score", "empirical_novelty_score"])
    #写入列
    for i in range(len(technical_novelty_score_list)):
        writer.writerow([technical_novelty_score_list[i], empirical_novelty_score_list[i]])
 