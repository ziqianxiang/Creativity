import json
import os
import csv
#读取json文件
def read_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

#批量读取json文件
def read_jsons(path):
    import os
    files = os.listdir(path)
    #print(files)
    with open("D:\\研究生-心理与行为大数据\\创造力\\Reviews\\Reviews\\ICLR2022\\Desk Rejected Withdrawn Submissions\\novelty_score\\Desk_noveltyscore.csv", "w", newline="") as f:
      writer = csv.writer(f)
      writer.writerow(["file", "technical_novelty_score_mean", "empirical_novelty_score_mean", "correctness_score_mean", "recommendation_score_mean", "confidence_score_mean"])
      for file in files:
        if not os.path.isdir(file):
            #print(file)
            #读取json文件
            data = read_json(path + "\\" + file)
            #print(data)
            #读取键值为“technical_novelty_and_significance”的值
            novelty_score = data["Reviews"]
            #print(novelty_score)
            #历遍review的值
            #建立两个空列表，用于存储novelty_score的值
            technical_novelty_score_list = []
            empirical_novelty_score_list = []
            #新建空列表，用于存储correctness_socre`s value
            correctness_score_list = []
            #新建空列表，用于存储recommendation_score`s value
            recommendation_score_list = []
            #新建空列表，用于存储confidence_score`s value
            confidence_score_list = []
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
                #读取键值为correctness的值
                correctness_score = i["correctness"]
                correctness_score = correctness_score.split(":")[0]
                #读取键值为recommendation的值
                recommendation_score = i["recommendation"]
                recommendation_score = recommendation_score.split(":")[0]
                #读取键值为confidence的值
                confidence_score = i["confidence"]
                confidence_score = confidence_score.split(":")[0]
                #如果值为数字，则将其添加到列表中
                if technical_novelty_score.isdigit():
                    technical_novelty_score_list.append(technical_novelty_score)
                if empirical_novelty_score.isdigit():
                    empirical_novelty_score_list.append(empirical_novelty_score)
                if correctness_score.isdigit():
                    correctness_score_list.append(correctness_score)
               
                if recommendation_score.isdigit():
                    recommendation_score_list.append(recommendation_score)
                if confidence_score.isdigit():
                    confidence_score_list.append(confidence_score)
                
            #计算novelty_score的平均值
            #去除列表中的非数字元素
            
            technical_novelty_score_list = [float(i) for i in technical_novelty_score_list ] 
            empirical_novelty_score_list = [float(i) for i in empirical_novelty_score_list ]
            correctness_score_list = [float(i) for i in correctness_score_list ]
            recommendation_score_list = [float(i) for i in recommendation_score_list ]
            confidence_score_list = [float(i) for i in confidence_score_list ]
            #计算平均值

            if len(technical_novelty_score_list) != 0:
                technical_novelty_score_mean = sum(technical_novelty_score_list)/len(technical_novelty_score_list)
                #保留四位小数
                technical_novelty_score_mean = round(technical_novelty_score_mean, 4)
            else:
                technical_novelty_score_mean = "Null"
            if len(empirical_novelty_score_list) != 0:
                empirical_novelty_score_mean = sum(empirical_novelty_score_list)/len(empirical_novelty_score_list)
                empirical_novelty_score_mean = round(empirical_novelty_score_mean, 4)
            else:
                empirical_novelty_score_mean = "Null"
            if len(correctness_score_list) != 0:
                correctness_score_mean = sum(correctness_score_list)/len(correctness_score_list)
                correctness_score_mean = round(correctness_score_mean, 4)
            else:
                correctness_score_mean = "Null"
            if len(recommendation_score_list) != 0:
                recommendation_score_mean = sum(recommendation_score_list)/len(recommendation_score_list)
                recommendation_score_mean = round(recommendation_score_mean, 4)
            else:
                recommendation_score_mean = "Null"
            if len(confidence_score_list) != 0:
                confidence_score_mean = sum(confidence_score_list)/len(confidence_score_list)
                confidence_score_mean = round(confidence_score_mean, 4)
            else:
                confidence_score_mean = "Null"
            #去除file中的.json
            file = file.split(".")[0]
            #将文件名，novelty_score的平均值，correctness_score的平均值，recommendation_score的平均值，confidence_score的平均值写入csv文件
           # with open("D:\\研究生-心理与行为大数据\\创造力\\Reviews\\Reviews\\ICLR2022\\Desk Rejected Withdrawn Submissions\\novelty_score\\Desk_noveltyscore.csv", "w", newline="") as f:
            #writer = csv.writer(f)
            #writer.writerow(["file", "technical_novelty_score_mean", "empirical_novelty_score_mean", "correctness_score_mean", "recommendation_score_mean", "confidence_score_mean"])
            writer.writerow([file, technical_novelty_score_mean, empirical_novelty_score_mean, correctness_score_mean, recommendation_score_mean, confidence_score_mean])

if __name__ == "__main__":
    path = "D:\\研究生-心理与行为大数据\\创造力\\Reviews\\Reviews\\ICLR2022\\Desk Rejected Withdrawn Submissions\\review_deal"
    read_jsons(path)



