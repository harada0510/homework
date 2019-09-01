#name.txtの中に"Aladdin"という名前が存在するかどうかを確かめる
#また，存在する場合には何行目にあるのかもprint

#coding:utf-8
  
a = open("name.txt","r")

l = a.read().split()

if 'Aladdin' in l:
        row = str(l.index('Aladdin') + 1)
        print('Aladdinは' + row + '行目にあります')
else: 
        print('Aladdinは存在しません')

a.close()
