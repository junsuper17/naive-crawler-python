from __future__ import print_function
from datasets import data_input 
import jieba 

obj_data=data_input.data_input()
data = obj_data.read_data()

def doit():
  for i in range(5):
    print(data[i])
    seg_list = jieba.cut_for_search(data[i][1])
    print("%s   ||" %data[i], end='')
    print(",".join(seg_list))


if __name__=="__main__":
  doit()
