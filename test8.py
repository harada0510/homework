#coding:utf-8
#1122334455を並び替えてできる組み合わせを全て出力

import itertools

num = '1122334455'

list1 = [''. join(i) for i in itertools.permutations(num)]

list2 = set(list1)

print("順列の個数(重複なし)：{0}".format(len(list2)))
print(list2)
