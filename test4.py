#test3.pyにおいて,名簿検索プログラム
#「検索したい人の名前を入力してください」と表示させてユーザに入力させる
#入力された人の名前が存在するか検索
#検索結果を返す

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
