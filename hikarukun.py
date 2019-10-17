#!/usr/bin/python3
# -*- coding: utf-8 -*-

import math
import itertools

#　引数１，２のどちらかがn桁の整数でないとき、0を返す。
#　引数１，２がn桁の整数（int）のとき、それぞれの引数の数字を並び替えて、重複を許さず新たな数字の列を作る。
#　その数字のリストのうち、それぞれの引数から作成した数字の列を比較して、３数字以上連続で同じ並びになる組み合わせの個数と、組み合わせのリストを返す。（重複を許さない）
#引数１，２＝n桁（3桁以上）のint型　返り値＝組み合わせ数、組み合わせのリスト　（エラー、組み合わせが0のとき、組み合わせ数は0と返し、からのリストが返される。
def check_combination(arg1,arg2):
    #定数
    #組み合わせが０のとき
    NO_COMBINATION = 0
    #引数が適切でないとき(int型でないとき)
    WRONG_ARGUMENT_ERROR = 0
    #引数が3桁以下の数字のとき
    SHORT_INTEGER = 0
    #組み合わせ数
    combination_nomber = 0
    #組み合わせのリスト（二次元リスト）
    combination_list = []
    #arg1の桁数
    digits1 = 0
    #arg2の桁数
    digits2 = 0
    #引数１の数字を一つずつ要素に分けたリスト
    arg1_list = []
    #引数２の数字を一つずつ要素に分けたリスト
    arg2_list = []
    #引数1を並び替えてできる数字の列の組み合わせリスト
    arg1_permutation_list = []
    #引数2を並び替えてできる数字の列の組み合わせリスト
    arg2_permutation_list = []    
    #引数1の中に、それぞれの数字がいくつ含まれているか。左から右に0~9がそれぞれ該当。
    arg1_3perm_list = []
    #引数1の中に、それぞれの数字がいくつ含まれているか。左から右に0~9がそれぞれ該当。
    arg2_3perm_list = []
    #共通の3桁の順列を入れるリスト
    common_3perm_list = []


    #もしも引数がint型でなかったら、エラーを吐く。
    if not check_integer(arg1,arg2):
        return WRONG_ARGUMENT_ERROR, combination_list
    else:
        #len関数などを使うため、strに変換しておく。
        arg1 = str(arg1)
        arg2 = str(arg2)
        #桁数を代入する
        digits1 = len(arg1)
        digits2 = len(arg2)

        #test
        print("debug log Start:")
        print("========================================")
        print("桁数1:{0}".format(digits1))
        print("桁数2:{0}" .format(digits2))
        #

        #3桁より引数が短いとき、終了する。
        if digits1 < 3 | digits2 < 3:
            return SHORT_INTEGER, combination_list
        else:
            #引数の数字を一つずつの要素にしてリストに格納する。
            arg1_list = to_list(arg1,arg1_list)
            arg2_list = to_list(arg2,arg2_list)
            #test
            print("list1:{0}".format(arg1_list))
            print("list2:{0}".format(arg2_list))
            #
            #数字を入れ替えてできるすべての数字の列（タプル型で一つずつ区切り）をリストにして格納する。（重複を許さない）
            arg1_permutation_list = all_permutations(arg1_list,arg1_permutation_list)
            arg2_permutation_list = all_permutations(arg2_list,arg2_permutation_list)
            #test
            #print("perm1:{0}コ".format(len(arg1_permutation_list)))
            #print("perm2:{0}コ".format(len(arg2_permutation_list)))
            #
            #それぞれの引数の3つの数字の順列(タプル型)のリストを作成する（重複を許さない）
            arg1_3perm_list = three_permutations(arg1_list,arg1_3perm_list)
            arg2_3perm_list = three_permutations(arg2_list,arg2_3perm_list)
            
            #test
            print("3perm1:{0}".format(arg1_3perm_list))
            print("3perm2:{0}".format(arg2_3perm_list))
            #

            #それぞれの3つの数字の順列のうち、共通のものを取り出す。
            common_3perm_list = common_element(arg1_3perm_list,arg2_3perm_list,common_3perm_list)

            
            #test
            print("common_3perm:{0}".format(common_3perm_list))
            #

            #正規表現ツールを使うため、タプルの順列をstrの順列に直す
            arg1_permutation_list = tupplelist_to_strlist(arg1_permutation_list)
            arg2_permutation_list = tupplelist_to_strlist(arg2_permutation_list)
            common_3perm_list = tupplelist_to_strlist(common_3perm_list)
            
            #test
            #print("perm1:{0}".format(arg1_permutation_list))
            #print("perm2:{0}".format(arg2_permutation_list))
            #print("common_3perm:{0}".format(common_3perm_list))
            #
            #共通の3つの並びをもつ組み合わせを返す
            combination_list = have_common3_check(arg1_permutation_list,arg2_permutation_list,common_3perm_list)
            combination_nomber = len(combination_list)

            #test
            print("debug log End:")
            print("========================================")

    return combination_nomber,combination_list

