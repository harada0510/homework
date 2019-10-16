#coding:utf-8
#123456789を並び替えてできる組み合わせを全て出力

import itertools
          
num = '123456789'
          
list = [''. join(i) for i in itertools.permutations(num)]
        
print("順列の個数：{0}".format(len(list)))
             
print(list)
