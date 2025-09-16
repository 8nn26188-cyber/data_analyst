import numpy as np
from my_numpy.basenumpy import BaseNumpy

class ArraySort(BaseNumpy):
    def __init__(self,arr):
        super().__init__()
        self.arr = arr

    def return_sort(self):
        arr = self.ini_np(self.arr,return_print=False,return_arr=True)
        print('-'*40)
        print(np.sort(arr))