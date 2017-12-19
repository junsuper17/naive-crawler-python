from __future__ import print_function
import os

class data_input:
  def __init__(self):
    self.obj = []
    self.file_path=os.path.dirname(os.path.realpath(__file__))+"/hwmc-utf8-test.csv"
    self.data_status=os.path.dirname(os.path.realpath(__file__))+"/status"
    print(self.file_path)
  def read_data(self):
    status={}
    if os.path.exists(self.data_status)==True:
      with open(self.data_status) as fin:
        for eachLine in fin:
          line=eachLine.strip().split(',')
          status[line[0]] = line[1] 
      fin.close()

    i = 0;
    with open(self.file_path) as fin:
      for eachLine in fin:
        line = eachLine.strip().decode('utf-8', 'ignore').split(',')
        line[0] = i
        if status.has_key(str(i))==False:
          status[str(i)] = 0
        line.append(status[str(i)])
        self.obj.append(line)
        i += 1
    fin.close()
    return self.obj

  def output_data(self,st=-1,ed=-1):
    if st>=0 and ed>=0 and ed>=st and ed<=len(self.obj) and st<=len(self.obj):
      for i in range(st, ed+1):
        print(i, self.obj[i].encode('utf-8'))
    else:
      for i in range(len(obj)):
        print(i, self.obj[i].encode('utf-8'))

