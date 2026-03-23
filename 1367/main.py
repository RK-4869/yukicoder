# # ---問題文---
# # 文字列 S が与えられます。
# # 以下の操作を0回以上行って文字列をkadomatsuと一致させられるかどうか判定してください。

# # 好きな1文字を好きな位置に挿入する。先頭や末尾に挿入しても良い。
# 挿入操作を0回以上行って文字列をkadomatsuに出来るならばYes、 出来ないならばNoを出力してください。



# #文字列をinput関数を使用して標準入力させる。
s = input()
#kadomatsuに一致させるかなので、got変数を"kadomatsu"にする。
got = "kadomatsu"

#sの何文字目をチェックしているかを表す番号を示す。
check_s = 0

#gotを1文字ずつ取り出す
for char in got:
    #今見ているgotの文字列が現在と同じものか　かつ　全部確認できていないものとしたら
    if check_s < len(s) and char == s[check_s]:
        check_s = check_s +1

if check_s == len(s):
    print("Yes")
else:
    print("No")