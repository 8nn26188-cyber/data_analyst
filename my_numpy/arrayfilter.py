import numpy as np
from my_numpy.basenumpy import BaseNumpy

class ArrayFilter(BaseNumpy):
    def __init__(self,arr):
        super().__init__()
        self.arr = arr

    def return_arr(self,filter_arr):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        newarr = arr[filter_arr]
        print(filter_arr)
        print(newarr)
    
    def filter_loop(self,condition):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        filter_arr = [condition(element) for element in arr]
        return filter_arr

    def no_loop(self,condition):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        filter_arr = condition(arr)
        return filter_arr