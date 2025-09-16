import numpy as np
from my_numpy.basenumpy import BaseNumpy

class ArraySearch(BaseNumpy):
    def __init__(self,arr):
        super().__init__()
        self.arr = arr
        
    def return_where(self,condition):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        x = np.where(condition(arr))
        print('-'*50)
        print(x)

    def return_search(self,value,side='left'):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        x = np.searchsorted(arr,value,side=side)
        print('-'*50)
        print(x)