from codecs import readbuffer_encode
import re
from tkinter import N


#s='1999,xxxxxxxxxxffffffff'
#s= "I'm Bob.2001a,\nWhat's your name?"
#re.split('\d\d\d\d\w,',s)
#re.split('\d\d\d\d\w,\n',s)
#re.split('\d\d\d\d,|\d\d\d\d\w,\n',s)

s="F. d'Alche-Buc, E. Fox, and R. Garnett . Towards understanding regularization in batch normalization. Advances in Neural Information Processing Systems,volume 32. Curran Associates, Inc., 2019."
'''
以第一个前一个字符不是大写字母的句号对句子进行分割
'''
def filter_re2(string):
    
        names = re.search(r'.*?[^A-Z]\.', string).group(0)
    
        #return names.rstrip('.').split(',')
        return names



#a = "123abc456"
#re.search("([0-9])([a-z])([0-9])",a).group(0) #123abc456
a = "123abc456"
print(re.search("([0-9]*)([a-z]*)([0-9]*)",a).group(3))


print(filter_re2(s))
#print(result)    
print(s.split(filter_re2(s)))
reff=s.split(filter_re2(s))
reftrue=reff[1]
print(reftrue.split('.'))

#print(s.split('.'))

'''
if test_str==None:
    print("没有没有真没有特殊字符")
else:
    print("该文本包含特殊字符")
'''

#re.split('. \d\n',s)
#print(re.split('. \d\n',s))

'''
处理文本中的换行符

list1 = ["Starbucks\n", "has the \nbest", "coffee\n\n "]
rez = []

for x in list1:
    rez.append(x.replace("\n", ""))

print("New list : " + str(rez))

#s = "A=3, B=value one, value two, value three, C=NA, D=Other institution, except insurance, id=DRT_12345"
#re.findall(r'\S+=.*?(?=, \S+=|$)', s)

s="Value-aware quantization for training and inferenceof neural networks, In Proceedings of the European Conference on Computer Vision (ECCV), pp"
s.rsplit(',', 1)
print(s.rsplit(',', 1))
'''