import re
from tkinter import N


#s='1999,xxxxxxxxxxffffffff'
#s= "I'm Bob.2001a,\nWhat's your name?"
#re.split('\d\d\d\d\w,',s)
#re.split('\d\d\d\d\w,\n',s)
#re.split('\d\d\d\d,|\d\d\d\d\w,\n',s)

s="Distribution-aware adaptive multi-bit quantization. In\nProceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition, 1999. pp.\n9281-9290, 2021b.\nAojun Zhou"
re.split(', \d\d\d\d.|, \d\d\d\d\w.',s)

'''
处理文本中的换行符
'''
list1 = ["Starbucks\n", "has the \nbest", "coffee\n\n "]
rez = []

for x in list1:
    rez.append(x.replace("\n", ""))

print("New list : " + str(rez))