#引数が半角数字配列であった場合にはtrueを返す。違ったら、FALSEを返す。
def check_integer(arg1,arg2):
    if is_int(arg1) and is_int(arg2):
        return True
    else:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

#数字とリストを引数にもち、数字を一つずつの要素に分けてリストに格納して返り値とする。
def to_list(int_arg,arg_list):
    arg_list = []
    arg_len = len(int_arg)
    for i in range(0,arg_len):
        arg_list.append(int_arg[i:i+1])
    return arg_list

#引数のリストの階乗の順列から重複を除いたものをタプルのリストで返す
def all_permutations(arg_list,arg_perm_list):
    for i in itertools.permutations(arg_list):
        arg_perm_list.append(i)
    #重複を消す
    arg_perm_list = list(set(arg_perm_list))
    return arg_perm_list

#3つの数字だけ選んで、順列を作り、重複を消して返す。
def three_permutations(arg_list,arg_3perm_list):
    for i in itertools.permutations(arg_list,3):
        arg_3perm_list.append(i)
    #重複を消す
    arg_3perm_list = list(set(arg_3perm_list))
    return arg_3perm_list

#リストの中の共通のものを取り出して返す
def common_element(list_perm1,list_perm2,list_common_perm):
    common_perm = list(set(list_perm1) & set(list_perm2))
    return common_perm

#タプルのリストから、タプルの中身を結合して文字列(str型)にしたリストを作成する。
def tupplelist_to_strlist(tupplelist):
    #返すリスト。タプルではなく、strが入っている。
    str_list = []
    for tupple in tupplelist:
        string_from_tupple = ""
        for char in tupple:
            string_from_tupple += char
        str_list.append(string_from_tupple)
    return str_list

#common_listに含まれる文字列を持つ組み合わせを、list1とlist2から取り出してきて、組み合わせリストを返す。
def have_common3_check(list1,list2,common_list):
    #returnする最終的なもの
    list_combination = []
    #3桁の数字：それを含むもののリスト　形式の辞書　{"123":["123456","412356"],}のような形式
    list1_common = {}
    list2_common = {}
    for common3 in common_list:
        list1_pre = []
        list2_pre = []
        for item1 in list1:
            if common3 in item1:
                list1_pre.append(item1)
        for item2 in list2:
            if common3 in item2:
                list2_pre.append(item2)
        list1_common[common3] = list1_pre
        list2_common[common3] = list2_pre

    for common3 in common_list:
        #list1_common[common3].valueとlist2_common[common3].valueはlist型
        for item1 in list1_common[common3]:
            for item2 in list2_common[common3]:
                list_combination.append([item1,item2])
        
    #重複の組み合わせを消す（これでは、[0,1]と[1,0]が違うと認識してしまうかも、、、これは一緒と捉えて消してほしい。）
    list_combination = list(map(list,set(map(tuple,list_combination))))
    return list_combination


if __name__ == '__main__':
    print("数字を二つ入力してください（半角スペース空けてください）")
    print("その文字を並び替えて、3つ連続の数字ができるペアを返します")
    s = input().split()
    combination_nomber,combination_list = check_combination(s[0],s[1])
    print("見つかった組み合わせ数：{0}".format(combination_nomber))
    print("見つかった組み合わせ：{0}".format(combination_list))
