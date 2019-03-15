# (C)Copyright Brian Zheng 2019, all rights reserved
# This file is under the Apache 2.0 license, for more information, visit the LICENSE.txt file
from scipy.spatial.distance import euclidean

import collections
import numpy as np

class main:
  # Source code for the K-Best-Average Algorithm(In development)
  # The class "main" requires x_train and y_train for training test data,
  # and the x value for which we need to predict the y
  # The optional arguments are n, the number of y you want to
  # calculate the average, the K, the distance away from the input # value and all cases within
  # K will be taken for average calculation
  # This algorithm is a lazy learning algorithm

  def __init__(self):
    # n and K defaults to None
    # It is ok to have n and K set a positive integer at the same time,
    # that will take n cases from K and calculate their average
    self.avg_list = []
    pass
  
  def find_outlier(self, ds):
    self.ds = sorted(ds)
    self.o = []
    q1, q3= np.percentile(self.ds,[25,75])
    iqr = q3 - q1
    lower_bound = q1 -(1.5 * iqr) 
    upper_bound = q3 +(1.5 * iqr) 
    for i in self.ds:
      if i < lower_bound or i > upper_bound:
        self.o.append(i)
      else:
        pass
    return self.o

  def split_data(self, input_data, p):
    if p > 1:
      raise Exception("p value should not be bigger than 1")
    else:
      self.ir = [input_data[0 : int(len(input_data) * p)]]
      for f in self.ir[0]:
        input_data.remove(f)
      return self.ir[0], input_data
    pass

  def train(self, xydict):
    # As this a lazy learning function, there is not an actual "train"
    # function, it is more like an init function
    self.xydict = xydict
    self.dist_list = []
  def predict(self, input_x, n, K):
    # Fix: input_x must be a tuple to represent to coords of the x to predict
    self.flist = []
    self.dist_dict = {}
    self.input_x = input_x
    x_list = sorted(self.xydict, key=self.xydict.get)
    #print(x_list)
    for i in range(len(input_x)):
      #print(i)
      self.t = input_x[i]
      #print(self.t)
      #print(x_list)
      for a in x_list:
        #print(a)
        self.f = (a)
        #print(self.f)
        #append this to a list
        #print(self.xydict[f])
        self.dist_dict[self.f] = (euclidean(list(a), list(self.t)))
      self.flist = []
      # Combine dist_list to a dict
    self.n = n
    self.K = K
    self.xydict = dict(sorted(self.xydict.items(), key = lambda x:x[0]))
    #print(self.n)
    #print(len(list(self.dist_dict.keys())))
    #fix this!!!
    if self.n > len(list(self.dist_dict.keys())):
      raise Exception("n is smaller than the total amount of cases")

    else:
      #print(self.xydict)
      r = list(self.dist_dict.keys())
      self.invert_dict = inv_map = {v: k for k, v in self.xydict.items()}
      #self.xydict = sorted(self.xydict.items(), key=lambda kv: kv[1])
      for i in range(self.n):
        #calculate the average
        #print(self.xydict[r[i]])
        if self.dist_dict[self.invert_dict[self.xydict[r[i]]]] < K:
          self.avg_list.append(list(self.xydict[r[i]]))
      if len(self.avg_list) < self.n:
        raise Exception("There are not enough cases to satify n")
      data = np.array(self.avg_list)
      return tuple(np.average(data, axis=0).tolist()) #https://stackoverflow.com/questions/55153446/getting-the-average-of-a-list-of-coordinates-in-python
      
