import numpy as np
from my_numpy.basenumpy import BaseNumpy

class ArraySplit(BaseNumpy):
    def __init__(self,arr):
        super().__init__()
        self.arr = arr

    def return_split(self,nums,axis=0,return_loop=False,h=False,v=False,d=False):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        newarr = np.array_split(arr,nums,axis=axis)
        # hsplit(): split 2-d to many 2-d along columns
        if h:
            newarr = np.hsplit(arr,nums)
        if v:
            newarr = np.vsplit(arr,nums)
        if d:
            newarr = np.dsplit(arr,nums)
        if return_loop:
            for x in range(0,nums):
                print(f'{x} of arr: {newarr[x]}')
        print('-'*40)
        print(newarr)