import json
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

                empirical_novelty_score_list.append(empirical_novelty_score)
                technical_novelty_score_list.append(technical_novelty_score)
                correctness_score_list.append(correctness_score)
                recommendation_score_list.append(recommendation_score)
                confidence_score_list.append(confidence_score)
                
            print(technical_novelty_score_list)
            print(empirical_novelty_score_list)
            #去除file中的.json
            file = file.split(".")[0]
            #将list technical_novelty_score_list 和empirical_novelty_score_list写入csv
            import csv
            with open("D:\\研究生-心理与行为大数据\\创造力\\Reviews\\Reviews\\ICLR2022\\Desk Rejected Withdrawn Submissions\\novelty_score\\" + file + ".csv", "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerow(["technical_novelty_score", "empirical_novelty_score", "correctness_score", "recommendation_score", "confidence_score"])
                #写入列
                for i in range(len(technical_novelty_score_list)):
                    writer.writerow([technical_novelty_score_list[i], empirical_novelty_score_list[i], correctness_score_list[i], recommendation_score_list[i], confidence_score_list[i]])

if __name__ == "__main__":
    path = "D:\\研究生-心理与行为大数据\\创造力\\Reviews\\Reviews\\ICLR2022\\Desk Rejected Withdrawn Submissions\\review_deal"
    read_jsons(path)



