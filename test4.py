#coding:utf-8
  
a = open("name.txt","r")

l = a.read().split()
         
name = input('検索したい人の名前を入力してください\n---->')
         
if str(name) in l:
        row = str((l.index(name) + 1))
        print(name + 'は' + row + '行目にあります')
else: 
        print(name + 'は存在しません')

a.close()
